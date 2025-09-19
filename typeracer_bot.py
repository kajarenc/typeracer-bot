import asyncio
import random
from typing import Optional
from playwright.async_api import async_playwright, Page, Browser


class TypeRacerBot:
    def __init__(self, wpm: int = 60, variation: float = 0.1):
        self.wpm = wpm
        self.variation = variation
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None

    async def initialize(self, headless: bool = False):
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(
            headless=headless, args=["--disable-blink-features=AutomationControlled"]
        )
        context = await self.browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        self.page = await context.new_page()

    async def navigate_to_typeracer(self):
        if not self.page:
            raise RuntimeError("Bot not initialized. Call initialize() first.")

        await self.page.goto(
            "https://play.typeracer.com/", wait_until="domcontentloaded", timeout=60000
        )
        await asyncio.sleep(2)

    async def select_practice_mode(self):
        if not self.page:
            raise RuntimeError("Bot not initialized. Call initialize() first.")

        try:
            practice_button = await self.page.wait_for_selector(
                "a:has-text('Practice')", timeout=15000
            )
            await practice_button.click()
            await asyncio.sleep(2)

        except Exception as e:
            print(f"Trying alternative selector...")
            try:
                practice_link = await self.page.wait_for_selector(
                    "a[href*='practice'], .gwt-Anchor:has-text('practice')",
                    timeout=15000,
                )
                await practice_link.click()
            except:
                await self.page.goto(
                    "https://play.typeracer.com/?universe=lang_en&gameType=practice",
                    timeout=6000,
                )

    async def wait_for_race_start(self):
        if not self.page:
            raise RuntimeError("Bot not initialized. Call initialize() first.")

        await self.page.wait_for_selector(
            ".txtInput, input.txtInput", state="visible", timeout=30000
        )

    async def extract_text(self) -> str:
        if not self.page:
            raise RuntimeError("Bot not initialized. Call initialize() first.")

        text_elements = await self.page.query_selector_all("span[unselectable='on']")

        full_text = ""
        for element in text_elements:
            text = await element.text_content()
            if text:
                full_text += text

        return full_text.strip()

    async def type_text(self, text: str):
        if not self.page:
            raise RuntimeError("Bot not initialized. Call initialize() first.")

        input_field = await self.page.query_selector(".txtInput, input.txtInput")
        if not input_field:
            raise RuntimeError("Could not find input field")

        chars_per_minute = self.wpm * 5 * 1.8
        base_delay = 60000 / chars_per_minute

        await input_field.focus()

        for char in text:
            delay_variation = random.uniform(1 - self.variation, 1 + self.variation)
            delay = base_delay * delay_variation

            await self.page.keyboard.type(char, delay=int(delay))

            if random.random() < 0.05:
                await asyncio.sleep(random.uniform(0.1, 0.3))

    async def run_practice_race(self, headless: bool = False):
        try:
            await self.initialize(headless=headless)

            print("Navigating to TypeRacer...")
            await self.navigate_to_typeracer()

            print("Selecting practice mode...")
            await self.select_practice_mode()

            print("Waiting for race to start...")
            await self.wait_for_race_start()

            await asyncio.sleep(1)

            print("Extracting text...")
            text_to_type = await self.extract_text()
            print(f"Text to type: {text_to_type[:50]}...")

            print(f"Starting to type at ~{self.wpm} WPM...")
            await self.type_text(text_to_type)

            print("Race completed!")

            await asyncio.sleep(5)

        except Exception as e:
            print(f"Error during race: {e}")

        finally:
            if self.browser:
                await self.browser.close()


async def main():
    bot = TypeRacerBot(wpm=90, variation=0.15)
    await bot.run_practice_race()


if __name__ == "__main__":
    asyncio.run(main())
