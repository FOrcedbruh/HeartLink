from fastapi import Body


def create_profileForm(
        firstname: str = Body(),
        surname: str = Body(),
    ) -> dict:
        return {
            "firstname": firstname,
            "surname": surname,
        }

def update_gender_and_ageForm(
        gender: str = Body(),
        age: int = Body(),
    ) -> dict:
        return {
            "gender": gender,
            "age": age
        }

def update_bio_and_hobbiesForm(
        bio: str = Body(),
        hobbies: list[str] = Body()
    ) -> dict:
    return {
        "bio": bio,
        "hobbies": hobbies
    }
    
