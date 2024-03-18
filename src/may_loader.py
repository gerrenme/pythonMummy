from files_uploader import FilesUploader

if __name__ == "__main__":
    uploader = FilesUploader()
    uploader.upload_file(filename="bot.log", dirr="Logs")
