import os
import time
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv

# Load the .env using the dotenv(python-dotenv) package
load_dotenv()

# Create anthropic client and pass api key
anthropic_client = Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))


def predict_product_category(name_of_product):
    # Define the prompt with product category constraints (as categorized on jumia.co.ke)
    prompt = """
    I have this product name: "{}" 
    Predict the product category of the above product name from among the following options:
    Computing, Electronics, Sporting Goods, Garden & Outdoors, Musical Instruments, Phones & Tablets, 
    Toys & Games, Fashion, Pet Supplies, Home & Office, 
    Automobile, Health & Beauty, Baby Products, Industrial & Scientific

    """.format(name_of_product)

    completion = anthropic_client.completions.create(
        model="claude-2.1",
        max_tokens_to_sample=1024,
        prompt=f"{HUMAN_PROMPT} prompt{AI_PROMPT}",
    )
    print(completion.completion)


predict_product_category("Infinix Note 30 4G, 6.66"", 256GB + 8GB RAM (Dual SIM), 5000mAh, Obsidian Black")
