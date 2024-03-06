import os
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
    - Computing
    - Electronics
    - Sporting Goods
    - Garden & Outdoors
    - Musical Instruments
    - Phones & Tablets
    - Toys & Games
    - Fashion
    - Pet Supplies
    - Home & Office
    - Automobile
    - Health & Beauty
    - Baby Products
    - Industrial & Scientific

    Product Name: "{}"
    """.format(name_of_product)

    # Set up the model
    generation_config = {
      "temperature": 0.9,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    # Define the model & its parameters
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,)

    convo = model.start_chat(history=[])  # Start chat
    convo.send_message(prompt)  # Send the prompt
    # print(convo.last.text)  # Extract the text
    return convo.last.text  # Return AI response

