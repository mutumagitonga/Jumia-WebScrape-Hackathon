import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

# Load the .env using the dotenv(python-dotenv) package
load_dotenv()

# Pass api key to the genai client
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def predict_product_category(name_of_product):
    # Define the prompt with product category constraints (as categorized on jumia.co.ke)
    prompt = """
    Given a product name, predict the product category from the following options:
    Computing, Electronics, Sporting Goods, Garden & Outdoors, Musical Instruments, Phones & Tablets, 
    Toys & Games, Fashion, Pet Supplies, Home & Office, 
    Automobile, Health & Beauty, Baby Products, Industrial & Scientific

    Product Name: "{}"
    """.format(name_of_product)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


