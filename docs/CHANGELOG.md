# Changelog

All notable changes to pygame_sl will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive testing infrastructure with pytest
- Unit tests for model processor and generator
- Integration tests for end-to-end workflows
- Complete documentation suite (Tutorial, Grammar Reference, Examples, Contributing)
- MIT License
- Development dependencies (pytest, black, ruff, mypy)
- .gitignore for Python projects
- Enhanced README with badges, examples, and troubleshooting
- Examples assets directory with documentation
- Code quality configuration files (.editorconfig, pyproject.toml, pre-commit hooks)
- GitHub Actions CI/CD workflow
- Makefile for common development tasks
- MANIFEST.in for proper package distribution

### Changed
- Updated examples to use portable relative paths instead of hardcoded Windows paths
- Enhanced README with comprehensive documentation and visual improvements
- Updated setup.py with package classifiers and metadata
- Improved error messages in model processor with helpful suggestions

### Fixed
- Critical bug in pygame.template: `screen.f(BLUE)` → `screen.fill(BLUE)` (line 299)
- Added missing `pygame` dependency to install_requires
- Fixed asset path portability issues in example files

## [0.1.0] - Initial Release

### Added
- Core DSL grammar for 2D platform games
- Player configuration with colors or images
- Animation support (walk, idle, jump)
- Two item types: points (collectibles) and boosts (speed powerups)
- Level system with backgrounds and platforms
- Sound support (background music, sound effects)
- Customizable game settings (FPS, screen size, move speed, etc.)
- Code generation to pygame Python files
- TextX integration for DSL parsing
- Jinja2 templating for code generation
- Basic examples (game1.pg, pikachu_game.pg)

### Features
- **Player avatars**: Color-based or image-based with optional animations
- **Items**: Collectible points and speed boost powerups
- **Levels**: Multiple levels with image or color backgrounds
- **Platforms**: Customizable platforms with optional textures
- **Sound system**: Background music and event-based sound effects
- **Settings**: Comprehensive game customization options

---

## Version History

### [0.1.0] - Initial Release
- First working version created for JSD course
- Core DSL functionality implemented
- Basic code generation working

---

## Upgrade Guide

### From 0.1.0 to Unreleased

**Breaking Changes:**
- None

**New Features:**
- Testing framework available
- Comprehensive documentation added
- Development tools configured

**Migration Steps:**
1. Update your installation: `pip install -e .`
2. Install new dependencies: `pip install -r requirements.txt`
3. (For developers) Install dev dependencies: `pip install -r requirements-dev.txt`
4. Update asset paths in .pg files to use relative paths

**Asset Path Updates:**

Before (absolute paths):
```
player {
    image "C:/Users/Name/Desktop/player.png"
}
```

After (relative paths):
```
player {
    image "assets/players/player.png"
}
```

---

## Future Plans

### Planned for 1.0.0
- [ ] Asset path validation during model processing
- [ ] Better error messages with line numbers
- [ ] `--validate` flag to check .pg files without generating
- [ ] Additional platform types (moving platforms, breakable platforms)
- [ ] Enemy support
- [ ] More animation types
- [ ] Level editor tool
- [ ] GUI for creating games
- [ ] PyPI package publishing

### Under Consideration
- Interactive tutorial mode
- Export to other game engines
- Multiplayer support
- Save/load game state
- Custom player controls configuration
- Particle effects support
- Camera system improvements

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to pygame_sl.

---

## Acknowledgments

Thanks to all contributors who have helped make pygame_sl better!

---

## Links

- [Homepage](https://github.com/DejanS24/pygame_sl)
- [Issue Tracker](https://github.com/DejanS24/pygame_sl/issues)
- [Documentation](https://github.com/DejanS24/pygame_sl/tree/main/docs)
