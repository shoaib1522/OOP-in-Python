import struct

class CellPhone:
	def __init__(self, manufact, model, price):
		self.__manufact = manufact
		self.__model = model
		self.__retail_price = price

	def set_manufact(self, manufact):
		self.__manufact = manufact

	def set_model(self, model):
		self.__model = model

	def set_retail_price(self, price):
		self.__retail_price = price

	def get_manufact(self):
		return self.__manufact

	def get_model(self):
		return self.__model

	def get_retail_price(self):
		return self.__retail_price
	
	def __str__(self):
		return self.__manufact + ' ' + self.__model + ' ' + str(self.__retail_price)
	
	def get_binary_string(self):
		return self.__manufact.ljust(20) + self.__model.rjust(10) + struct.pack('i', self.__retail_price)
	
