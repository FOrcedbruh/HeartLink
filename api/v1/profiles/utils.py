from fastapi import Form



def create_profileForm(
        firstname: str = Form(),
        surname: str = Form(),
        gender: str = Form(),
        age: int = Form(),
        profileImages: list[str] = Form(),
        hobbies: list[str] = Form()
    ) -> dict:
        return {
            "firstname": firstname,
            "surname": surname,
            "gender": gender,
            "age": age,
            "profileImages": profileImages,
            "hobbies": hobbies
        }

