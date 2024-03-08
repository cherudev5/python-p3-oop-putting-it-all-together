#!/usr/bin/env python3

class Book:
    
    def __init__(self,title,page_count):
        self.title = title
        self.set_page_count(page_count)
        
    def set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self.page_count = page_count
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        
    
   
# book1=Book("Book", 'andrew')

# print(book1.page_count)
