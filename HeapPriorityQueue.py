class HeapPQ:
    def __init__(self):
        self.heap = []
        self.position_map = {}

    def insert1(self, node, priority):
        self.heap.append((node, priority))
        self.position_map[node] = len(self.heap) - 1
        self.bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if (len(self.heap) == 1):
            return self.heap.pop()
        min_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        del self.position_map[min_node[0]]
        if self.heap:
            self.position_map[self.heap[0][0]] = 0
            self.bubble_down()
        return min_node
    
    def decrease_key(self, node, new_priority):
        #update and bubble up
        index = self.position_map[node]
        self.heap[index] = (node, new_priority)
        self.bubble_up(index)

    def swap(self, index1, index2):
        self.position_map[self.heap[index1][0]] = index2
        self.position_map[self.heap[index2][0]] = index1

        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
     
    def bubble_up(self, index):
        while index > 0:
            parent = self.get_parent_index(index)
            if self.heap[index][1] < self.heap[parent][1]:
                self.swap(index, self.get_parent_index(index))
                index = parent
            else:
                break
            
    def bubble_down(self):
        index = 0
        size = len(self.heap)
        while index < size:
            left = self.get_left_child_index(index)
            right = self.get_right_child_index(index)
            smallest = index

            if left < size and self.heap[smallest][1] > self.heap[left][1]:
                smallest = left
            if right < size and self.heap[smallest][1] > self.heap[right][1]:
                smallest = right
            
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break
        

    def get_parent_index(self, index):
        if index <= 0:
            return None
        else:
            return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return index * 2 + 1

    def get_right_child_index(self, index):
        return index * 2 + 2

