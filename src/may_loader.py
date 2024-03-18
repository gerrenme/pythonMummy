from files_uploader import FilesUploader

if __name__ == "__main__":
    uploader = FilesUploader()
    uploader.download_file(filename="logs_from2024-03-18.log", dirr="Logs")
