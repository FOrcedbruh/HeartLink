from ...base.exceptions.exceptions import BaseException


HOBBY_NOT_FOUND_EXCEPTION_DETAIL: str = "Увлечения не найдены"

class HobbyNotFoundException(BaseException):
    status: int = 400
    detail: str = HOBBY_NOT_FOUND_EXCEPTION_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)