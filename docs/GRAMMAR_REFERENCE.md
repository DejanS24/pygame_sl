# pygame_sl Grammar Reference

This document provides a complete reference for the pygame_sl Domain-Specific Language syntax.

## Table of Contents

1. [Overview](#overview)
2. [Game Declaration](#game-declaration)
3. [Player Configuration](#player-configuration)
4. [Items](#items)
5. [Levels](#levels)
6. [Sounds](#sounds)
7. [Settings](#settings)
8. [Data Types](#data-types)
9. [Complete Grammar](#complete-grammar)

---

## Overview

A pygame_sl file (`.pg`) describes a complete 2D platform game. The general structure is:

```
game "Game Name"
"Optional description"

player { ... }

// Item definitions (optional)
point itemName { ... }
boost itemName { ... }

// Level definitions (at least one required)
level LevelName { ... }

// Sound configuration (optional)
sound { ... }

// Game settings (optional)
settings { ... }
```

---

## Game Declaration

Every game starts with a `game` declaration.

### Syntax

```
game "Game Name"
"Optional description"
```

### Fields

- **name** (required): String - The name of your game
- **description** (optional): String - A description of your game

### Example

```
game "Super Platformer"
"A thrilling adventure through challenging levels"
```

---

## Player Configuration

Defines the player character's appearance and size.

### Syntax

```
player {
    // Avatar (required) - either color-based or image-based
    (color <color_name> | image <path>)

    // Optional animation images
    [walk image <path>]
    [idle image <path>]
    [jump image <path>]

    // Size (required)
    height <number>
    width <number>
}
```

### Fields

**Avatar** (required, choose one):
- `color <color_name>`: Use a solid color
- `image <path>`: Use an image file

**Animation Images** (optional, only with image avatar):
- `walk image <path>`: Walking animation sprite
- `idle image <path>`: Idle/standing animation sprite
- `jump image <path>`: Jumping animation sprite

**Dimensions** (required):
- `height <number>`: Player height in pixels
- `width <number>`: Player width in pixels

### Valid Colors

- `black`
- `blue`
- `red`
- `green`
- `yellow`
- `white`

### Examples

**Color-based player:**
```
player {
    color blue
    height 75
    width 50
}
```

**Image-based player with animations:**
```
player {
    image "assets/players/hero_default.png"
    walk image "assets/players/hero_walk.png"
    idle image "assets/players/hero_idle.png"
    jump image "assets/players/hero_jump.png"
    height 100
    width 80
}
```

---

## Items

Items are collectibles that the player can pick up. There are two types: **points** and **boosts**.

### Point Items

Collectibles that increment the player's score.

#### Syntax

```
point <itemName> {
    (color <color_name> | image <path>)
}
```

#### Example

```
point coins {
    color yellow
}

point gems {
    image "assets/items/gem.png"
}
```

### Boost Items

Power-ups that increase the player's movement speed.

#### Syntax

```
boost <itemName> {
    (color <color_name> | image <path>)
}
```

#### Example

```
boost speedBoost {
    color green
}

boost lightning {
    image "assets/items/lightning.png"
}
```

---

## Levels

Levels define the game environment, including background, platforms, and item placements.

### Syntax

```
level <LevelName> {
    background (color <color_name> | image <path>)

    // Platforms (required, at least one)
    platform {
        position <x> <y>
        [texture image <path>]
        height <number>
        width <number>
    }

    // Item instances (optional)
    point <itemName> {
        position <x> <y>
    }

    boost <itemName> {
        position <x> <y>
    }
}
```

### Fields

**Background** (required):
- `background color <color_name>`: Solid color background
- `background image <path>`: Image background

**Platforms** (required, at least one):
- `position <x> <y>`: Top-left corner coordinates
- `texture image <path>` (optional): Platform texture image
- `height <number>`: Platform height in pixels
- `width <number>`: Platform width in pixels

**Item Instances** (optional):
- References items defined earlier
- `position <x> <y>`: Item location

### Example

```
level Forest {
    background image "assets/backgrounds/forest.jpg"

    // Ground platform
    platform {
        position 0 550
        texture image "assets/platforms/grass.png"
        height 50
        width 800
    }

    // Floating platform
    platform {
        position 300 400
        height 30
        width 150
    }

    // Place items
    point coins {
        position 350 330
    }

    boost speedBoost {
        position 600 480
    }
}
```

### Coordinate System

- Origin (0, 0) is at the top-left corner
- X increases to the right
- Y increases downward
- Default screen size: 800x600 pixels

---

## Sounds

Add audio to your game with background music and sound effects.

### Syntax

```
sound {
    [game music <path>]
    [jump sound <path>]
    [boost sound <path>]
    [point sound <path>]
    [end music <path>]
}
```

### Fields

All fields are optional:

- `game music <path>`: Background music during gameplay (loops)
- `jump sound <path>`: Sound effect when player jumps
- `boost sound <path>`: Sound effect when collecting a boost
- `point sound <path>`: Sound effect when collecting a point
- `end music <path>`: Music played on the end screen

### Supported Audio Formats

- MP3
- WAV
- OGG

### Example

```
sound {
    game music "assets/sounds/background_music.mp3"
    jump sound "assets/sounds/jump.wav"
    boost sound "assets/sounds/powerup.wav"
    point sound "assets/sounds/coin.wav"
    end music "assets/sounds/victory.mp3"
}
```

---

## Settings

Customize game behavior and appearance.

### Syntax

```
settings {
    [title <string>]
    [fps <number>]
    [default color <string>]
    [default texture color <string>]
    [font name <string>]
    [screen width <number>]
    [screen height <number>]
    [movespeed <number>]
}
```

### Fields

All fields are optional with default values:

- `title <string>`: Game window title (default: game name)
- `fps <number>`: Frames per second (default: 60)
- `default color <string>`: Default text color (default: "black")
- `default texture color <string>`: Default platform color when no texture (default: "green")
- `font name <string>`: Font for text rendering (default: "arial")
- `screen width <number>`: Screen width in pixels (default: 800)
- `screen height <number>`: Screen height in pixels (default: 600)
- `movespeed <number>`: Player movement speed (default: 6)

### Example

```
settings {
    title "My Awesome Game"
    fps 60
    screen width 1024
    screen height 768
    movespeed 8
    default color black
    font name "courier"
    default texture color green
}
```

---

## Data Types

### STRING

Quoted text for names, paths, and descriptions.

```
"my_game.png"
"Super Platformer"
'arial'
```

### INT

Integer numbers for positions, dimensions, and numeric settings.

```
75
800
60
```

### ID

Identifiers for level and item names (unquoted).

```
Level1
speedBoost
coins
myLevel
```

### WORD

Color names and other keyword values.

```
blue
red
green
```

---

## Complete Grammar

For reference, here's the complete grammar in TextX notation:

```
Game:
  "game" name=STRING
  (description=STRING)?
  player=Player
  items*=Item
  levels+=Level
  (sounds=Sound)?
  (settings=Setting)?
;

Player:
  "player" "{"
    avatar=Avatar
    "height" height=INT
    "width" width=INT
  "}"
;

Avatar:
  ( ImageAvatar | Color)
;

ImageAvatar:
  default=Image
  ("walk" walkingImage=Image)?
  ("idle" idleImage=Image)?
  ("jump" jumpingImage=Image)?
;

Image:
  "image" path=STRING
;

Color:
  "color" color=WORD
;

Item:
  Boost | Point
;

Boost:
  "boost" name=ID "{"
    avatar=ImageOrColor
  "}"
;

Point:
  "point" name=ID "{"
    avatar=ImageOrColor
  "}"
;

Level:
  "level" name=ID "{"
    "background" background=ImageOrColor
    platforms*=Platform
    items*=ItemReference
  "}"
;

Platform:
  "platform" "{"
    "position" x=INT y=INT
    ("texture" texture=Image)?
    "height" height=INT
    "width" width=INT
  "}"
;

ItemReference:
  BoostInstance | PointInstance
;

BoostInstance:
  "boost" type=[Boost] "{"
    "position" x=INT y=INT
  "}"
;

PointInstance:
  "point" type=[Point] "{"
    "position" x=INT y=INT
  "}"
;

Sound:
  "sounds" "{"
    ("game music" game_music=STRING |
     "jump sound" jump_sound=STRING |
     "boost sound" boost_sound=STRING |
     "point sound" point_sound=STRING |
     "end music" end_music=STRING
    )+
  "}"
;

Setting:
  "settings" "{"
    ("title" title=STRING |
     "fps" fps=INT |
     "default color" default_color=STRING |
     "default texture color" default_texture_color=STRING |
     "font name" font=STRING |
     "screen width" screen_width=INT |
     "screen height" screen_height=INT |
     "movespeed" movespeed=INT
    )+
  "}"
;

ImageOrColor:
  Image | Color
;
```

---

## Best Practices

1. **Use descriptive names**: Choose clear names for items and levels
2. **Organize logically**: Define items before using them in levels
3. **Comment your code**: Use `//` for single-line comments
4. **Test incrementally**: Generate and test after adding each level
5. **Consistent spacing**: Use indentation for readability
6. **Asset paths**: Use relative paths for portability

---

## Common Patterns

### Minimal Game

```
game "Minimal"

player {
    color blue
    height 75
    width 50
}

level Level1 {
    background color yellow
    platform {
        position 0 550
        height 50
        width 800
    }
}
```

### Full-Featured Game

```
game "Complete Game"
"A game with all features"

player {
    image "assets/player.png"
    walk image "assets/player_walk.png"
    height 100
    width 80
}

point coins {
    color yellow
}

boost speed {
    color green
}

level Level1 {
    background image "assets/bg.jpg"

    platform {
        position 0 550
        texture image "assets/ground.png"
        height 50
        width 800
    }

    point coins {
        position 400 480
    }
}

sound {
    game music "assets/music.mp3"
    jump sound "assets/jump.wav"
}

settings {
    title "My Game"
    fps 60
    screen width 800
    screen height 600
}
```

---

For more examples, see [EXAMPLES.md](EXAMPLES.md) and the [examples/](../examples/) directory.
