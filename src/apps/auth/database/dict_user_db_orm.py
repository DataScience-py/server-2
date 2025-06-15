from .base_user_db_orm import UserDBORM
from user import User, AddUser
from typing import Optional, Dict


class DictUserDB(UserDBORM):

    def __init__(self):
        self._storage: Dict[int, User] = {}
        self._email_index: Dict[str, User] = {}
        self._username_index: Dict[str, User] = {}
        self._counter = 1  # Простой счетчик для ID

    def get_user_by_id(self, user_id: Optional[int]) -> Optional[User]:
        """Получить пользователя по ID"""
        if user_id is None: 
            return None        
        return self._storage.get(user_id)

    def get_user_by_email(self, email: Optional[str]) -> Optional[User]:
        """Получить пользователя по email"""
        if email is None: 
            return None
        return self._email_index.get(email)

    def get_user_by_username(self, username: Optional[str]) -> Optional[User]:
        """Получить пользователя по username"""
        if username is None: 
            return None
        return self._username_index.get(username)

    def add_user(self, add_user: AddUser) -> bool:
        """Получить пользователя по username"""
        user = User(
            id=self._counter,
            username=add_user.username,
            email=add_user.email,
            firstname=add_user.firstname,
            lastname=add_user.lastname,
            hashed_password=add_user.hashed_password
        )
        self._storage[user.id] = user
        self._email_index[user.email] = user
        self._username_index[user.username] = user
        self._counter += 1
        return True
    
dict_user_db = DictUserDB()