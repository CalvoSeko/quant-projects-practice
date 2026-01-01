class shop_item:
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int]
    ):
        self._name = name
        self._price = price
        self._stats = stats
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def stats(self):
        return self._stats
