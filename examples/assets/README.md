# Game Assets Directory

This directory is for storing game assets (images, sounds, etc.) used in the example `.pg` files.

## Recommended Structure

```
assets/
├── backgrounds/          # Background images
├── players/             # Player character sprites
│   ├── walk/           # Walking animations
│   ├── idle/           # Idle animations
│   └── jump/           # Jumping animations
├── platforms/           # Platform textures
├── items/              # Collectible item images
└── sounds/             # Sound effects and music
```

## Image Specifications

### Player Sprites
- **Format**: PNG (with transparency recommended)
- **Recommended size**: 50-100px width, 75-150px height
- **Animation frames**: Place in respective subdirectories

### Backgrounds
- **Format**: PNG or JPG
- **Size**: Should match your screen dimensions (default: 800x600)

### Platform Textures
- **Format**: PNG (with transparency recommended)
- **Size**: Flexible, will be scaled to platform dimensions

### Items
- **Format**: PNG (with transparency recommended)
- **Recommended size**: 30-50px square

## Using Assets in Your .pg Files

Use relative paths from your `.pg` file location:

```
player {
    image "assets/players/walk/pikachu.png"
    walkingImage "assets/players/walk/pikachu_walk.png"
    idleImage "assets/players/idle/pikachu_idle.png"
    jumpingImage "assets/players/jump/pikachu_jump.png"
    height 75
    width 50
}

level Level1 {
    background image "assets/backgrounds/grass_field.png"
    platform {
        position 300 420
        texture "assets/platforms/wood.png"
        height 50
        width 80
    }
}
```

## Note

The example files may reference assets that are not included in this repository.
You should replace these paths with your own asset files or use color-based graphics instead.
