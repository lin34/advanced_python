from typing import List

class ShoppingCart:
    def __init__(self, maxSize: int) -> None:
        self.items: List[str] = []
        self.maxSize = maxSize

    def add(self, item:str):
        if self.size() >= self.maxSize:
            raise OverflowError("Cannot add more items")
        self.items.append(item)

    
    def size(self) -> int:
        return len(self.items)

    def get_items(self):
        return self.items
    
    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            price = price_map.get(item)
            total_price += price
        return total_price

