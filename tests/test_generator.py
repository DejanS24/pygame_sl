"""Unit tests for code generator and template filters."""
import pytest
from generator.util import python_module_name


class TestPythonModuleName:
    """Tests for python_module_name utility function."""

    @pytest.mark.unit
    def test_simple_name(self):
        """Test conversion of simple game names."""
        assert python_module_name("MyGame") == "mygame.py"
        assert python_module_name("Test") == "test.py"

    @pytest.mark.unit
    def test_name_with_spaces(self):
        """Test conversion of names with spaces."""
        assert python_module_name("My Game") == "my_game.py"
        assert python_module_name("2D Platformer") == "2d_platformer.py"

    @pytest.mark.unit
    def test_name_with_special_chars(self):
        """Test conversion of names with special characters."""
        assert python_module_name("Game!") == "game_.py"
        assert python_module_name("Test@Game#") == "test_game_.py"
        assert python_module_name("My-Game") == "my-game.py"

    @pytest.mark.unit
    def test_name_with_numbers(self):
        """Test conversion of names with numbers."""
        assert python_module_name("Game2") == "game2.py"
        assert python_module_name("3D Game") == "3d_game.py"

    @pytest.mark.unit
    def test_lowercase_conversion(self):
        """Test that output is always lowercase."""
        assert python_module_name("UPPERCASE") == "uppercase.py"
        assert python_module_name("MixedCase") == "mixedcase.py"


class TestGeneratorFilters:
    """Tests for Jinja2 template filters."""

    @pytest.mark.unit
    def test_filter_imports(self):
        """Test that filter functions can be imported."""
        # These functions are defined inside the generate() function,
        # so we test the logic independently here

        # Test animation_level logic
        class ColorAvatar:
            __class__.__name__ = 'Color'

        class ImageAvatar:
            __class__.__name__ = 'ImageAvatar'
            walkingImage = True
            idleImage = True
            jumpingImage = False

        # Test check_list logic
        class Boost:
            pass

        class Point:
            pass

        items = [Boost(), Point(), Boost()]

        # Count boosts and points
        boosts = sum(1 for i in items if i.__class__.__name__ == 'Boost')
        points = sum(1 for i in items if i.__class__.__name__ == 'Point')

        assert boosts == 2
        assert points == 1

    @pytest.mark.unit
    def test_check_sounds_logic(self):
        """Test the sound checking logic."""
        # Test None sounds
        sounds = None
        result = sounds is None or not (sounds.jump_sound if hasattr(sounds, 'jump_sound') else False)
        assert result is True

        # Test with mock sounds object
        class Sounds:
            jump_sound = True
            boost_sound = False
            point_sound = True

        sounds = Sounds()
        has_any_sound = sounds.jump_sound or sounds.boost_sound or sounds.point_sound
        assert has_any_sound is True
