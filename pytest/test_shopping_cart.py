from shopping_cart import ShoppingCart
import pytest
from item_database import ItemDatabase

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()

def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(5)
    for i in range(5):
        cart.add(i)
    with pytest.raises(OverflowError):
        cart.add("cat")

def test_can_get_total_price():
    cart = ShoppingCart(5)
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 1.5
    # item_database.get = Mock(side_effect=mock_get)
    price_map = {
        "apple": 1.5,
        "orange": 1
    }
    assert cart.get_total_price(item_database) == 2.5