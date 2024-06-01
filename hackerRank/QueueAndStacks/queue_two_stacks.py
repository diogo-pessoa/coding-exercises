import sys

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue.pop(0)

    def next_in_queue(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue[0]


def process_queries(queries):
    queue = Queue()
    for query in queries:
        if query[0] == 1:
            queue.enqueue(query[1])
        elif query[0] == 2:
            queue.dequeue()
        elif query[0] == 3:
            print(queue.next_in_queue())


if __name__ == '__main__':
    queries = []
    for line in sys.stdin:
        queries.append(list(map(int, line.strip().split())))
    process_queries(queries)