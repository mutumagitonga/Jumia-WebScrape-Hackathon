import openai

# Define my OpenAI API key
openai.api_key = 'MY_API_KEY'


def predict_product_category(product_name):
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
    """.format(product_name)

    # Invoke the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 model
        prompt=prompt,
        temperature=0.5,  # Randomness of output (Higher: More adventurous, Lower: More cautious)
        max_tokens=100  # Response length
    )

    # Extract the predicted category from the response
    predicted_product_category = response.choices[0].text.strip()

    print("Predicted category:", predicted_product_category)
