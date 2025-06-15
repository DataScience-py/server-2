from typing import Optional
from fastapi import HTTPException

from .user import User, UserRegisterForm, UserExists, LoginUser, AddUser
from hasher import bcrypt_hasher, BaseHasher
from database import UserDBORM, dict_user_db

class UserRepository:
    def __init__(self, password_hasher: BaseHasher, database_orm: UserDBORM) -> None:
        self.password_hasher: BaseHasher = password_hasher
        self.database_orm: UserDBORM = database_orm

    def _get_user(self, user_exists: UserExists) -> User:
        if user_exists.id is not None:
            by_id = self.database_orm.get_user_by_id(user_exists.id)
            if by_id is not None:
                return by_id
        if user_exists.email is not None:
            by_email = self.database_orm.get_user_by_email(user_exists.email)
            if by_email is not None:
                return by_email
        if user_exists is not None:
            by_username = self.database_orm.get_user_by_username(user_exists.username)
            if by_username is not None:
                return by_username
        raise HTTPException(status_code=404, detail="Incorect_data")

    def get_user(self, login_user: LoginUser) -> Optional[User]:
        user = self._get_user(user_exists=UserExists(id=login_user.id, email=login_user.email, username=login_user.username))
        if not self.password_hasher.verify(login_user.password, user.hashed_password):
            raise HTTPException(status_code=404, detail="Incorect_data")
        return user

    def add_user(self, user_register_form: UserRegisterForm) -> bool:
        if self.is_user_exists(UserExists(email=user_register_form.email, username=user_register_form.username)):
            raise HTTPException(status_code=404, detail="Incorect_data")
        if user_register_form.password != user_register_form.confirm_password:
            raise HTTPException(status_code=404, detail="password is not confirm")
        self.database_orm.add_user(
            AddUser(
                username=user_register_form.username, 
                email=user_register_form.email, 
                firstname=user_register_form.firstname, 
                lastname=user_register_form.lastname, 
                hashed_password=self.password_hasher.hash(user_register_form.password)
                )
            )
        print("user added")
        return True

    def is_user_exists(self, user_exists: UserExists) -> bool:
        return (
            self.database_orm.get_user_by_id(user_exists.id) is not None or 
            self.database_orm.get_user_by_email(user_exists.email) is not None or 
            self.database_orm.get_user_by_username(user_exists.username) is not None
            )


user_repository = UserRepository(password_hasher=bcrypt_hasher, database_orm=dict_user_db)