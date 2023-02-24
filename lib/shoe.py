#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size

    def get_shoe_size(self):
        return self._size
    
    def set_shoe_size(self, value):
        if type(value) == int:
            self._size = value

        print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print('Your shoe is as good as new!')
        

    size = property(get_shoe_size, set_shoe_size)