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

class dummy:
    def __init__(
        self, 
        max_health: float, 
        health: float = max_health, 
        armor: float = 0, 
        magic_resistance: float = 0
    ):
        self._max_health = max_health
        self._health = health
        self._armor = armor
        self._magic_resistance = magic_resistance
    
    @property
    def max_health(self):
        return self._max_health
    
    @property
    def health(self):
        return self._health
    
    @property
    def armor(self):
        return self._armor
    
    @property
    def magic_resistance(self):
        return self._magic_resistance