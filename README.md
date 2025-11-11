# pygame_sl

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
<!-- Add these badges once CI/CD is set up:
[![Build Status](https://github.com/DejanS24/pygame_sl/workflows/CI/badge.svg)](https://github.com/DejanS24/pygame_sl/actions)
[![Coverage](https://img.shields.io/badge/coverage-70%25-green.svg)](https://github.com/DejanS24/pygame_sl)
-->

A Domain-Specific Language (DSL) for generating 2D platform games in Python using the pygame library.

**pygame_sl** makes it easy for anyone to design their own 2D platform game using a simple, intuitive syntax. No need to write complex game logic—just describe your game and let pygame_sl generate the code!

---

## 🎮 Features

- **Simple Player Configuration**: Define player avatar with colors or images, including animations (walk, idle, jump)
- **Multiple Item Types**: Add collectible points and speed boosts to enhance gameplay
- **Level Designer**: Create multiple levels with custom backgrounds and platforms
- **Platform Customization**: Define platform positions, textures, and dimensions
- **Sound Support**: Add background music, sound effects for jumps, item pickups, and game ending
- **Flexible Settings**: Customize game title, FPS, move speed, screen size, default colors, and fonts
- **Automatic Code Generation**: Generates clean, working Python/pygame code from your DSL file

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/DejanS24/pygame_sl.git
cd pygame_sl

# Install in development mode
pip install -e .
```

### Install dependencies

```bash
# Runtime dependencies
pip install -r requirements.txt

# Development dependencies (for testing and contributing)
pip install -r requirements-dev.txt
```

---

## 🚀 Quick Start

### 1. Create a `.pg` file

Create a file named `my_game.pg`:

```
game "My First Platformer"

player {
    color blue
    height 75
    width 50
}

level Level1 {
    background color yellow
    platform {
        position 300 420
        height 50
        width 200
    }
}

level Level2 {
    background color green
    platform {
        position 400 450
        height 50
        width 150
    }
}
```

### 2. Generate Python code

```bash
textx generate my_game.pg --target python
```

This creates `my_first_platformer.py` in the same directory.

### 3. Run your game

```bash
python my_first_platformer.py
```

Use arrow keys to move and jump. Reach the right side to advance to the next level!

---

## 📖 Documentation

- **[Tutorial](docs/TUTORIAL.md)** - Step-by-step guide to creating your first game
- **[Grammar Reference](docs/GRAMMAR_REFERENCE.md)** - Complete DSL syntax documentation
- **[Examples](docs/EXAMPLES.md)** - Annotated example walkthroughs
- **[Contributing](docs/CONTRIBUTING.md)** - Guidelines for contributors
- **[Changelog](docs/CHANGELOG.md)** - Version history and changes

---

## 🎨 Example with Images and Animations

```
game "Pokemon Platformer"

player {
    image "assets/players/pikachu_default.png"
    walk image "assets/players/pikachu_walk.png"
    idle image "assets/players/pikachu_idle.png"
    jump image "assets/players/pikachu_jump.png"
    height 100
    width 80
}

point coins {
    image "assets/items/coin.png"
}

boost speed {
    color green
}

level Level1 {
    background image "assets/backgrounds/forest.jpg"

    platform {
        position 460 460
        texture image "assets/platforms/grass.png"
        height 30
        width 80
    }

    point coins {
        position 500 380
    }

    boost speed {
        position 700 400
    }
}

settings {
    title "My Pokemon Adventure"
    fps 60
    screen width 1024
    screen height 768
}
```

See the [examples/](examples/) directory for more complete examples.

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=lang --cov=generator --cov-report=html

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration
```

---

## 🛠️ Development

### Setting up development environment

```bash
# Install in development mode with dev dependencies
pip install -e .
pip install -r requirements-dev.txt

# Run code formatting
black .

# Run linter
ruff check .

# Run type checker
mypy lang/ generator/
```

### Using Make commands

```bash
make install     # Install dependencies
make test        # Run tests
make format      # Format code
make lint        # Run linters
make clean       # Clean build artifacts
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Quick contribution guide:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and add tests
4. Run the test suite (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎓 Academic Context

This project was created for the JSD (Jezici Specifični za Domen / Domain-Specific Languages) course.

---

## 📧 Contact

**Dejan Sorgic**
- Email: dejans1224@gmail.com
- GitHub: [@DejanS24](https://github.com/DejanS24)

---

## 🙏 Acknowledgments

- Built with [textX](https://github.com/textX/textX) - a meta-language for building DSLs
- Powered by [pygame](https://www.pygame.org/) - a cross-platform set of Python modules for games
- Template rendering with [Jinja2](https://jinja.palletsprojects.com/)

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError: No module named 'textx'`
**Solution**: Install dependencies with `pip install -r requirements.txt`

**Problem**: Generated game window doesn't open
**Solution**: Make sure pygame is installed: `pip install pygame`

**Problem**: Asset files not found when running generated game
**Solution**: Use relative paths in your .pg file, and ensure asset files exist in the specified locations

For more help, please [open an issue](https://github.com/DejanS24/pygame_sl/issues).
