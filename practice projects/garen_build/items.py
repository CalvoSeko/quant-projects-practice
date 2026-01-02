class shop_item:
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int],
        percent_dmg_amp: float = 0
    ):
        self._name = name
        self._price = price
        self._stats = stats
        self._percent_dmg_amp = percent_dmg_amp    
    
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
    def percent_dmg_amp(self):
        return self._percent_dmg_amp

class active_item(shop_item):
    def __init__(
        self, 
        name: str, 
        price: int, 
        stats: dict[str, int],
        percent_dmg_amp: float = 0,
        active_dmg: float = 0
    ):
        super().__init__(name, price, stats, percent_dmg_amp)
        self._active_dmg = active_dmg
    
    @property
    def active_dmg(self):
        return self._active_dmg