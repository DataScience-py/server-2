from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_DATA = "PLEASE ADD DATA IN .env FILE"


class Settings(BaseSettings):
    APP_NAME: str = "TermiusServerAuth"
    DATABASE_URL: str =ENV_DATA

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()