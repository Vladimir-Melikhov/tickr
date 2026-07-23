from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = '-'
    description: str | None = None
    database_url: str | None = None

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
