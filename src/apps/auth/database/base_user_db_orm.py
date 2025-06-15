from abc import ABC, abstractmethod
from typing import Optional
from user import User, AddUser

class UserDBORM(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: Optional[int]) -> Optional[User]:
        """Получить пользователя по ID"""
        pass

    @abstractmethod
    def get_user_by_email(self, email: Optional[str]) -> Optional[User]:
        """Получить пользователя по email"""
        pass

    @abstractmethod
    def get_user_by_username(self, username: Optional[str]) -> Optional[User]:
        """Получить пользователя по username"""
        pass

    @abstractmethod
    def add_user(self, add_user: AddUser) -> bool:
        """Получить пользователя по username"""
        pass