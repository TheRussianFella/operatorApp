from enum import Enum

def enum(**named_values):
    return type('Enum', (), named_values)
