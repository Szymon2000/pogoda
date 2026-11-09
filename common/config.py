from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
    API_KEY = os.getenv("API_KEY")
    CITY = "Lisbon"
    FILENAME = "pogoda_2026.csv"