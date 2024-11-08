# Author: Jeevana Dova
# Date: 11-02-2024
# Description: This Program defines a class named Product that encapsulates the details of a product order

class Product:
    def __init__(self, name, units, price):
        self.__name = name
        self.__units = units
        self.__price = price
        self.__total_cost = units * price

    # Getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter for units
    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units
        self.__update_total_cost()  # Recalculate total cost when units are updated

    # Getter and setter for price_per_unit
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
        self.__update_total_cost()  # Recalculate total cost when price is updated

    # Getter for total_cost (no setter, since total cost is derived)
    def get_total_cost(self):
        return self.__total_cost

    # Update total cost based on current units and price
    def __update_total_cost(self):
        self.__total_cost = self.__units * self.__price
