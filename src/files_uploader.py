import yadisk
from config import yadisk_token
from logger import Logger
import datetime
import os
import shutil


class FilesUploader:
    def __init__(self):
        self.yd_connect: yadisk.YaDisk = yadisk.YaDisk(token=yadisk_token)
        self.logger: Logger = Logger()

    def remove_file(self, filename: str) -> bool:
        try:
            self.yd_connect.remove(filename, permamently=True)
            return True

        except Exception as _ex:
            self.logger.log_rm_error(filename=filename, exception=_ex)

    def upload_file(self, dirr: str, filename: str) -> bool:
        try:
            self.yd_connect.upload(filename, f"{dirr}/{filename}")
            return True

        except Exception as _ex:
            self.logger.log_upload_error(dirr=dirr, filename=filename, exception=_ex)

    def download_file(self, filename: str, dirr: str) -> bool:
        try:
            self.yd_connect.upload(f"{dirr}/{filename}", filename)
            return True

        except Exception as _ex:
            self.logger.log_download_error(dirr=dirr, filename=filename, exception=_ex)

    def upload_logs(self, filename: str = "bot.log") -> None:
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
