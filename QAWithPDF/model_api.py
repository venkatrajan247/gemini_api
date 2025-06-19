print("Script started!")

try:
    import sys
    import os

    # Get the absolute path to the directory containing exception.py
    exception_dir = r'C:\Users\nisha\QA_System'
    sys.path.append(exception_dir)

    from exception import customexception
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
        """
        Loads a Gemini-Pro model for natural language processing.

        Returns:
        - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
        """
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

except Exception as e:
    print(f"An unexpected error occurred at the top level: {e}")



















# print("Script started!")

# import sys
# import os

# # Get the absolute path to the directory containing exception.py
# exception_dir = r'C:\Users\nisha\QA_System'
# sys.path.append(exception_dir)

# from exception import customexception
# from logger import logging
# from dotenv import load_dotenv
# from llama_index.llms.gemini import Gemini
# from IPython.display import Markdown, display
# import google.generativeai as genai

# load_dotenv()

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Configure genai with the API key
# configured = False
# if GOOGLE_API_KEY:
#     try:
#         genai.configure(api_key=GOOGLE_API_KEY)
#         logging.info("Google API key configured successfully.")
#         configured = True
#     except Exception as e:
#         logging.error(f"Error configuring Google API: {e}")
# else:
#     logging.error("GOOGLE_API_KEY environment variable not set.")

# def load_model():
#     """
#     Loads a Gemini-Pro model for natural language processing.

#     Returns:
#     - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
#     """
#     try:
#         if not configured:
#             raise ValueError("Google API key was not successfully configured.")
#         model = Gemini(model_name='gemini-pro')
#         return model
#     except Exception as e:
#         raise customexception(e, sys)

# # Example of how you might use it:
# if __name__ == "__main__":
#     logging.info("Loading Gemini Pro model...")
#     try:
#         gemini_model = load_model()
#         logging.info("Gemini Pro model loaded successfully.")
#         response = gemini_model.complete("Explain the basics of cricket in one paragraph.")
#         print(response)
#     except customexception as ex:
#         logging.error(f"Error loading model: {ex}")