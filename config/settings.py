import os

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com/login")

BROWSER = os.getenv("BROWSER", "chrome")

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"