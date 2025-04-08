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
    return get_terminal_shop_products(client).model_dump()


def create_address(city: str, country: str, name: str, street1: str, zip: str) -> str:
    """
    Sets the users address for the shipment.

    Args:
        client (Terminal): The Terminal Shop client.
        city (str): The city.
        country (str): The country.
        name (str): The name.
        street1 (str): The street address.
        zip (str): The zip code.

    Returns:
        str: The address id.
    """
    client = get_terminal_shop_client()
    address = Address(
        id=str(uuid4()),
        city=city,
        country=country,
        name=name,
        street1=street1,
        zip=zip,
    )
    shipping_address_id = set_shipping_address(client, address)
    return shipping_address_id


def run_order_workflow(variant_id: str, quantity: int) -> str:
    """
    Runs the order workflow to purchase coffee.
    This function will guide the user through the process of creating an order.
    The workflow consists of the following steps:
    1. Check if the user has a shipping address.
    2. If not ask the user for their shipping address.
    3. Check if the user has a valid credit card or not.
    4. If not redirect the user to an url where their credit card info can be entered.
    5. Create the order.
    6. Return the order id.

    Args:
        variant_id (str): The variant id of the product.
        quantity (int): The quantity of the product.

    Returns:
        str: A message indicating the result of the order creation process.
    """
    client = get_terminal_shop_client()
    shipping_address = get_shipping_address(client)
    if shipping_address:
        shipping_address_id = shipping_address[0].id
    else:
        return (
            "Please enter your shipping address."
            "We need your city, street, country code, name and zip"
        )

    credit_card = get_credit_card(client)
    if credit_card:
        card_id = credit_card[0].id
    else:
        url = collect_credit_card_info(client)
        return f"Please go to {url.url} to enter your credit card details."

    product_variant = {variant_id: quantity}
    order_id = create_order(client, shipping_address_id, card_id, product_variant)
    return f"Order created with id: {order_id}"
