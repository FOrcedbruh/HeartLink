from schemas.likes import LikeCreateSchema


def LikeForm(
    like_in: LikeCreateSchema
) -> LikeCreateSchema:
    return LikeCreateSchema(
        liked_profile_id=like_in.liked_profile_id,
        profile_id=like_in.profile_id
    )