print("Script started!")

import sys
import os
import importlib.util

# Import exception module using full path
exception_path = r'C:\Users\nisha\QA_System\exception.py'
spec_exception = importlib.util.spec_from_file_location("exception", exception_path)
exception_module = importlib.util.module_from_spec(spec_exception)
sys.modules["exception"] = exception_module
spec_exception.loader.exec_module(exception_module)
from exception import customexception

# Import logger module using full path
logger_path = r'C:\Users\nisha\QA_System\logger.py'
spec_logger = importlib.util.spec_from_file_location("logger", logger_path)
logger_module = importlib.util.module_from_spec(spec_logger)
sys.modules["logger"] = logger_module
spec_logger.loader.exec_module(logger_module)
from logger import logging

from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure genai with the API key
configured = False
if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        logging.info("Google API key configured successfully.")
        configured = True
    except Exception as e:
        logging.error(f"Error configuring Google API: {e}")
else:
    logging.error("GOOGLE_API_KEY environment variable not set.")

def load_model():
    try:
        if not configured:
            raise ValueError("Google API key was not successfully configured.")
        model = Gemini(model_name='gemini-pro')
        return model
    except Exception as e:
        raise customexception(e, sys)

# Example of how you might use it:
if __name__ == "__main__":
    logging.info("Loading Gemini Pro model...")
    try:
        gemini_model = load_model()
        logging.info("Gemini Pro model loaded successfully.")
        response = gemini_model.complete("Explain the basics of cricket in one paragraph.")
        print(response)
    except customexception as ex:
        logging.error(f"Error loading model: {ex}")