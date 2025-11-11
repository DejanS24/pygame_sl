# from pygame_sl.generator import generator
import sys
import os

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


def validate_asset_path(path, context, model_file_path=None):
    """
    Validate that an asset file exists.

    Args:
        path (str): The asset file path
        context (str): Context string for error message (e.g., "Player avatar")
        model_file_path (str): Path to the .pg file for relative path resolution

    Returns:
        bool: True if file exists or validation should be skipped, False otherwise
    """
    if not path:
        return True

    # Resolve relative paths based on .pg file location
    if model_file_path and not os.path.isabs(path):
        base_dir = os.path.dirname(model_file_path)
        full_path = os.path.join(base_dir, path)
    else:
        full_path = path

    if not os.path.exists(full_path):
        warning(f"{context}: Asset file not found: '{path}'")
        if not os.path.isabs(path):
            warning(f"  Looked in: {os.path.abspath(full_path)}")
        warning(f"  Make sure the file exists before running the generated game.")
        return False

    return True


def validate_image_avatar(avatar, context, model_file_path=None):
    """
    Validate image-based avatar assets.

    Args:
        avatar: The avatar object to validate
        context (str): Context for error messages
        model_file_path (str): Path to the .pg file
    """
    if avatar.__class__.__name__ == 'ImageAvatar':
        # Check default image
        if hasattr(avatar, 'default') and avatar.default:
            validate_asset_path(avatar.default.path, f"{context} (default image)", model_file_path)

        # Check animation images
        if hasattr(avatar, 'walkingImage') and avatar.walkingImage:
            validate_asset_path(avatar.walkingImage.path, f"{context} (walk animation)", model_file_path)

        if hasattr(avatar, 'idleImage') and avatar.idleImage:
            validate_asset_path(avatar.idleImage.path, f"{context} (idle animation)", model_file_path)

        if hasattr(avatar, 'jumpingImage') and avatar.jumpingImage:
            validate_asset_path(avatar.jumpingImage.path, f"{context} (jump animation)", model_file_path)


def validate_image_or_color(obj, context, model_file_path=None):
    """
    Validate ImageOrColor objects.

    Args:
        obj: The ImageOrColor object
        context (str): Context for error messages
        model_file_path (str): Path to the .pg file
    """
    if obj.__class__.__name__ == 'Image':
        validate_asset_path(obj.path, context, model_file_path)


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


def validate_platforms(level, model_file_path=None):
    """
    Validate platform positions and dimensions.

    Args:
        level: The level object to validate
        model_file_path (str): Path to the .pg file
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

        # Validate platform texture if present
        if hasattr(platform, 'texture') and platform.texture:
            validate_image_or_color(platform.texture, f"Level '{level.name}' Platform #{idx+1} texture", model_file_path)


def validate_sounds(sounds, model_file_path=None):
    """
    Validate sound file paths.

    Args:
        sounds: The sounds object
        model_file_path (str): Path to the .pg file
    """
    if not sounds:
        return

    sound_fields = [
        ('game_music', 'Background music'),
        ('jump_sound', 'Jump sound'),
        ('boost_sound', 'Boost sound'),
        ('point_sound', 'Point sound'),
        ('end_music', 'End music'),
    ]

    for field, context in sound_fields:
        if hasattr(sounds, field):
            path = getattr(sounds, field)
            if path:
                validate_asset_path(path, context, model_file_path)


def pygame_sl_model_processor(model, metamodel):
    """
    Process and validate the pygame_sl model.

    Applies defaults, validates data, and provides helpful warnings.

    Args:
        model: The parsed game model
        metamodel: The textX metamodel
    """
    info(f"Processing game: '{model.name}'")

    # Get model file path for relative asset resolution
    model_file_path = getattr(model, '_tx_filename', None)

    # Validate player avatar
    if hasattr(model.player, 'avatar'):
        validate_image_avatar(model.player.avatar, "Player", model_file_path)

    # Validate and process items
    for item in model.items:
        # Validate item avatar/image
        if hasattr(item, 'avatar'):
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
            else:
                validate_image_or_color(item.avatar, f"Item '{item.name}'", model_file_path)

    # Validate levels
    if len(model.levels) == 0:
        warning("No levels defined! Game needs at least one level.")
    else:
        info(f"Found {len(model.levels)} level(s): {', '.join(lvl.name for lvl in model.levels)}")

    for level in model.levels:
        # Check for platforms
        if len(level.platforms) == 0:
            warning(f"Level '{level.name}' has no platforms. Player will fall!")

        # Validate level background
        if hasattr(level, 'background'):
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
            else:
                validate_image_or_color(level.background, f"Level '{level.name}' background", model_file_path)

        # Validate platform properties
        validate_platforms(level, model_file_path)

    # Validate player dimensions
    if model.player.height <= 0 or model.player.width <= 0:
        warning(f"Player dimensions must be positive. Got height={model.player.height}, width={model.player.width}")

    # Validate sounds
    if hasattr(model, 'sounds'):
        validate_sounds(model.sounds, model_file_path)

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
