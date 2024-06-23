from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALPACA_API_ENDPOINT: str
    ALPACA_API_KEY: str
    ALPACA_API_SECRET: str


settings = Settings()
