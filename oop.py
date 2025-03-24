""" def name():
    name = get_name()
    house = get_house()
    print(name , house)
    
def get_name():
    return input("Name: ")

def get_house():
    return input("house: ") """
    
class Student:
    def __init__(self, name, last):
        if not name:
            raise ValueError("missing name")