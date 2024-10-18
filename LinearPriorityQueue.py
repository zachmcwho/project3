class LinearPQ:
    def __init__(self):
        self.queue = [] #stores priority, node tuples
        self.position_map = {} #stores node -> index in queue

    def insert1(self, node, priority):
        self.queue.append((node, priority))
        self.position_map[node] = len(self.queue) - 1
          
    def extract_min(self):
        if not self.queue:
            return None
        
        min_index = 0
        
        for i in range(1, len(self.queue)):
            if (self.queue[i][1] < self.queue[min_index][1]):
                min_index = i
        
        node, priority = self.queue[min_index]
        last_element = self.queue.pop()

        if (min_index < len(self.queue)):
            self.queue[min_index] = last_element
            self.position_map[last_element[0]] = min_index
            
        if node in self.position_map:
            del self.position_map[node]

        return node, priority
        
    def decrease_key(self, node, new_priority):
        if node not in self.position_map:
            return
        
        index = self.position_map[node]
        self.queue[index] = (node, new_priority)

        