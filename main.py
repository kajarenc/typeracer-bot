import asyncio
from typeracer_bot import TypeRacerBot


async def main():
    print("TypeRacer Bot")
    print("-" * 40)

    wpm = input("Enter target WPM (default 60): ").strip()
    wpm = int(wpm) if wpm else 60

    headless = input("Run headless? (y/N): ").strip().lower() == "y"

    bot = TypeRacerBot(wpm=wpm, variation=0.15)

    print(f"\nStarting bot with {wpm} WPM...")
    await bot.run_practice_race(headless=headless)


if __name__ == "__main__":
    asyncio.run(main())
