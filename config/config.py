
import os

class Config:

    ENV = os.getenv("ENV", "qa")

    ENV_URLS = {
        "dev": "https://www.saucedemo.com/",
        "qa": "https://www.saucedemo.com/",
        "prod": "https://www.saucedemo.com/"
    }

    BASE_URL = ENV_URLS.get(ENV)

    USERNAME = os.getenv("APP_USERNAME", "standard_user")
    PASSWORD = os.getenv("APP_PASSWORD", "secret_sauce")

    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    
    if BASE_URL is None:
        raise ValueError(f"Invalid ENV value: {ENV}")
    
