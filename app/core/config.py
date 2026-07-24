import os 
from dotenv import load_dotenv

load_dotenv()

SERVER_ENV=os.getenv("SERVER_ENV")

# Origin Environment Variables for CORS configuration
LOCAL_ORIGIN=os.getenv("LOCAL_ORIGIN","http://localhost:3000")
PRODUCTION_ORIGIN=os.getenv("PRODUCTION_ORIGIN","")