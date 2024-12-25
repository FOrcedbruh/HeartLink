from fastapi import Body
from schemas.profiles import ProfileCreateSchema, ProfileUpdateSchema


def create_profileForm(
    profile_in: ProfileCreateSchema = Body()
) -> ProfileCreateSchema:
    return profile_in


def update_profileForm(
    profile_in: ProfileUpdateSchema = Body()
) -> ProfileUpdateSchema:
    return ProfileUpdateSchema(
        bio=profile_in.bio,
        hobbies=profile_in.hobbies,
        firstname=profile_in.firstname,
        surname=profile_in.surname,
        age=profile_in.age
    )


    
