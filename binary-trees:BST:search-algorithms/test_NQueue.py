import node as N
from NQueue import Queue

def test_queue_initialization():
    q = Queue()
    assert q.is_empty() == True, "Test Fail: Queue should be empty on initialization"
    assert q.size() == 0, "Test Fail: Queue size should be 0 on initialization"

def test_enqueue():
    q = Queue()
    q.enqueue(10)
    assert q.size() == 1, "Test Fail: Queue size should be 1 after one enqueue"
    q.enqueue(20)
    assert q.size() == 2, "Test Fail: Queue size should be 2 after two enqueues"

def test_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10, "Test Fail: Dequeue should return the first enqueued value"
    assert q.size() == 1, "Test Fail: Queue size should decrement to 1 after dequeue"

def test_peek():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.peek() == 10, "Test Fail: Peek should return the first enqueued value without removing it"
    assert q.size() == 2, "Test Fail: Queue size should remain unchanged after peek"

def test_is_empty():
    q = Queue()
    assert q.is_empty() == True, "Test Fail: is_empty() should return True for an empty queue"
    q.enqueue(10)
    assert q.is_empty() == False, "Test Fail: is_empty() should return False when queue is not empty"

if __name__ == "__main__":
    test_queue_initialization()
    test_enqueue()
    test_dequeue()
    test_peek()
    test_is_empty()
    print("All tests passed!")
