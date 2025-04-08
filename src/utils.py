from terminal_shop import Terminal
from terminal_shop.types import ProductListResponse, Profile, Address
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


def get_terminal_shop_client(mode: str = "dev") -> Terminal:
    return Terminal(
        # defaults to "dev".
        environment=mode,
    )


def get_terminal_shop_products(client: Terminal) -> ProductListResponse:
    """
    Lists out all the different coffee types available for purchase.

    Args:
        client (Terminal): The Terminal Shop client.

    Returns:
        ProductList: A list of products.
    """
    products = client.product.list()
    return products


def get_customer_profile(client: Terminal) -> Profile:
    """
    Retrieves the customer profile.
    The customer id can then be used to make subsequent queries like getting the
    shipping address

    Args:
        client (Terminal): The Terminal Shop client.

    Returns:
        Profile: The customer profile.
    """
    customer = client.profile.me()
    return customer.data


def set_shipping_address(client: Terminal, shipping_address: Address):
    """
    Sets the shipping address.
    The shipping address id can then be used to make subsequent queries like creating an order.

    Args:
        client (Terminal): The Terminal Shop client.
        shipping_address (Address): The shipping address.

    Returns:
        Address: The shipping address.
    """
    response = client.address.create(
        city=shipping_address.city,
        country=shipping_address.country,
        street1=shipping_address.street1,
        zip=shipping_address.zip,
        name=shipping_address.name,
    )

    return response.data


def get_shipping_address(client: Terminal) -> Address:
    """
    Retrieves the shipping address.
    The shipping address id can then be used to make subsequent queries like creating an order.

    Args:
        client (Terminal): The Terminal Shop client.

    Returns:
        Address: The shipping address
    """
    response = client.address.list()
    return response.data


def get_credit_card(client: Terminal) -> str:
    """
    Retrieves the credit card.
    The credit card id can then be used to make subsequent queries like creating an order.

    Args:
        client (Terminal): The Terminal Shop client.

    Returns:
        str: The credit card id.
    """
    response = client.card.list()
    return response.data


def set_credit_card(
    client: Terminal, number: str, exp_month: str, exp_year: str, cvc: str
):
    """
    Sets the credit card to be used for the order.

    Args:
        client (Terminal): The Terminal Shop client.
        number (str): The card number.
        exp_month (str): The card expiration month.
        exp_year (str): The card expiration year.
        cvc (str): The card security code.

    Returns:
        str: The credit card id.
    """
    stripe_card_token = get_stripe_card_token(number, exp_month, exp_year, cvc)
    response = client.card.create(stripe_card_token)
    return response.data


def create_order(
    client: Terminal,
    shipping_address_id: str,
    card_id: str,
    product_variants: Dict[str, int],
) -> str:
    """
    Creates an order for your coffee to be shipped.
    Args:
        client (Terminal): The Terminal Shop client.
        shipping_address_id (str): The shipping address id.
        card_id (str): The card id.
        product_variants (Dict[str, int]): The product variants.
    Returns:
        str: The order id.
    """
    response = client.order.create(
        address_id=shipping_address_id, card_id=card_id, variants=product_variants
    )
    return response.data


def collect_credit_card_info(client: Terminal) -> str:
    """
    Creates a temp url for collecting credit card info via stripe.
    Args:
        client (Terminal): The Terminal Shop client.
    Returns:
        str: The url to enter your cc info.
    """
    response = client.card.collect()
    return response.data