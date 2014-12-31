'''
Created on Dec 2, 2014
@author: c

A Cell object represents one cell of memory on the Turing Machine's tape. A cell
contains a symbol; initially, the cell's content is delta, which denotes that 
it's empty (the underscore char is used to represent delta).

Cells are connected together as a doubly-connected linked list to represent the
tape of the TM. Therefore, each cell has a reference to 'next' and 'prev'.
'''

class Cell:
    
    def __init__(self, symbol = '_'):
        self.symbol = symbol
        self.prev = None
        self.next = None