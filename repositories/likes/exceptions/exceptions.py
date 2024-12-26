from ...base.exceptions.exceptions import BaseException


LIKE_NOT_FOUND_EXCEPTION: str = "Отметки 'нравится' не найдены"


class LikeNotFoundException(BaseException):
    status: int = 400
    detail: str = LIKE_NOT_FOUND_EXCEPTION

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)