
from LinearPriorityQueue import LinearPQ
from HeapPriorityQueue import HeapPQ
from LinearPriorityQueueDict import LinearPQDict
class TestLinearPQ:

    def test_insert_and_extract_min(self):
        pq = LinearPQDict()
        pq.insert1('A', 10)
        pq.insert1('B', 5)
        pq.insert1('C', 8)

        # Extract the minimum (should be 'B' with priority 5)
        node, priority = pq.extract_min()
        assert node == 'B'
        assert priority == 5

        # Extract the next minimum (should be 'C' with priority 8)
        node, priority = pq.extract_min()
        assert node == 'C'
        assert priority == 8

        # Extract the last element (should be 'A' with priority 10)
        node, priority = pq.extract_min()
        assert node == 'A'
        assert priority == 10

    def test_decrease_key(self):
        pq = LinearPQDict()
        pq.insert1('A', 10)
        pq.insert1('B', 5)
        pq.insert1('C', 8)

        # Decrease the key of 'A' to 2 (should become the minimum)
        pq.decrease_key('A', 2)

        # Extract the minimum (should now be 'A' with priority 2)
        node, priority = pq.extract_min()
        assert node == 'A'
        assert priority == 2

        # Extract the next minimum (should be 'B' with priority 5)
        node, priority = pq.extract_min()
        assert node == 'B'
        assert priority == 5

        # The last element should be 'C' with priority 8
        node, priority = pq.extract_min()
        assert node == 'C'
        assert priority == 8

    def test_insert_and_extract_single_element(self):
        pq = LinearPQ()
        pq.insert1('A', 100)

        # Extract the only element (should be 'A' with priority 100)
        node, priority = pq.extract_min()
        assert node == 'A'
        assert priority == 100

    def test_decrease_key_non_existent_node(self):
        pq = LinearPQDict()
        pq.insert1('A', 10)
        pq.insert1('B', 20)

        # Try to decrease the key of a node that doesn't exist ('C')
        pq.decrease_key('C', 5)

        # The queue should remain unchanged
        node, priority = pq.extract_min()
        assert node == 'A'
        assert priority == 10

    def test_decrease_key_with_multiple_updates(self):
        pq = LinearPQDict()
        pq.insert1('A', 10)
        pq.insert1('B', 20)
        pq.insert1('C', 15)

        # Decrease the key of 'B' to 5
        pq.decrease_key('B', 5)

        # Decrease the key of 'C' to 3 (this should become the minimum)
        pq.decrease_key('C', 3)

        # Extract the minimum (should now be 'C' with priority 3)
        node, priority = pq.extract_min()
        assert node == 'C'
        assert priority == 3

        # Extract the next minimum (should be 'B' with priority 5)
        node, priority = pq.extract_min()
        assert node == 'B'
        assert priority == 5

        # The last element should be 'A' with priority 10
        node, priority = pq.extract_min()
        assert node == 'A'
        assert priority == 10

def test_insert_and_extract_min():
        pq = HeapPQDict()
        pq.insert1('A', 10)
        pq.insert1('B', 5)
        pq.insert1('C', 8)

        # Extract the minimum (should be 'B' with priority 5)
        node, priority = pq.extract_min()
        assert node == 'B'
        assert priority == 5

        # Extract the next minimum (should be 'C' with priority 8)
        node, priority = pq.extract_min()
        assert node == 'C'
        assert priority == 8

        # Extract the last element (should be 'A' with priority 10)
        node, priority = pq.extract_min()
        assert node == 'A'
        assert priority == 10
        
# test_insert_and_extract_min()
