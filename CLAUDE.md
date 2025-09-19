# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a TypeRacer bot project written in Python for educational purposes. The bot automates typing on TypeRacer.com to demonstrate web automation techniques using Selenium WebDriver.

## Technical Stack

- **Language**: Python 3.12
- **Web Automation**: Selenium WebDriver
- **Browser**: Chrome/Chromium with ChromeDriver
- **Package Manager**: uv (preferred) or pip
- **Testing**: pytest
- **Code Quality**: ruff (linting), black (formatting)

## Development Commands

### Running the application
```bash
python main.py
```

### Running with options
```bash
python main.py --speed 80 --accuracy 95
python main.py --debug
```

### Installing dependencies
```bash
uv sync  # Preferred
# or
pip install -r requirements.txt
```

### Running tests
```bash
pytest tests/
```

### Code formatting and linting
```bash
ruff check --fix .
black .
```

## Project Structure

```
typeracer-bot/
├── main.py              # Entry point with CLI argument parsing
├── typeracer_bot.py     # Core bot implementation with TypeRacerBot class
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Locked dependencies (when using uv)
├── requirements.txt     # Python dependencies for pip
├── tests/              # Test suite
│   └── test_bot.py     # Bot functionality tests
└── README.md           # User-facing documentation
```

## Key Implementation Details

### TypeRacerBot Class (`typeracer_bot.py`)
- **Initialization**: Sets up WebDriver, configures typing speed and accuracy
- **Text Detection**: Locates and extracts race text from the page
- **Typing Simulation**: Implements human-like typing with:
  - Variable delays between keystrokes
  - Configurable WPM (words per minute)
  - Random error injection based on accuracy setting
  - Natural typing rhythm variations

### Configuration Options
- `TYPING_SPEED`: Target WPM (default: 60, range: 30-120)
- `ACCURACY`: Percentage accuracy (default: 95, range: 80-100)
- `HUMAN_DELAY`: Enable realistic typing patterns (default: True)
- `DEBUG_MODE`: Verbose logging for development (default: False)

## Dependencies to Install

When setting up the project, ensure these are in `pyproject.toml`:
```toml
[project]
dependencies = [
    "selenium>=4.0.0",
    "webdriver-manager>=4.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
    "black>=23.0.0",
]
```

## Important Guidelines

1. **Ethical Use**: This bot is for educational purposes only. Always emphasize responsible use and learning objectives.

2. **Error Handling**: Implement robust error handling for:
   - WebDriver initialization failures
   - Element not found exceptions
   - Network timeouts
   - Page load issues

3. **Human-like Behavior**: To make the bot behave naturally:
   - Add random variations in typing speed (±10-15%)
   - Include occasional pauses (thinking time)
   - Implement backspace corrections for errors
   - Vary delay between words slightly

4. **Testing**: Write tests for:
   - Text extraction accuracy
   - Typing speed calculations
   - Error injection logic
   - WebDriver initialization

5. **Security**: Never:
   - Store credentials in code
   - Use for competitive advantage
   - Bypass anti-bot measures aggressively

## Common Tasks

### Adding a new feature
1. Create feature branch
2. Implement in `typeracer_bot.py`
3. Add tests in `tests/`
4. Update README if user-facing
5. Run formatters and linters

### Debugging issues
- Enable debug mode: `python main.py --debug`
- Check ChromeDriver compatibility with Chrome version
- Verify element selectors haven't changed on TypeRacer
- Review browser console for JavaScript errors

## TypeRacer-Specific Details

### Page Elements (subject to change)
- Race text container: Usually in a span with specific class
- Input field: Text input where typing occurs
- Start button: Triggers race beginning
- WPM display: Shows current typing speed

### Anti-Bot Considerations
TypeRacer may have anti-bot measures. The educational implementation should:
- Not attempt to bypass security measures
- Respect rate limits
- Only use in practice/guest mode
- Include clear disclaimers about Terms of Service