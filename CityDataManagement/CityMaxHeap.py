from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self, index):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        current_index : int = index
        while self.has_parent(current_index):
            parent_index : int = self.get_parent_index(current_index)
            if self.get_city_population(current_index) > self.get_parent_population(current_index):
                self.swap_nodes(current_index, parent_index)
                current_index = parent_index
            else:
                return

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        if self.has_parent(index):
            parent_index = self.get_parent_index(index)
            if self.get_city_population(index) > self.get_parent_population(index):
                self.swap_nodes(index, parent_index)
                self.heapify_up_recursive(parent_index)

    def heapify_floyd(self, index, amount_of_cities): # FLOYDDDDDDD
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.
        
        """
        for i in range(amount_of_cities, index, -1):
            if(self.recursive):
                self.heapify_down_recursive(self.get_parent_index(i))
            else:
                self.heapify_down_iterative(self.get_parent_index(i))

    def heapify_down_iterative(self, index):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        current_index = index
        while self.has_left_child(current_index):
            child_index = self.get_left_child_index(current_index)
            if self.has_right_child(current_index) and self.get_right_child_population(current_index) > self.get_left_child_population(current_index):
                child_index = self.get_right_child_index(current_index)
            if self.get_city_population(current_index) < self.get_city_population(child_index):
                self.swap_nodes(current_index, child_index)
                current_index = child_index
            else:
                return

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # super.heapify_down_recursive(self, index)
        child_index = None
        if self.has_left_child(index):
            child_index = self.get_left_child_index(index)
        if self.has_right_child(index) and self.get_right_child_population(index) > self.get_left_child_population(index):
            child_index = self.get_right_child_index(index)
        if child_index == None:
            return
        if self.get_city_population(index) < self.get_city_population(child_index):
            self.swap_nodes(index, child_index)
            self.heapify_down_recursive(child_index)
        

    def remove(self, index: int = 0):
        """
        Remove a City from the Max-Heap
        """
        # super.remove(self.get_index(city))
        self.currentHeapLastIndex -= 1
        self.swap_nodes(index, self.currentHeapLastIndex)
        if(self.recursive):
            self.heapify_down_recursive(index)
        else:
            self.heapify_down_iterative(index)
