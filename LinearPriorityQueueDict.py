import math

class LinearPQDict:
    def __init__(self):
        self.dict = {}

    def insert1(self, node, priority):
        self.dict[node] = priority
    
    def extract_min(self):
        if not self.dict:
            return None
        
        min = math.inf
        min_node = ""
        
        for node, priority in self.dict.items():
            if priority < min:
                min = priority
                min_node = node

        if min_node == "":
            return None
        
        del self.dict[min_node]

        return (min_node, min)

    def decrease_key(self, node, new_priority):
        self.dict[node] = new_priority