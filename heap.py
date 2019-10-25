class Heap:

    def __init__(self):
        self._elements = []

    def _swap(self, a, b):
        self._elements[a], self._elements[b] = self._elements[b], self._elements[a]


    @staticmethod
    def parent(i):
        return (i-1) // 2

    @staticmethod 
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2 * (i + 1)

    @property
    def elements(self):
        return self._elements

    @property
    def heap_size(self):
        return len(self._elements)

    def __getitem__(self, index):
        return self._elements[index]


class MinHeap(Heap):

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)

        if left < self.heap_size and self[left] < self[i]:
            smallest = left
        else:
            smallest = i

        if right < self.heap_size and self[right] < self[smallest]:
            smallest = right

        if smallest != i:
            self._swap(i, smallest)
            self.heapify(smallest)

    def extract_minimum(self):
        min = self.minimum
        self._elements[0] = self._elements.pop()
        self.heapify(0)
        return min
    
    def insert(self, item):
        self._elements.append(item)
        i = self.heap_size - 1

        while i >= 1 and self[self.parent(i)] > self[i]:
            self._swap(i, self.parent(i))
            i = self.parent(i)

    @property
    def minimum(self):
        return self[0]


class MaxHeap(Heap):

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)

        if left < self.heap_size and self[left] > self[i]:
            largest = left
        else:
            largest = i

        if right < self.heap_size and self[right] > self[largest]:
            largest = right

        if largest != i:
            self._swap(i, largest)
            self.heapify(largest)

    def extract_maximum(self):
        maximum = self.maximum
        self._elements[0] = self._elements.pop()
        self.heapify(0)
        return maximum

    def insert(self, item):
        self._elements.append(item)
        i = self.heap_size - 1

        while i >= 1 and self[self.parent(i)] < self[i]:
            self._swap(self.parent(i), i)
            i = self.parent(i)
    
    @property
    def maximum(self):
        return self[0]

    
class Median:

    def __init__(self):
        self.low = MaxHeap()
        self.high = MinHeap()

    def add_element(self, element):
        if not self.low.elements and not self.high.elements:
            self.low.insert(element)

        elif not self.high.elements :
            if element > self.low.maximum:
                self.high.insert(element)
            else:
                self.low.insert(element)
        else:
            if element < self.high.minimum:
                self.low.insert(element)
            else:
                self.high.insert(element)

        self._balance()

    def _balance(self):
        if self.low._elements and self.high._elements:
            if self.low.heap_size >= self.high.heap_size + 2:
                self.high.insert(self.low.extract_maximum())
            elif self.high.heap_size >= self.low.heap_size + 2:
                self.low.insert(self.high.extract_minimum())  
        elif self.low.heap_size == 2:
            self.high.insert(self.low.extract_maximum())
        elif self.high.heap_size == 2:
            self.low.insert(self.high.extract_minimum())

    def get_median(self):
        if self.low.heap_size > 0 and self.high.heap_size > 0:

            if (self.low.heap_size + self.high.heap_size) % 2 == 0:
                return self.low.maximum, self.high.minimum
            elif self.low.heap_size > self.high.heap_size:
                return self.low.maximum

            return self.high.minimum

        elif self.low.heap_size > 0:
            return self.low.maximum

        else:
            return self.high.minimum  

    
    def get_maxheap_elements(self):
        return self.low.elements

    def get_minheap_elements(self):
        return self.high.elements
 
if __name__ == "__main__":
    med = Median() 
    for i in reversed(range(11)):
        med.add_element(i)
        print(med.get_median())
        print(med.get_maxheap_elements(), med.get_minheap_elements())