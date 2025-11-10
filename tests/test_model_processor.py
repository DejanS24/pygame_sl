"""Unit tests for model processor validation and defaults."""
import pytest
from lang.model_processor import (
    check_color_existing,
    set_default_settings,
    colors,
    defaults
)


class TestColorValidation:
    """Tests for color validation functionality."""

    @pytest.mark.unit
    def test_valid_color_returns_false(self):
        """Test that valid colors return False (no error)."""
        for color in colors:
            assert check_color_existing('player_color', color) is False

    @pytest.mark.unit
    def test_invalid_color_returns_true(self):
        """Test that invalid colors return True (error)."""
        assert check_color_existing('background_color', 'purple') is True
        assert check_color_existing('texture_color', 'orange') is True
        assert check_color_existing('default_color', 'pink') is True

    @pytest.mark.unit
    def test_non_color_key_returns_false(self):
        """Test that keys without 'color' return False."""
        assert check_color_existing('width', 'purple') is False
        assert check_color_existing('height', 100) is False


class TestDefaultSettings:
    """Tests for default settings application."""

    @pytest.mark.unit
    def test_defaults_exist(self):
        """Test that all expected defaults are defined."""
        expected_keys = [
            'screen_width', 'screen_height', 'font',
            'default_color', 'fps', 'movespeed', 'default_texture_color'
        ]
        for key in expected_keys:
            assert key in defaults

    @pytest.mark.unit
    def test_default_values(self):
        """Test that default values are reasonable."""
        assert defaults['screen_width'] == 800
        assert defaults['screen_height'] == 600
        assert defaults['font'] == 'arial'
        assert defaults['default_color'] == 'black'
        assert defaults['fps'] == 60
        assert defaults['movespeed'] == 6
        assert defaults['default_texture_color'] == 'green'


class TestValidColors:
    """Tests for the colors list."""

    @pytest.mark.unit
    def test_colors_list_content(self):
        """Test that expected colors are in the list."""
        expected_colors = ['black', 'blue', 'red', 'green', 'yellow', 'white']
        assert set(colors) == set(expected_colors)

    @pytest.mark.unit
    def test_colors_are_lowercase(self):
        """Test that all colors are lowercase."""
        for color in colors:
            assert color.islower()
