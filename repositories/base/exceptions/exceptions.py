


class BaseException(Exception):
    def __init__(self, status: int, detail: str):
        self.status = status
        self.detail = detail