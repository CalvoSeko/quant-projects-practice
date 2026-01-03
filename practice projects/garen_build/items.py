class shop_item:
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int],
        item_type: str = None
    ):
        self._name = name
        self._price = price
        self._stats = stats
        self._item_type = item_type
    
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
    def item_type(self):
        return self._item_type

class active_item(shop_item):
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int],
        active_dmg: float = 0,
        item_type: str = None
    ):
        super().__init__(name, price, stats, item_type)
        self._active_dmg = active_dmg
    
    @property
    def active_dmg(self):
        return self._active_dmg