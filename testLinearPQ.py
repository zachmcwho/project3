
from LinearPriorityQueueDict import LinearPQDict

def test_decrease_key():
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

test_decrease_key()