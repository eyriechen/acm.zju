class City:
    city_size = 0
    city = []
    moves = []
    max_move = 0

    def __init__(self, city_size):
        self.city_size = city_size

    def input(self):
        self.city = []
        self.moves = []
        self.max_move = 0
        for i in range(0, self.city_size):
            row = []
            line = raw_input()
            for letter in line:
                if letter == '.':
                    row.append(0)
                else:
                    row.append(-1)
            self.city.append(row)

    def show(self):
        # for row in self.city:
        #     for cell in row:
        #         sys.stdout.write('\t' + str(cell))
        #     print
        print str(self.max_move)

    def mark_move(self):
        if len(self.moves) > self.max_move:
            self.max_move = len(self.moves)

    def place(self,i,j):
        self.moves.append([i, j])
        self.mark_move()
        self.city[i][j] = len(self.moves)
        for k in range(0, i):
            if self.city[k][j] == -1:
                break;
            if self.city[k][j] != 0:
                continue
            self.city[k][j] = len(self.moves)
        for k in range(i, self.city_size):
            if self.city[k][j] == -1:
                break;
            if self.city[k][j] != 0:
                continue
            self.city[k][j] = len(self.moves)
        for k in range(0, j):
            if self.city[i][k] == -1:
                break;
            if self.city[i][k] != 0:
                continue
            self.city[i][k] = len(self.moves)
        for k in range(j, self.city_size):
            if self.city[i][k] == -1:
                break;
            if self.city[i][k] != 0:
                continue
            self.city[i][k] = len(self.moves)

    def remove(self):
        for i in range(0, self.city_size):
            for j in range(0, self.city_size):
                if self.city[i][j] == len(self.moves):
                    self.city[i][j] = 0
        self.moves.pop()

    def next_move(self):
        for i in range(0, self.city_size):
            for j in range(0, self.city_size):
                if self.city[i][j] != 0:
                    continue
                self.place(i,j)
                self.next_move()
                self.remove()

while True:
    try:
        s = raw_input()
        size = int(s)
        if size == 0:
            exit(0)
        c = City(size)
        c.input()
        c.next_move()
        c.show()
    except EOFError:
        exit(0)