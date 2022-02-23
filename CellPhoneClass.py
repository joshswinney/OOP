class CellPhone:


    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__set_model = model

    def set_retail_price(self, price):
        self.__set_retail_price = price

    def get_manufact(self, manufact):
        return "Manufacturer: " + self.__manufact

    def get_model(self, model):
        return "Model number: " + self.__set_model

    def get_retail_price(self, price):
        return "Retail price: " + self.__set_retail_price

    def __str__(self):
        return self.__retail_price

    