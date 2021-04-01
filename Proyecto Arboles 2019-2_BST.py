# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:00:27 2019

@author: diego
"""
import Node
class BST:
    def __init__(self):
        self._root = None
    
    def addNode(self, label, x,y):
        if(self._root):
            self._addNode(label,x,y, parent = self._root,(level= root.level()+1))
        else:
            self._root = Node(label, x,y,None,level=0)
    
    def _addNode(self, label, x,y, parent,level):
          
        if((parent.getLevel() % 2) != 0 ):
        
            if(y >= parent.getCoordinates([1])):
                
                rc = parent.hasRightChild()
                if(rc):
                    self._addNode(label, x,y, rc, level = (rc.getLevel() +1))
                else:
                    newNode = Node(label, x,y, parent,(level = parent.getLevel() +1))
                    parent.setRightChild(newNode)
            else: 
            
                if(y < parent.getCoordinates([1])):
                   
                    lc = parent.hasLeftChild()
                    if(lc):
                        self._addNode(label, x,y, lc, (level = lc.getLevel()+1)
                    else:
                        newNode = Node(label, x,y, parent,(level = parent.getLevel() +1))
                        parent.setLeftChild(newNode)
        else:
             if(x < parent.getCoordinates([0]) ):
                lc = parent.hasLeftChild()
                if(lc):
                    self._addNode(label, x,y, lc, level = lc.getLevel() + 1)
                else:
                    newNode = Node(label, x,y, parent, level = parent.getLevel() + 1)
                    parent.setLeftChild(newNode)
                    
             else:
                 
                 if(x >= parent.getCoordinates([0]) ):
                rc = parent.hasRightChild()
                if(rc):
                    self._addNode(label, x,y, rc, (level = rc.getLevel() + 1))
                else:
                    newNode = Node(label, x,y, parent, (level = parent.getLevel() + 1))
                    parent.setRightChild(newNode)
       
            
    
    def searchNode(self, label):
        if(self._root):
            return self._searchNode(label, self._root)
        else:
            print("The tree is empty.")
    
    def _searchNode(self, label, parent):
        if(not parent):
            return None
        if(label == parent.getLabel()):
            return parent
        else:
            node = self._searchNode(label, parent.hasLeftChild())
            if(not node):
                node = self._searchNode(label, parent.hasRightChild())
            return node
    
   
            
    def removeNode(self, label):
        if(self._root):
            targetNode = self.searchNode(label)
            if(targetNode):
                self._removeNode(targetNode)
                print("The node has been removed successfuly")
            else:
                print("Element with label ", label, " does not exists!")
        else:
            print("The tree is empty.")
            
    def _removeNode(self, node):
        if(node.isLeaf()):
            if(node.isLeftChild()):
                node.getParent().setLeftChild(None)
            else:
                node.getParent().setRightChild(None)            
            node.setParent(None);
        else:
            if(node.hasLeftChild() and node.hasRightChild()):
                suc = self._getSucessor(node.hasRightChild())
                self._updateNode(node, suc)
                if(suc.isLeaf()):
                    suc.getParent().setLeftChild(None)
                    suc.setParent(None)
                else:
                    suc.getParent().setLeftChild(suc.hasRightChild())
                    suc.hasRightChild().setParent(suc.getParent())
                    suc.setRightChild(None)
                    suc.setParent(None)
            else:
                if(node.isLeftChild()):
                    if(node.hasLeftChild()):
                        node.getParent().setLeftChild(node.hasLeftChild())
                        node.hasLeftChild().setParent(node.getParent())
                        node.setLeftChild(None)
                    else:
                        node.getParent().setLeftChild(node.hasRightChild())
                        node.hasRightChild().setParent(node.getParent())
                        node.setRightChild(None)
                else:
                    if(node.hasLeftChild()):
                        node.getParent().setRightChild(node.hasLeftChild())
                        node.hasLeftChild().setParent(node.getParent())
                        node.setLeftChild(None)
                    else:
                        node.getParent().setRightChild(node.hasRightChild())
                        node.hasRightChild().setParent(node.getParent())
                        node.setRightChild(None)
                node.setParent(None)
                
                    
    def _updateNode(self, oldNode, newNode):
        oldNode.setValue(newNode.getValue())
        oldNode.setLabel(newNode.getLabel())
        
    def _getSucessor(self, node):
        lc = node.hasLeftChild()
        if(lc):
            return self._getSucessor(lc)
        else:
            return node
        
        
        
        
myTree = BST()
myTree.addNode("A",10,10)
myTree.addNode("B",11,13)
myTree.addNode("C", 22,13)
myTree.addNode("D",3, 7)
myTree.addNode("E",18, 28)