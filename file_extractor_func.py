import zipfile


def extract_files(zip_name, desti_dir):
    with zipfile.ZipFile(zip_name, 'r') as archive:
        archive.extractall(desti_dir)


if __name__ == "__main__":
    extract_files(r"D:\compressed.zip",r"D:\New folder")