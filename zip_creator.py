import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as arch:
        for filepath in filepaths:
            print(filepath)
            filepath = pathlib.Path(filepath)
            print(filepath)
            arch.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=[r"D:/Python Sample Programs/a.txt", r"D:/Python Sample Programs/b.txt"],
                 dest_dir="D:/")