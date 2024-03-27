class ItemDatabase:
    def __init__(self) -> None:
        self.data = {"apple": 1.5,
        "orange": 1.0}

    def get(self, item:str) -> float:
        if item in self.data:
            return self.data.get(item)
        return 0