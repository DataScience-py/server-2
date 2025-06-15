from abc import ABC, abstractmethod

class BaseHasher(ABC):
    @abstractmethod
    def verify(self, password: str, hashed_password: str) -> bool:
        """Проверяет, соответствует ли пароль хешу."""
        pass

    @abstractmethod
    def hash(self, password: str) -> str:
        """Генерирует хеш пароля."""
        pass