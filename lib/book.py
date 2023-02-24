#!/usr/bin/env python3
class Book:
    def __init__(self, title, author='', page_count=0, genre=''):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, value):
        if type(value) == int:
            self._page_count = value

        print('page_count must be an integer')

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count)



