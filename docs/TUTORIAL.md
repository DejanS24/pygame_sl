# pygame_sl Tutorial

Welcome to the pygame_sl tutorial! This guide will walk you through creating your first 2D platform game using the pygame_sl DSL.

## Table of Contents

1. [Introduction](#introduction)
2. [Your First Game](#your-first-game)
3. [Adding Images and Animations](#adding-images-and-animations)
4. [Working with Items](#working-with-items)
5. [Multiple Levels](#multiple-levels)
6. [Customizing Settings](#customizing-settings)
7. [Adding Sound](#adding-sound)
8. [Advanced Topics](#advanced-topics)

---

## Introduction

pygame_sl is a Domain-Specific Language that lets you create 2D platform games without writing complex pygame code. You describe your game in a simple `.pg` file, and pygame_sl generates the complete Python code for you.

### What You'll Need

- Python 3.8 or higher
- pygame_sl installed (`pip install -e .`)
- A text editor

---

## Your First Game

Let's create a simple platformer game with a player and two levels.

### Step 1: Create a .pg File

Create a file named `tutorial_game.pg`:

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
        position 0 550
        height 50
        width 800
    }
}
```

### Step 2: Generate the Code

Run the textX generator:

```bash
textx generate tutorial_game.pg --target python
```

This creates `my_first_platformer.py`.

### Step 3: Run Your Game

```bash
python my_first_platformer.py
```

**Controls:**
- Left Arrow: Move left
- Right Arrow: Move right
- Up Arrow: Jump

Your player starts on the left side. Move to the right edge to complete the level!

---

## Adding Images and Animations

Color-based graphics are great for prototyping, but images make your game look better!

### Using Images for the Player

First, prepare your image assets in an `assets/` folder:

```
assets/
└── players/
    ├── hero_default.png
    ├── hero_walk.png
    ├── hero_idle.png
    └── hero_jump.png
```

Update your `.pg` file:

```
game "Image-Based Game"

player {
    image "assets/players/hero_default.png"
    walk image "assets/players/hero_walk.png"
    idle image "assets/players/hero_idle.png"
    jump image "assets/players/hero_jump.png"
    height 100
    width 80
}

level Level1 {
    background image "assets/backgrounds/sky.jpg"

    platform {
        position 0 550
        texture image "assets/platforms/ground.png"
        height 50
        width 800
    }
}
```

**Note:** If you don't have images, you can use color-based graphics:
```
player {
    color blue
    height 75
    width 50
}
```

---

## Working with Items

Items make your game more interesting! pygame_sl supports two types:

### 1. Point Items (Collectibles)

```
point coins {
    color yellow
}

level Level1 {
    background color cyan

    platform {
        position 0 550
        height 50
        width 800
    }

    point coins {
        position 300 480
    }

    point coins {
        position 500 480
    }
}
```

### 2. Boost Items (Speed Power-ups)

```
boost speedBoost {
    color green
}

level Level1 {
    background color cyan

    platform {
        position 0 550
        height 50
        width 800
    }

    boost speedBoost {
        position 400 480
    }
}
```

When the player collects a speed boost, they move faster!

### Using Images for Items

```
point stars {
    image "assets/items/star.png"
}

boost lightning {
    image "assets/items/lightning.png"
}
```

---

## Multiple Levels

Create challenging games with multiple levels:

```
game "Multi-Level Adventure"

player {
    color blue
    height 75
    width 50
}

level Level1 {
    background color cyan

    platform {
        position 0 550
        height 50
        width 800
    }

    platform {
        position 300 400
        height 30
        width 150
    }
}

level Level2 {
    background color purple

    platform {
        position 0 550
        height 50
        width 800
    }

    platform {
        position 200 450
        height 30
        width 100
    }

    platform {
        position 400 350
        height 30
        width 100
    }
}

level Level3 {
    background color orange

    platform {
        position 0 550
        height 50
        width 800
    }

    platform {
        position 150 480
        height 30
        width 80
    }

    platform {
        position 350 400
        height 30
        width 80
    }

    platform {
        position 550 320
        height 30
        width 80
    }
}
```

The player progresses through levels by reaching the right edge of the screen.

---

## Customizing Settings

Customize your game's behavior and appearance:

```
settings {
    title "My Awesome Game"
    fps 60
    screen width 1024
    screen height 768
    movespeed 8
    default color black
    font "arial"
    default texture color green
}
```

**Available Settings:**

- `title`: Game window title
- `fps`: Frames per second (default: 60)
- `screen width`: Screen width in pixels (default: 800)
- `screen height`: Screen height in pixels (default: 600)
- `movespeed`: Player movement speed (default: 6)
- `default color`: Default text color (default: black)
- `font`: Font name for text (default: arial)
- `default texture color`: Default platform color if no texture (default: green)

---

## Adding Sound

Make your game more immersive with sound effects and music!

```
sound {
    game music "assets/sounds/background_music.mp3"
    jump sound "assets/sounds/jump.wav"
    boost sound "assets/sounds/powerup.wav"
    point sound "assets/sounds/coin.wav"
    end music "assets/sounds/victory.mp3"
}
```

**Sound Types:**

- `game music`: Plays continuously during gameplay
- `jump sound`: Plays when the player jumps
- `boost sound`: Plays when collecting a speed boost
- `point sound`: Plays when collecting a point item
- `end music`: Plays on the end screen after completing all levels

**Supported Formats:** MP3, WAV, OGG

---

## Advanced Topics

### Complex Level Design

Create interesting platforming challenges:

```
level Challenge {
    background image "assets/backgrounds/cave.jpg"

    // Ground
    platform {
        position 0 550
        height 50
        width 200
    }

    // Floating platforms
    platform {
        position 250 450
        height 30
        width 100
    }

    platform {
        position 400 380
        height 30
        width 100
    }

    platform {
        position 550 320
        height 30
        width 100
    }

    // High platform with reward
    platform {
        position 650 200
        height 30
        width 150
    }

    point treasure {
        image "assets/items/gem.png"
        position 700 130
    }
}
```

### Mixing Colors and Images

You can mix colors and images in the same game:

```
player {
    color blue
    height 75
    width 50
}

point stars {
    image "assets/items/star.png"
}

boost speedUp {
    color green
}

level Level1 {
    background image "assets/backgrounds/sky.jpg"

    platform {
        position 0 550
        color brown
        height 50
        width 800
    }

    platform {
        position 300 400
        texture image "assets/platforms/wood.png"
        height 30
        width 150
    }
}
```

### Tips for Better Games

1. **Start Simple**: Begin with color-based graphics, then add images later
2. **Test Frequently**: Generate and run your game after each change
3. **Platform Spacing**: Make sure platforms are close enough to jump between
4. **Visual Variety**: Use different background colors or images for each level
5. **Reward Exploration**: Place point items in challenging locations
6. **Difficulty Curve**: Make early levels easier, later levels harder

---

## Complete Example

Here's a complete game putting it all together:

```
game "Adventure Quest"

"A thrilling platformer adventure!"

player {
    image "assets/players/knight_default.png"
    walk image "assets/players/knight_walk.png"
    idle image "assets/players/knight_idle.png"
    jump image "assets/players/knight_jump.png"
    height 90
    width 70
}

point gems {
    image "assets/items/gem.png"
}

boost potion {
    image "assets/items/potion.png"
}

level Forest {
    background image "assets/backgrounds/forest.jpg"

    platform {
        position 0 550
        texture image "assets/platforms/grass.png"
        height 50
        width 300
    }

    platform {
        position 400 550
        texture image "assets/platforms/grass.png"
        height 50
        width 400
    }

    platform {
        position 350 420
        texture image "assets/platforms/wood.png"
        height 30
        width 120
    }

    point gems {
        position 400 350
    }
}

level Castle {
    background image "assets/backgrounds/castle.jpg"

    platform {
        position 0 550
        texture image "assets/platforms/stone.png"
        height 50
        width 800
    }

    platform {
        position 200 450
        texture image "assets/platforms/stone.png"
        height 30
        width 100
    }

    platform {
        position 450 350
        texture image "assets/platforms/stone.png"
        height 30
        width 100
    }

    boost potion {
        position 500 280
    }

    point gems {
        position 200 380
    }

    point gems {
        position 500 280
    }
}

sound {
    game music "assets/sounds/adventure_theme.mp3"
    jump sound "assets/sounds/jump.wav"
    point sound "assets/sounds/gem_collect.wav"
    boost sound "assets/sounds/potion.wav"
    end music "assets/sounds/victory.mp3"
}

settings {
    title "Adventure Quest"
    fps 60
    screen width 800
    screen height 600
    movespeed 7
}
```

---

## Next Steps

- Check out the [Grammar Reference](GRAMMAR_REFERENCE.md) for complete syntax details
- View more [Examples](EXAMPLES.md) for inspiration
- Learn how to [contribute](CONTRIBUTING.md) to pygame_sl

Happy game making! 🎮
