class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Insert a value into the heap, maintaining the max-heap property."""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        """Remove and return the maximum value from the heap, maintaining the max-heap property."""
        if not self.heap:
            raise IndexError("Heap is empty.")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._heapify_down(0)
        return max_value

    def get_max(self):
        """Return the maximum value from the heap without removing it."""
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] > self.heap[largest]):
            largest = left_child_index

        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] > self.heap[largest]):
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example usage
if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(10) #inserting a number
    heap.insert(20) #inserting a number
    heap.insert(5) #inserting a number
    print(heap.get_max())  # Output: 20
    print(heap.delete())   # Output: 20
    print(heap.get_max())  # Output: 10
