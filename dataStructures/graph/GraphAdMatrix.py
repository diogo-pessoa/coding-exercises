class GraphAdMatrix:
    def __init__(self, num_cannon_events):
        self.num_cannon_events = num_cannon_events
        # Initialise the matrix with a list comprehension to create a 2D list(Matrix)
        # of zeroes
        self.multiverse = [[0 for _ in range(num_cannon_events)] for _ in
                           range(num_cannon_events)]

    def add_connection(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.multiverse[v1][v2] = 1
        self.multiverse[v2][v1] = 1

    def remove_connection(self, v1, v2):
        if self.multiverse[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.multiverse[v1][v2] = 0
        self.multiverse[v2][v1] = 0

    def add_cannon_event(self, v):
        if v >= self.num_cannon_events:
            print("Vertex %d is out of bounds" % v)
            return
        self.multiverse[v][v] = 1

    def remove_cannon_event(self, v1, v2):
        if self.multiverse[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.multiverse[v1][v2] = 0
        self.multiverse[v2][v1] = 0

    def show_multiverse(self):
        for row in self.multiverse:
            print(row)
