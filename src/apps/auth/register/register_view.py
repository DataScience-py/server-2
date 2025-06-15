from fastapi import APIRouter
from user import user_repository, UserRegisterForm

from pydantic import BaseModel

class UserAdded(BaseModel):
    status: str = "200"
    message: str = "user added"

router = APIRouter(tags=["register"])

@router.post("/register/", response_model=UserAdded)
async def register(
    user_register_form: UserRegisterForm
):
    user_repository.add_user(user_register_form=user_register_form)
    return UserAdded()