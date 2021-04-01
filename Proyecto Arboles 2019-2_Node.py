# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:59:55 2019

@author: diego
"""

class Node:
    def __init__(self,label,x,y,level):
        self._label = label
        self._coordinates = [x,y]
        self._parent = None
        self._rightChild = None
        self._leftChild = None
        self._level = level
    
    def getCoordinates(self):
        return self._coordinates
    
    def getLabel(self):
        return self._label
    
    def getLevel(self):
        return self.getLevel
    
    def setCoordinates(self, x,y):
        self._coordinates = [x,y]
        
    def setLabel(self, l):
        self._label = l
        
    def setLevel(self, level):
        self._level = level
    
    def hasRightChild(self):
        return self._rightChild
    
    def hasLeftChild(self):
        return self._leftChild
    
    def setRightChild(self, child):
        self._rightChild = child
    
    def setLeftChild(self, child):
        self._leftChild = child
    
    def isLeaf(self):
        return (not self._leftChild and not self._rightChild)
    
    def getParent(self):
        return self._parent
    
    def isRightChild(self):
        return (self.getParent().hasRightChild() and self._label == self._parent._rightChild._label)
    
    def isLeftChild(self):
        return (self.getParent().hasLeftChild() and self._label == self._parent._leftChild._label)
    
    def setParent(self, parent):
        self._parent = parent