# from pygame_sl.generator import generator
import sys

colors = [
    "black",
    "blue",
    "red",
    "green",
    "yellow",
    "white"
]

# default values if none is given in .pg file
defaults = {
    'screen_width': 800,
    'screen_height': 600,
    'font': 'arial',
    'default_color': 'black',
    'fps': 60,
    'movespeed': 6,
    'default_texture_color': 'green'
}


def check_color_existing(key, value):
    """
    Check if a color value is invalid.

    Args:
        key (str): The setting key to check
        value: The value to validate

    Returns:
        bool: True if color is invalid, False otherwise
    """
    if 'color' in key:
        if value not in colors:
            return True
        else:
            return False
    else:
        return False


def get_color_suggestion(invalid_color):
    """
    Suggest a valid color based on invalid input.

    Args:
        invalid_color (str): The invalid color name

    Returns:
        str: Suggested valid color or empty string
    """
    invalid_lower = str(invalid_color).lower()

    # Simple similarity matching
    suggestions = {
        'purple': 'blue',
        'pink': 'red',
        'orange': 'red',
        'brown': 'red',
        'gray': 'black',
        'grey': 'black',
        'cyan': 'blue',
        'magenta': 'red',
    }

    if invalid_lower in suggestions:
        return suggestions[invalid_lower]

    # Default suggestion
    return 'blue'


def warning(message):
    """Print a warning message."""
    print(f"⚠️  WARNING: {message}", file=sys.stderr)


def info(message):
    """Print an info message."""
    print(f"ℹ️  INFO: {message}")


def set_default_settings(model):
    """
    Apply default settings to the model if not specified.

    Args:
        model: The game model to process
    """
    if not model.settings:
        model.settings = {}

    for key, value in defaults.items():
        try:
            attr_val = getattr(model.settings, key)
        except AttributeError:
            model.settings[key] = value
            continue

        if len(attr_val) == 0 or check_color_existing(key, attr_val[0]):
            if check_color_existing(key, attr_val[0]) and len(attr_val) > 0:
                warning(f"Invalid color '{attr_val[0]}' for setting '{key}'. Using default '{value}'.")
                warning(f"Valid colors are: {', '.join(colors)}")
            setattr(model.settings, key, value)
        else:
            setattr(model.settings, key, attr_val[0])


def validate_platforms(level):
    """
    Validate platform positions and dimensions.

    Args:
        level: The level object to validate
    """
    for idx, platform in enumerate(level.platforms):
        # Check for negative dimensions
        if platform.height <= 0:
            warning(f"Level '{level.name}': Platform #{idx+1} has invalid height ({platform.height}). Height must be positive.")

        if platform.width <= 0:
            warning(f"Level '{level.name}': Platform #{idx+1} has invalid width ({platform.width}). Width must be positive.")

        # Check for platforms outside typical screen bounds
        if platform.y < 0:
            warning(f"Level '{level.name}': Platform #{idx+1} has negative y position ({platform.y}). May not be visible.")

        if platform.y > 1000:
            warning(f"Level '{level.name}': Platform #{idx+1} y position ({platform.y}) is very high. May be below default screen.")


def pygame_sl_model_processor(model, metamodel):
    """
    Process and validate the pygame_sl model.

    Applies defaults, validates data, and provides helpful warnings.

    Args:
        model: The parsed game model
        metamodel: The textX metamodel
    """
    info(f"Processing game: '{model.name}'")

    # Validate and process items
    for item in model.items:
        if item.avatar.__class__.__name__ == 'Color':
            if check_color_existing('color', item.avatar.color):
                suggested = get_color_suggestion(item.avatar.color)
                warning(
                    f"Item '{item.name}' uses invalid color '{item.avatar.color}'. "
                    f"Using default '{defaults['default_texture_color']}' instead."
                )
                warning(f"Valid colors are: {', '.join(colors)}")
                warning(f"Did you mean '{suggested}'?")
                item.avatar.color = defaults['default_texture_color']

    # Validate levels
    if len(model.levels) == 0:
        warning("No levels defined! Game needs at least one level.")
    else:
        info(f"Found {len(model.levels)} level(s): {', '.join(lvl.name for lvl in model.levels)}")

    for level in model.levels:
        # Check for platforms
        if len(level.platforms) == 0:
            warning(f"Level '{level.name}' has no platforms. Player will fall!")

        # Validate platform properties
        validate_platforms(level)

        # Check for background color validity
        if level.background.__class__.__name__ == 'Color':
            if check_color_existing('color', level.background.color):
                suggested = get_color_suggestion(level.background.color)
                warning(
                    f"Level '{level.name}' background uses invalid color '{level.background.color}'. "
                    f"Using white instead."
                )
                warning(f"Valid colors are: {', '.join(colors)}")
                warning(f"Did you mean '{suggested}'?")
                level.background.color = 'white'

    # Validate player
    if model.player.height <= 0 or model.player.width <= 0:
        warning(f"Player dimensions must be positive. Got height={model.player.height}, width={model.player.width}")

    # Apply default settings
    set_default_settings(model)

    # Info about items
    if len(model.items) > 0:
        points = [item.name for item in model.items if item.__class__.__name__ == 'Point']
        boosts = [item.name for item in model.items if item.__class__.__name__ == 'Boost']

        if points:
            info(f"Point items: {', '.join(points)}")
        if boosts:
            info(f"Boost items: {', '.join(boosts)}")

    info("Model processing complete! ✓")
