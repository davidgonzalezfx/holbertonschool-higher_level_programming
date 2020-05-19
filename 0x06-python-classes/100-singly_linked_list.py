#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        actual = self.__head
        to_print = ''
        while actual:
            to_print = to_print + str(actual.data)
            if actual.next_node:
                    to_print = to_print + '\n'
            actual = actual.next_node
        return to_print

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif value <= self.__head.data:
            self.__head = Node(value, self.__head)
        elif value > self.__head.data:
            actual = self.__head
            while actual is not None:
                if not actual.next_node:
                    actual.next_node = Node(value)
                    break
                elif value < actual.next_node.data:
                    actual.next_node = Node(value, actual.next_node)
                    break
                actual = actual.next_node
