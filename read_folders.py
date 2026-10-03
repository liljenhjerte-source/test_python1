from pathlib import Path


def main() -> None:
	parent_folder = Path(__file__).resolve().parent.parent.parent.parent
	folder_names = sorted(
		path.name for path in parent_folder.iterdir() if path.is_dir()
	)

	for folder_name in folder_names:
		print(folder_name)


if __name__ == "__main__":
	main()
