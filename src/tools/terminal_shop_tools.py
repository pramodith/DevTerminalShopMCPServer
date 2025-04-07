from uuid import uuid4
from terminal_shop.types import Address
from utils import (
    get_terminal_shop_client,
    get_terminal_shop_products,
    set_shipping_address,
    get_shipping_address,
    get_credit_card,
    create_order,
    collect_credit_card_info,
)


def get_coffee_products():
    """
    Lists out all the different coffee types available for purchase.

    Returns:
        ProductList: A list of products.
    """
    client = get_terminal_shop_client()
    return get_terminal_shop_products(client)


def run_order_workflow() -> str:
    """
    Runs the order workflow to purchase coffee.
    This function will guide the user through the process of creating an order.
    If no address is present it will prompt the user for the following information:
    - City
    - Country
    - Name
    - Street address
    - Zip code
    - Credit card details

    If no credit card info is present it will prompt the user to enter their credit card details.
    at a url.
    Args:
        None

    Returns:
        str: A message indicating the result of the order creation process.
    """
    client = get_terminal_shop_client()
    shipping_address = get_shipping_address(client)
    products = get_coffee_products()
    if shipping_address:
        shipping_address_id = shipping_address[0].id
    else:
        id = str(uuid4())
        city = input("Enter city: ")
        country = input("Enter country: ")
        name = input("Enter name: ")
        street1 = input("Enter street address: ")
        zip = input("Enter zip code: ")
        address = Address(
            id=id, city=city, country=country, name=name, street1=street1, zip=zip
        )
        shipping_address_id = set_shipping_address(client, address)

    credit_card = get_credit_card(client)
    if credit_card:
        card_id = credit_card[0].id
    else:
        url = collect_credit_card_info(client)
        return f"Please go to {url.url} to enter your credit card details."

    product_string = ""
    index = 0
    variant_price_map = {}
    for product in products.data:
        description = product.description
        name = product.name
        for variant in product.variants:
            product_string += f"{index + 1}.{name}: {description}\nQuantity: {variant.name}\nPrice: ${variant.price / 100}\n\n"
            variant_price_map[index + 1] = (variant.id, variant.price / 100)
            index += 1

    product_index = input(
        f"Pick your choice by selecting the index i.e. 1, 2 etc."
        f"\nWhich product would you like to order?\r\n{product_string}"
    )

    quantity = input(f"How many of {product_index} would you like to order?")
    product_variant = {variant_price_map[int(product_index)][0]: int(quantity)}
    order_id = create_order(client, shipping_address_id, card_id, product_variant)
    return f"Order created with id: {order_id}"
