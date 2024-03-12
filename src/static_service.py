import re


class StaticSrvice:
    @staticmethod
    def validate_name(name: str) -> bool:
        if not 4 <= len(name) <= 32:
            return False

        if re.search(pattern=r'\d', string=name):
            return False

        if not re.match(pattern=r'^[a-zA-Z]+$', string=name):
            return False

        return True


