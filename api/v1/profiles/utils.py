from fastapi import Form


def create_profileForm(
        firstname: str = Form(),
        surname: str = Form(),
    ) -> dict:
        return {
            "firstname": firstname,
            "surname": surname,
        }

def update_gender_and_ageForm(
        gender: str = Form(),
        age: int = Form(),
    ) -> dict:
        return {
            "gender": gender,
            "age": age
        }

def update_bio_and_hobbiesForm(
        bio: str = Form(),
        hobbies: list[str] = Form()
    ) -> dict:
    return {
        "bio": bio,
        "hobbies": hobbies
    }
    
