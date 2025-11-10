"""Integration tests for end-to-end DSL processing."""
import pytest
import os
import tempfile
import ast
from pathlib import Path
from textx import metamodel_from_file
from lang.model_processor import pygame_sl_model_processor


class TestEndToEnd:
    """Integration tests for full workflow."""

    @pytest.fixture
    def test_pg_file(self):
        """Fixture that provides path to test .pg file."""
        return Path(__file__).parent / 'fixtures' / 'test_game.pg'

    @pytest.fixture
    def metamodel(self):
        """Fixture that creates the pygame_sl metamodel."""
        grammar_path = Path(__file__).parent.parent / 'lang' / 'pygame_sl.tx'
        mm = metamodel_from_file(str(grammar_path))
        mm.register_model_processor(pygame_sl_model_processor)
        return mm

    @pytest.mark.integration
    def test_parse_valid_pg_file(self, metamodel, test_pg_file):
        """Test parsing a valid .pg file."""
        model = metamodel.model_from_file(str(test_pg_file))

        # Verify basic model structure
        assert model is not None
        assert model.name == "Test Game"
        assert model.player is not None
        assert len(model.levels) == 2

    @pytest.mark.integration
    def test_model_processor_applies_defaults(self, metamodel, test_pg_file):
        """Test that model processor applies default settings."""
        model = metamodel.model_from_file(str(test_pg_file))

        # Check that defaults were applied
        assert hasattr(model, 'settings')
        assert model.settings['screen_width'] == 800
        assert model.settings['screen_height'] == 600
        assert model.settings['fps'] == 60

    @pytest.mark.integration
    def test_generate_valid_python_code(self, metamodel, test_pg_file):
        """Test that generated code is syntactically valid Python."""
        from generator import generate
        import jinja2
        from generator.util import python_module_name

        model = metamodel.model_from_file(str(test_pg_file))

        # Generate code to a temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:
            # Manually generate using the template
            template_path = Path(__file__).parent.parent / 'generator'
            jinja_env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(str(template_path))
            )
            template = jinja_env.get_template('pygame.template')
            generated_code = template.render(m=model)

            # Write to temporary file
            output_file = Path(tmpdir) / python_module_name(model.name)
            output_file.write_text(generated_code)

            # Try to parse the generated Python code
            try:
                ast.parse(generated_code)
                syntax_valid = True
            except SyntaxError:
                syntax_valid = False

            assert syntax_valid, "Generated code should be syntactically valid Python"
            assert output_file.exists()

    @pytest.mark.integration
    def test_generated_code_contains_game_elements(self, metamodel, test_pg_file):
        """Test that generated code contains expected game elements."""
        import jinja2
        from pathlib import Path

        model = metamodel.model_from_file(str(test_pg_file))

        # Generate code
        template_path = Path(__file__).parent.parent / 'generator'
        jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(template_path))
        )
        template = jinja_env.get_template('pygame.template')
        generated_code = template.render(m=model)

        # Check for essential game elements
        assert 'class Player' in generated_code
        assert 'class Platform' in generated_code
        assert 'class Level' in generated_code
        assert 'class Game' in generated_code
        assert 'pygame.init()' in generated_code
        assert model.name in generated_code or 'Test Game' in generated_code
