# TypeRacer Bot

An educational Python bot for automating typing on TypeRacer.com, built for learning purposes and understanding web automation techniques.

## ⚠️ Disclaimer

**This project is for educational purposes only.** Using bots on TypeRacer may violate their Terms of Service. This tool should only be used:
- For learning web automation techniques
- In practice/guest mode
- Never in competitive races or to gain unfair advantages
- With respect for other players and the platform

## Features

- Automated text recognition and typing
- Configurable typing speed and accuracy simulation
- Human-like typing patterns with variable delays
- Error simulation for more realistic behavior
- Support for practice mode

## Requirements

- Python 3.12 or higher
- Chrome/Chromium browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/typeracer-bot.git
cd typeracer-bot
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

## Usage

### Basic Usage

Run the bot in practice mode:
```bash
python main.py
```

### Configuration

You can configure the bot behavior by modifying settings in `typeracer_bot.py`:

- `TYPING_SPEED`: Words per minute (default: 60)
- `ACCURACY`: Typing accuracy percentage (default: 95)
- `HUMAN_DELAY`: Enable human-like delays between keystrokes

### Command Line Options

```bash
# Run with custom typing speed
python main.py --speed 80

# Run with custom accuracy
python main.py --accuracy 98

# Run in debug mode
python main.py --debug
```

## Project Structure

```
typeracer-bot/
├── main.py              # Entry point of the application
├── typeracer_bot.py     # Main bot implementation
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Locked dependencies (if using uv)
├── CLAUDE.md           # Instructions for Claude AI assistant
└── README.md           # This file
```

## Development


### Code Style

This project uses:
- `ruff` for linting and formatting.

## Ethical Considerations

This tool is created for educational purposes to understand:
- Web automation techniques
- Browser control via WebDriver
- DOM manipulation and element interaction
- Simulating human-computer interaction

**Please use responsibly and ethically.**
**Remember**: The purpose of this project is to learn, not to cheat. Respect the platform and other users.
