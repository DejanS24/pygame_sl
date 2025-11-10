# Contributing to pygame_sl

Thank you for your interest in contributing to pygame_sl! This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [How to Contribute](#how-to-contribute)
5. [Coding Standards](#coding-standards)
6. [Testing Guidelines](#testing-guidelines)
7. [Submitting Changes](#submitting-changes)
8. [Reporting Bugs](#reporting-bugs)
9. [Suggesting Features](#suggesting-features)

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and considerate in all interactions.

**Expected behavior:**
- Be respectful and professional
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what is best for the community

**Unacceptable behavior:**
- Harassment, discrimination, or offensive comments
- Personal attacks or trolling
- Publishing others' private information

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account
- Basic knowledge of Python and DSLs

### Useful Resources

- [textX documentation](http://textx.github.io/textX/)
- [pygame documentation](https://www.pygame.org/docs/)
- [Jinja2 documentation](https://jinja.palletsprojects.com/)

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/pygame_sl.git
cd pygame_sl
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e .
pip install -r requirements-dev.txt
```

### 3. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes:
git checkout -b fix/bug-description
```

### 4. Verify Setup

```bash
# Run tests to ensure everything works
pytest

# Try generating a sample game
textx generate examples/game1.pg --target python
```

---

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues in the code
- **New features**: Add new DSL features or generator capabilities
- **Documentation**: Improve docs, tutorials, or examples
- **Tests**: Add or improve test coverage
- **Examples**: Create new example games
- **Performance**: Optimize code generation or runtime

### Finding Work

- Check the [Issues](https://github.com/DejanS24/pygame_sl/issues) page
- Look for issues labeled `good-first-issue` or `help-wanted`
- Ask in issues if you'd like to work on something

---

## Coding Standards

### Python Style

We follow PEP 8 with some modifications:

```bash
# Format code with black
black .

# Check code with ruff
ruff check .

# Type check (optional but recommended)
mypy lang/ generator/
```

### Code Organization

- **lang/**: Grammar and model processing
  - Keep grammar simple and intuitive
  - Add validation in model_processor.py
  - Document grammar changes

- **generator/**: Code generation
  - Template logic in pygame.template
  - Helper functions in __init__.py
  - Utilities in util.py

- **tests/**: All tests
  - Unit tests for individual components
  - Integration tests for full workflow
  - Use descriptive test names

### Comments and Documentation

```python
# Good: Explains why
# Use custom filter to handle animation variations
animation = avatar | animation_level

# Bad: States the obvious
# Set x to 5
x = 5
```

**Docstrings for functions:**

```python
def python_module_name(name):
    """
    Convert game name to valid Python module filename.

    Args:
        name (str): Game name from DSL

    Returns:
        str: Valid Python filename (lowercase, underscores, .py extension)

    Example:
        >>> python_module_name("My Game!")
        'my_game_.py'
    """
    return "%s.py" % re.sub(r'[^\w\.-]', '_', name.lower())
```

---

## Testing Guidelines

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_generator.py

# Run with coverage
pytest --cov=lang --cov=generator --cov-report=html

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration
```

### Writing Tests

**Every contribution should include tests:**

1. **Unit tests** for new functions:

```python
@pytest.mark.unit
def test_color_validation():
    """Test that color validation works correctly."""
    assert check_color_existing('color', 'blue') is False
    assert check_color_existing('color', 'purple') is True
```

2. **Integration tests** for new features:

```python
@pytest.mark.integration
def test_new_feature_end_to_end(metamodel, tmp_path):
    """Test new feature from DSL to generated code."""
    # Parse .pg file
    model = metamodel.model_from_file('test_file.pg')

    # Generate code
    generate(model, output_path=tmp_path)

    # Verify output
    assert output_file.exists()
```

### Test Coverage

- Aim for >70% code coverage
- All new code should have tests
- Update tests when modifying existing code

---

## Submitting Changes

### Before Submitting

1. **Run tests**: Ensure all tests pass

```bash
pytest
```

2. **Format code**: Apply formatting

```bash
black .
ruff check .
```

3. **Update documentation**: If needed

4. **Add yourself to contributors**: (optional)

### Commit Messages

Write clear, descriptive commit messages:

**Format:**
```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what changed and why, not how.

- Bullet points for multiple changes
- Reference issues: Fixes #123
```

**Good examples:**
```
Add validation for platform positions

Platforms with negative coordinates or positions outside the screen
are now validated and reported with helpful error messages.

Fixes #45
```

```
Improve code generation performance

Optimize Jinja2 template rendering by caching environment.
Reduces generation time by ~30% for large games.
```

**Bad examples:**
```
Fixed bug
```

```
Updated stuff
```

### Pull Request Process

1. **Push to your fork:**

```bash
git push origin feature/your-feature-name
```

2. **Open a pull request** on GitHub

3. **Fill out the PR template:**
   - Describe what changed
   - Link related issues
   - Add screenshots/examples if applicable

4. **Respond to review feedback:**
   - Address all comments
   - Make requested changes
   - Re-request review when ready

5. **After approval:**
   - Maintainer will merge your PR
   - Your changes will be in the next release!

---

## Reporting Bugs

### Before Reporting

1. **Search existing issues**: Check if it's already reported
2. **Try latest version**: Update to the latest code
3. **Minimal reproduction**: Create smallest example that shows the bug

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Create file with content: '...'
2. Run command: '...'
3. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**.pg file example**
```
game "Bug Example"
...
```

**Error message**
```
Traceback (most recent call last):
...
```

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.10.5]
- pygame_sl version: [e.g., 0.1]
```

---

## Suggesting Features

We love feature suggestions! Before suggesting:

1. **Check existing issues**: Maybe it's already planned
2. **Consider scope**: Should it be in pygame_sl or a separate tool?
3. **Think about DSL design**: How would it fit the language?

### Feature Request Template

```markdown
**Feature description**
Clear description of the feature.

**Use case**
Why would this be useful? What problem does it solve?

**Proposed DSL syntax**
```
level MyLevel {
    new_feature {
        // Example of how it might work
    }
}
```

**Alternative solutions**
Are there other ways to achieve this?

**Additional context**
Screenshots, examples, references, etc.
```

---

## Development Workflow

### Typical Workflow

1. Choose an issue or feature
2. Create a branch
3. Make changes
4. Write tests
5. Run tests and formatting
6. Commit with clear message
7. Push to your fork
8. Open pull request
9. Respond to feedback
10. Celebrate when merged! 🎉

### Getting Help

- **Questions**: Open an issue with the `question` label
- **Discussion**: Use GitHub Discussions (if enabled)
- **Email**: Contact maintainer at dejans1224@gmail.com

---

## Recognition

Contributors will be:
- Listed in the contributors section
- Mentioned in release notes
- Appreciated forever! ❤️

---

## License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

## Thank You!

Your contributions make pygame_sl better for everyone. Thank you for taking the time to contribute! 🙌
