#!/usr/bin/env python
"""
Watch mode for pygame_sl development.

Watches .pg files for changes and automatically regenerates Python code.
Usage: python watch.py <path_to_pg_file>
"""

import sys
import os
import time
import subprocess
from pathlib import Path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("❌ watchdog package not installed")
    print("Install with: pip install watchdog")
    print("Or: pip install -e .[dev]")
    sys.exit(1)


class PygameSLWatcher(FileSystemEventHandler):
    """Watches .pg files and regenerates on changes."""

    def __init__(self, pg_file_path):
        self.pg_file_path = Path(pg_file_path).resolve()
        self.pg_file_name = self.pg_file_path.name
        self.last_generated = 0
        print(f"👀 Watching: {self.pg_file_path}")
        print(f"📂 Directory: {self.pg_file_path.parent}")
        print("Press Ctrl+C to stop\n")

        # Generate initially
        self.generate()

    def on_modified(self, event):
        """Called when a file is modified."""
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        # Only regenerate for the target .pg file
        if file_path.resolve() == self.pg_file_path:
            # Debounce - avoid multiple rapid regenerations
            current_time = time.time()
            if current_time - self.last_generated < 1.0:
                return

            self.last_generated = current_time
            self.generate()

    def generate(self):
        """Generate Python code from .pg file."""
        print(f"\n🔨 Generating from {self.pg_file_name}...")

        try:
            # Run textx generate command
            result = subprocess.run(
                ["textx", "generate", str(self.pg_file_path), "--target", "python"],
                capture_output=True,
                text=True,
                cwd=str(self.pg_file_path.parent)
            )

            if result.returncode == 0:
                print(f"✅ Generated successfully!")
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr)
            else:
                print(f"❌ Generation failed!")
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr)

        except FileNotFoundError:
            print("❌ 'textx' command not found")
            print("Make sure pygame_sl is installed: pip install -e .")
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python watch.py <path_to_pg_file>")
        print("\nExample:")
        print("  python watch.py examples/simple_platformer.pg")
        sys.exit(1)

    pg_file = sys.argv[1]

    if not os.path.exists(pg_file):
        print(f"❌ File not found: {pg_file}")
        sys.exit(1)

    if not pg_file.endswith('.pg'):
        print(f"⚠️  Warning: File doesn't have .pg extension: {pg_file}")

    pg_path = Path(pg_file)
    watch_dir = pg_path.parent.resolve()

    # Create watcher
    watcher = PygameSLWatcher(pg_path)

    # Set up observer
    observer = Observer()
    observer.schedule(watcher, str(watch_dir), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 Stopping watch mode...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
