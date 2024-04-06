class pet:
    max_matn = 0
    def __init__(self, matn : int, tentn : str, maulong : str, cannang : str, makh : int):
        self.__matn = matn
        self.__tentn = tentn
        self.__maulong = maulong
        self.__cannang = cannang
        self.__makh = makh

    
    def get_matn(self):
        return self.__matn
    
    def set_matn(self, matn):
        self.__matn = matn

    @classmethod
    def generate_matn(cls):
        cls.max_matn += 1
        return cls.max_matn
    
    def get_tentn(self):
        return self.__tentn
    
    def set_tentn(self, tentn):
        self.__tentn = tentn

    def get_maulong(self):
        return self.__maulong
    
    def set_maulong(self, maulong):
        self.__maulong = maulong
    
    def get_cannang(self):
        return self.__cannang
    
    def set_cannang(self, cannang):
        self.__cannang = cannang
    
    def get_makh(self):
        return self.__makh