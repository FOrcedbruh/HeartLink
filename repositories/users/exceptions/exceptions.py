from ...base.exceptions.exceptions import BaseException


USER_EXCEPTION_DETAIL: str = "Пользователи не найдены"
USER_EXISTS_EXCEPTION_DETAIL: str = "Пользовтаель с такой почтой уже существует"
USER_NOT_EXISTS_EXCEPTION_DETAIL: str = "Пользователя с такой почтой не существует"

class UserBaseException(BaseException):
    status: int = 400
    detail: str = USER_EXCEPTION_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)


class UserExistsException(BaseException):
        status: int = 400
        detail: str = USER_EXISTS_EXCEPTION_DETAIL

        def __init__(self):
            super().__init__(status=self.status, detail=self.detail)

class UserNotExistsException(BaseException):
    status: int = 400
    detail: str = USER_NOT_EXISTS_EXCEPTION_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)
        