import argparse
import logging
import pathlib
import subprocess


def map_files(source_folder: pathlib.Path, destination_folder: pathlib.Path) -> None:
    for item in source_folder.iterdir():
        relative_path = item.relative_to(destination_folder)
        link_name = item.name.replace("___", ".").replace("__", "/")
        destination_file = destination_folder / link_name
        destination_file.parent.mkdir(parents=True, exist_ok=True)
        if destination_file.exists():
            if destination_file.is_symlink() and destination_file.resolve() == item:
                logging.info("%s is already correctly set", link_name)
                continue
            logging.error("%s exists and is not a valid link")
        logging.info("Linking %s to %s", link_name, relative_path)
        destination_file.symlink_to(relative_path)


def get_parent_folder():
    completed = subprocess.run(
        ["git", "rev-parse", "--show-superproject-working-tree"],
        capture_output=True,
        check=True,
    )
    return completed.stdout.decode().strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="+")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s] %(message)s")
    settings_folder = pathlib.Path(__file__).parent.resolve() / "settings" 
    destination_folder = pathlib.Path(get_parent_folder())
    for folder in args.folders:
        source_folder = settings_folder / folder
        logging.info("Mapping files from %s to %s", source_folder, destination_folder)
        map_files(source_folder, destination_folder)


if __name__ == "__main__":
    main()
