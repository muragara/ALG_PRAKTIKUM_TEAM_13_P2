from abc import ABC, abstractmethod
from typing import List
from CityDataManagement.City import City
import copy


class AbstractCityHeap(ABC):
    """
    Abstract Class with the responsibility to offer the common methods of both a Min and Max heap.

    This class is divided into two parts:

    -Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)

    -Shared Methods Block (Methods identical for both a min and a max heap)


    Param:
    ------
    rawCityData: List[City]: raw unsorted List of City Objects

    recursiv: bool: should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
    
    floyd: bool: should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.

    Hint:   
    -----
    Think of the index of all elements in the heap as an array. Array: ([0],[1],[2],[3]...)
    The root is located at index 0, so it`s children must be on Index 1 and 2 and so on...
    """

    heapStorage: List[City] = [] # empty List of City Objects
    maximumHeapCapacity = 0
    currentHeapLastIndex = 0  # current last Index of the Heap based on the inserted City Objects, this is also the current Size of the Heap
    rawCityData: List[City] = []

    recursive: bool = False
    floyd: bool = False

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        self.rawCityData = raw_city_data
        self.maximumHeapCapacity = len(self.rawCityData)  # set Maximum Heap Capacity to the amount of City Objects
        self.recursive = recursive
        self.floyd = floyd
        self.heapStorage = []
        self.insert_raw_city_data_into_heap()

    # ----Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)--

    @abstractmethod
    def heapify_up_iterative(self, index):
        """
        Establish heap conditions iterative upwards.
        """

    @abstractmethod
    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions via Floyds Heap Construction Algorithmus
        """

    @abstractmethod
    def heapify_up_recursive(self, index):
        """
        Establish heap conditions recursive upwards.
        """

    @abstractmethod
    def heapify_down_iterative(self, index): # TODO
        """
        Establish heap conditions iterative downwards.
        """

    @abstractmethod
    def heapify_down_recursive(self, index): # TODO
        """
        Establish heap conditions recursive downwards.
        """
    
    @abstractmethod
    def remove(self, index):
        """
        Remove a City from the Heap.
        """
       
    # ------Shared Methods Block (Methods identical for both a min and a max heap)------

    def insert_raw_city_data_into_heap(self) -> None:
        """
        Insertion of all cities into the Heap.
        """
        if self.floyd:
            self.build_heap_via_floyd()
        else:
            for i in self.rawCityData:
                self.insert(i)

    def build_heap_via_floyd(self) -> None:
        """
        Build a Heap via Floyds Heap Construction Algorithm from a unsorted List Of Cities.
        """
        # TODO: implement me!
        self.heapStorage = copy.deepcopy(self.rawCityData)
        self.currentHeapLastIndex = len(self.heapStorage)
        self.heapify_floyd(0, self.currentHeapLastIndex)

    def insert(self, city) -> None:
        """
        Insert a single City into the Heap.
        """
        # TODO: implement me!
        self.heapStorage.append(city)
        self.currentHeapLastIndex += 1 

        if self.recursive:
            self.heapify_up_recursive(self.currentHeapLastIndex - 1)
        else:
            self.heapify_up_iterative(self.currentHeapLastIndex - 1)

    def get_root_city(self) -> City:
        """
        Return the City at the Root
        """
        # TODO: implement me!
        return self.heapStorage[0]

    def get_parent_index(self, index) -> int:
        """
        Return the index of the parent node. 
        """
        # TODO: implement me!
        return int((index - 1) / 2)

    def get_left_child_index(self, index) -> int:
        """
        Return the index of the left child. 
        """
        return int((index * 2) + 1)

    def get_right_child_index(self, index) -> int:
        """
        Return the index of the right child. 
        """
        # TODO: implement me!
        return int((index * 2) + 2)

    def has_parent(self, index) -> bool:
        """
        Check if the node has a parent. Return:    
            True    = Has parent
            False   = No parent
        """
        # TODO: implement me!
        return index > 0

    def has_left_child(self, index) -> bool:
        """
        Check if the Node has a left Child. Return:
            True    = Has leftChild
            False   = No leftChild
        Hint:
        -----
        The Index of the Child can be used for this purpose.
        """
        # TODO: implement me!
        if self.get_left_child_index(index) < self.currentHeapLastIndex:
            return True

    def has_right_child(self, index) -> bool:
        """
        Check if the Node has a right Child. Return:
            True    = Has rightChild
            False   = No rightChild
        Hint:
        -----
        The Index of the Child can be used for this purpose.
        """
        # TODO: implement me!
        if self.get_right_child_index(index) < self.currentHeapLastIndex:
            return True

    def get_city_population(self, index) -> int:
        """
        Return the Population of a City with the given index in the heap.
        """
        # TODO: implement me!
        return self.heapStorage[index].population

    def get_parent_population(self, index) -> int:
        """
        Returns the population of the parent.
        Hint:
        -----
        We need the position of the parent in the StorageArray to extract the population from this position.
        """
        # TODO: implement me! => (index - 1) / 2
        if self.has_parent:
            parent_index: int = self.get_parent_index(index)
            parent: City = self.heapStorage[parent_index]
            return parent.population
        else:
            None # Anmerkung: sollte hier nicht "return None" stehen?
        
    def get_left_child_population(self, index) -> int:
        """
        Return of the population of the left child.
        Hint:
        -----
        We need the position of the child in the StorageArray to extract the population from this position.
        """
        # TODO: implement me! (2 *index) + 1
        left_child_index: int = self.get_left_child_index(index)
        left_child: City = self.heapStorage[left_child_index]
        return left_child.population

    def get_right_child_population(self, index) -> int:
        """
        Return of the population of the right child.
        Hint:
        -----
        We need the position of the child in the StorageArray to extract the population from this position.
        """
        # TODO: implement me! (2 * index) +2
        right_child_index: int = self.get_right_child_index(index)
        right_child: City = self.heapStorage[right_child_index]
        return right_child.population

    def check_if_heap_is_full(self) -> bool:
        """
        Check if the heap has reached its maximum capacity. Return:
            True    = Full
            False   = Not full
        """
        # TODO: implement me!
        return self.maximumHeapCapacity == len(self.heapStorage)

    def swap_nodes(self, fst_node_index, sec_node_index) -> None:
        """
        Swap two nodes specified by their index.
        """
        # TODO: implement me!
        temp = self.heapStorage[fst_node_index]
        self.heapStorage[fst_node_index] = self.heapStorage[sec_node_index]
        self.heapStorage[sec_node_index] = temp

    def get_heap_data(self) -> List[City]:
        """
        Return the sorted List of City Objects
        ------
        List[City]:
        """
        return self.heapStorage

    def get_index(self, city: City):
        return self.heapStorage.index(city)
    