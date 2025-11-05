from pathlib import Path
import sys

from gui.directory_picker import select_directory
from core.config_loader import load_config
from core.pipeline import build_pipelines
from core.processor import process_directory
import augmentations  # noqa: F401  # make sure registry is populated


def main():
    # 1. Select input directory via Tkinter
    input_dir_str = select_directory()
    if not input_dir_str:
        print("No directory selected. Exiting.")
        sys.exit(0)

    input_dir = Path(input_dir_str)
    if not input_dir.is_dir():
        print(f"Selected path is not a directory: {input_dir}")
        sys.exit(1)

    # 2. Load config file at startup
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "configs" / "config.txt"
    if not config_path.is_file():
        print(f"Config file not found: {config_path}")
        sys.exit(1)

    print(f"Using config file: {config_path}")
    pipeline_configs = load_config(config_path)
    if not pipeline_configs:
        print("No valid pipelines found in config file.")
        sys.exit(1)

    # 3. Build augmentation pipelines
    pipelines = build_pipelines(pipeline_configs)

    # 4. Run processing
    process_directory(input_dir, pipeline_configs, pipelines)


if __name__ == "__main__":
    main()
