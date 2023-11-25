from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Accessing environment variable
my_variable_value = os.getenv('MY_VARIABLE')

# Checking if the variable exists
if my_variable_value is not None:
    print(f"Value of MY_VARIABLE: {my_variable_value}")
else:
    print("MY_VARIABLE is not set.")