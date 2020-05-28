class SolvingSoLE:
    def __init__(self, matrix, e, max_it):
        self.e = e
        self.matrix = matrix
        self.max_it = max_it
        self.answer = []
        self.error = []
        self.it = 0

    def check_sufficient_condition(self):
        visited = [False] * len(self.matrix.values)
        rows = [0] * len(self.matrix.values)
        self.transform_to_dominant(0, visited, rows)
        return not False in visited

    def transform_to_dominant(self, r, visited, rows):
        if r == self.matrix.n:
            new_matrix = []
            for i in range(len(rows)):
                new_matrix.append(self.matrix.values[rows[i]])
            self.matrix.values = new_matrix
        else:
            for i in range(self.matrix.n):
                if visited[i]:
                    continue
                sum = 0
                for j in range(self.matrix.n):
                    sum += abs(self.matrix.values[i][j])
                if 2 * abs(self.matrix.values[i][r]) > sum:
                    visited[i] = True
                    rows[r] = i
                    self.transform_to_dominant(r + 1, visited, rows)
                else:
                    visited[i] = False

    def set_e(self, e):
        self.e = e

    def set_max_it(self, max_it):
        self.max_it = max_it

    def set_error(self, previous):
        for i in range(len(self.answer)):
            self.error.append(self.answer[i] - previous[i])

    def simple_iteration_method(self):
        check = self.check_sufficient_condition()
        if not check:
            return False
        else:
            previous = [0] * self.matrix.n
            self.answer = [0] * self.matrix.n
            stop = False
            self.it = 0
            while not stop:
                self.it += 1
                for i in range(self.matrix.n):
                    sum = self.matrix.values[i][self.matrix.n]
                    for j in range(self.matrix.n):
                        if not (j == i):
                            sum -= self.matrix.values[i][j] * previous[j]
                    self.answer[i] = sum / self.matrix.values[i][i]
                max = 0
                for i in range(self.matrix.n):
                    if abs(self.answer[i] - previous[i]) >= max:
                        max = abs(self.answer[i] - previous[i])
                if (max <= self.e) or (self.it > self.max_it):
                    self.set_error(previous)
                    stop = True
                for i in range(len(previous)):
                    previous[i] = self.answer[i]
            return True
