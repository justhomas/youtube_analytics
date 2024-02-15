from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    PROJECT_SLUG: str
    SQLALCHEMY_DATABASE_URI: str
    DATA_FOLDER: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
