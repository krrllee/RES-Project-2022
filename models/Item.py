import sys
import socket,pickle


class Item:
    def __init__(self,code,value):
        self.code = code
        self.value = value

items = list(Item)

