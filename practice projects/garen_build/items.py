class shop_item:
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int],
        unique: bool = False
    ):
        self._name = name
        self._price = price
        self._stats = stats
        self._unique = unique
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def stats(self):
        return self._stats
    
    @property
    def unique(self):
        return self._unique

class active_item(shop_item):
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int],
        active_dmg: float = 0,
        unique: bool = False
    ):
        super().__init__(name, price, stats, unique)
        self._active_dmg = active_dmg
    
    @property
    def active_dmg(self):
        return self._active_dmg