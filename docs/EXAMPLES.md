# pygame_sl Examples

This document provides annotated examples showing different features and use cases of pygame_sl.

## Table of Contents

1. [Minimal Example](#minimal-example)
2. [Color-Based Game](#color-based-game)
3. [Image-Based Game](#image-based-game)
4. [Multi-Level Game](#multi-level-game)
5. [Game with Items](#game-with-items)
6. [Complete Game with All Features](#complete-game-with-all-features)
7. [Platform Patterns](#platform-patterns)

---

## Minimal Example

The absolute minimum needed for a working game.

```
game "Minimal Game"

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

**What it creates:**
- A blue player rectangle
- One level with yellow background
- One platform at the bottom of the screen
- Player wins by moving to the right edge

---

## Color-Based Game

A complete game using only colors (no image assets needed).

```
game "Color Platformer"

player {
    color blue
    height 75
    width 50
}

point stars {
    color yellow
}

boost speedUp {
    color green
}

level Beginner {
    background color cyan

    // Ground
    platform {
        position 0 550
        height 50
        width 800
    }

    // Floating platform
    platform {
        position 300 400
        height 30
        width 150
    }

    // Collectibles
    point stars {
        position 350 330
    }

    boost speedUp {
        position 650 480
    }
}

level Advanced {
    background color purple

    platform {
        position 0 550
        height 50
        width 300
    }

    platform {
        position 350 550
        height 50
        width 450
    }

    platform {
        position 200 420
        height 30
        width 100
    }

    platform {
        position 450 350
        height 30
        width 120
    }

    point stars {
        position 250 350
    }

    point stars {
        position 500 280
    }
}

settings {
    title "Color Platformer"
    fps 60
    movespeed 7
}
```

**Features demonstrated:**
- Color-based graphics
- Multiple levels
- Point and boost items
- Custom settings

---

## Image-Based Game

Using image assets for a polished look.

```
game "Adventure Game"

player {
    image "assets/players/hero_default.png"
    walk image "assets/players/hero_walk.png"
    idle image "assets/players/hero_idle.png"
    jump image "assets/players/hero_jump.png"
    height 100
    width 80
}

point gems {
    image "assets/items/gem.png"
}

level Forest {
    background image "assets/backgrounds/forest.jpg"

    platform {
        position 0 550
        texture image "assets/platforms/grass.png"
        height 50
        width 400
    }

    platform {
        position 500 550
        texture image "assets/platforms/grass.png"
        height 50
        width 300
    }

    platform {
        position 300 400
        texture image "assets/platforms/wood.png"
        height 30
        width 150
    }

    point gems {
        position 350 330
    }
}

settings {
    title "Adventure Game"
    screen width 800
    screen height 600
}
```

**Asset structure needed:**
```
assets/
├── players/
│   ├── hero_default.png
│   ├── hero_walk.png
│   ├── hero_idle.png
│   └── hero_jump.png
├── items/
│   └── gem.png
├── backgrounds/
│   └── forest.jpg
└── platforms/
    ├── grass.png
    └── wood.png
```

---

## Multi-Level Game

Progressive difficulty across multiple levels.

```
game "Sky Climber"

player {
    color blue
    height 75
    width 50
}

level Ground {
    background color cyan

    // Easy starting level
    platform {
        position 0 550
        height 50
        width 800
    }

    platform {
        position 350 450
        height 30
        width 200
    }
}

level Clouds {
    background color lightblue

    // Medium difficulty
    platform {
        position 0 550
        height 50
        width 250
    }

    platform {
        position 300 550
        height 50
        width 500
    }

    platform {
        position 200 450
        height 30
        width 100
    }

    platform {
        position 400 380
        height 30
        width 100
    }

    platform {
        position 600 320
        height 30
        width 100
    }
}

level Space {
    background color black

    // Challenging level
    platform {
        position 0 550
        height 50
        width 150
    }

    platform {
        position 200 480
        height 30
        width 80
    }

    platform {
        position 350 420
        height 30
        width 80
    }

    platform {
        position 500 360
        height 30
        width 80
    }

    platform {
        position 650 300
        height 30
        width 150
    }
}

settings {
    title "Sky Climber"
    fps 60
    movespeed 6
}
```

**Design notes:**
- Level 1: Wide platforms, easy jumps
- Level 2: Some gaps, moderate difficulty
- Level 3: Precise jumps required

---

## Game with Items

Demonstrating all item types and placements.

```
game "Treasure Hunt"

player {
    color blue
    height 75
    width 50
}

// Define multiple point items
point coins {
    color yellow
}

point gems {
    color red
}

// Define boost items
boost speedBoost {
    color green
}

level TreasureRoom {
    background color purple

    // Main ground
    platform {
        position 0 550
        height 50
        width 800
    }

    // Low platforms
    platform {
        position 150 480
        height 30
        width 100
    }

    platform {
        position 550 480
        height 30
        width 100
    }

    // High platform with valuable gem
    platform {
        position 350 320
        height 30
        width 100
    }

    // Place items strategically
    point coins {
        position 200 410  // On low platform
    }

    point coins {
        position 600 410  // On another low platform
    }

    point gems {
        position 380 250  // On high platform (more valuable)
    }

    boost speedBoost {
        position 100 480  // Near start
    }
}

settings {
    title "Treasure Hunt"
    fps 60
}
```

**Item placement strategy:**
- Common items (coins) in easy-to-reach places
- Rare items (gems) in challenging locations
- Boosts early in level to help players

---

## Complete Game with All Features

A full-featured game using every pygame_sl feature.

```
game "Epic Adventure"
"Journey through mysterious lands and collect treasures!"

player {
    image "assets/players/knight_default.png"
    walk image "assets/players/knight_walk.png"
    idle image "assets/players/knight_idle.png"
    jump image "assets/players/knight_jump.png"
    height 100
    width 80
}

point coins {
    image "assets/items/coin.png"
}

point diamonds {
    image "assets/items/diamond.png"
}

boost potion {
    image "assets/items/speed_potion.png"
}

level GreenValley {
    background image "assets/backgrounds/valley.jpg"

    // Continuous ground
    platform {
        position 0 550
        texture image "assets/platforms/grass.png"
        height 50
        width 800
    }

    // Floating platforms
    platform {
        position 250 450
        texture image "assets/platforms/wood.png"
        height 30
        width 120
    }

    platform {
        position 450 380
        texture image "assets/platforms/wood.png"
        height 30
        width 120
    }

    // Items
    point coins {
        position 300 380
    }

    point coins {
        position 500 310
    }

    boost potion {
        position 650 480
    }
}

level DarkCastle {
    background image "assets/backgrounds/castle.jpg"

    platform {
        position 0 550
        texture image "assets/platforms/stone.png"
        height 50
        width 350
    }

    platform {
        position 450 550
        texture image "assets/platforms/stone.png"
        height 50
        width 350
    }

    platform {
        position 200 450
        texture image "assets/platforms/stone.png"
        height 30
        width 100
    }

    platform {
        position 400 380
        texture image "assets/platforms/stone.png"
        height 30
        width 100
    }

    platform {
        position 600 320
        texture image "assets/platforms/stone.png"
        height 30
        width 100
    }

    point coins {
        position 230 380
    }

    point diamonds {
        position 430 310
    }

    point diamonds {
        position 630 250
    }
}

level SkyRealm {
    background image "assets/backgrounds/sky.jpg"

    platform {
        position 0 550
        texture image "assets/platforms/cloud.png"
        height 50
        width 200
    }

    platform {
        position 250 480
        texture image "assets/platforms/cloud.png"
        height 30
        width 100
    }

    platform {
        position 400 420
        texture image "assets/platforms/cloud.png"
        height 30
        width 100
    }

    platform {
        position 550 360
        texture image "assets/platforms/cloud.png"
        height 30
        width 100
    }

    platform {
        position 650 280
        texture image "assets/platforms/cloud.png"
        height 40
        width 150
    }

    boost potion {
        position 50 480
    }

    point diamonds {
        position 300 410
    }

    point diamonds {
        position 450 350
    }

    point diamonds {
        position 700 210
    }
}

sound {
    game music "assets/sounds/adventure_theme.mp3"
    jump sound "assets/sounds/jump.wav"
    point sound "assets/sounds/coin.wav"
    boost sound "assets/sounds/powerup.wav"
    end music "assets/sounds/victory.mp3"
}

settings {
    title "Epic Adventure"
    fps 60
    screen width 800
    screen height 600
    movespeed 7
    default color white
    font name "arial"
}
```

**Features demonstrated:**
- All avatar animation types
- Multiple item types (coins, diamonds, potions)
- Three thematic levels
- Complete sound system
- Full settings customization

---

## Platform Patterns

Common platform arrangements for different challenges.

### Staircase Pattern

```
level Stairs {
    background color cyan

    platform { position 0 550 height 50 width 150 }
    platform { position 200 480 height 40 width 120 }
    platform { position 370 410 height 40 width 120 }
    platform { position 540 340 height 40 width 120 }
    platform { position 700 270 height 50 width 100 }
}
```

### Gap Jumping

```
level Gaps {
    background color blue

    platform { position 0 550 height 50 width 200 }
    platform { position 300 550 height 50 width 150 }
    platform { position 550 550 height 50 width 250 }
}
```

### High-Low Pattern

```
level HighLow {
    background color purple

    platform { position 0 550 height 50 width 180 }
    platform { position 220 350 height 30 width 100 }
    platform { position 360 550 height 50 width 180 }
    platform { position 580 350 height 30 width 100 }
}
```

### Pyramid

```
level Pyramid {
    background color yellow

    // Base
    platform { position 300 550 height 40 width 200 }
    // Middle
    platform { position 350 480 height 35 width 100 }
    // Top
    platform { position 400 420 height 30 width 50 }
}
```

---

## Tips for Creating Engaging Games

1. **Level progression**: Start easy, gradually increase difficulty
2. **Visual variety**: Use different backgrounds for each level
3. **Strategic item placement**: Reward exploration and skill
4. **Platform spacing**: Ensure jumps are possible but challenging
5. **Test frequently**: Play your game after each change
6. **Use animations**: Animations make games feel more alive
7. **Add sound**: Audio significantly enhances game feel

---

## More Examples

Check the `examples/` directory in the repository for additional .pg files:

- `game1.pg` - Simple color-based example
- `pikachu_game.pg` - Image-based Pokemon-themed game

---

For detailed syntax information, see the [Grammar Reference](GRAMMAR_REFERENCE.md).

For a step-by-step guide, see the [Tutorial](TUTORIAL.md).
