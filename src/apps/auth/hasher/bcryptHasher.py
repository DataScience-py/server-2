import bcrypt

from .base_hasher import BaseHasher


class BcryptHasher(BaseHasher):
    def verify(self, password: str, hashed_password: str) -> bool:
        """Проверяет пароль с использованием bcrypt."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    def hash(self, password: str) -> str:
        """Генерирует bcrypt-хеш пароля."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
bcrypt_hasher = BcryptHasher()