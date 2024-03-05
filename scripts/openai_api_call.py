import os
from dotenv import load_dotenv

# Load the .env using the dotenv(python-dotenv) package
load_dotenv()


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


product_name = "NIVEA Radiant & Beauty Advanced Care Lotion"
predict_product_category(product_name)
