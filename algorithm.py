from collections import defaultdict

MAX_ITERATION = 100000000

class MDP:

    def __init__(self, grid, gamma, noise):
        self.gamma = gamma
        self.grid = grid 
        self.m = len(grid)
        self.n = len(grid[0])
        self.noise = noise
        self.states = self.getStatesFromGrid(grid)
        self.CONVERGE_VALUE = 0.00001

    def transition(self, i, j, direction):
        deltas = [[1, 0], [0, -1], [-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 1]]

        state = self.states[(i, j)]
        if not state: return None

        res = []
        for d in deltas[direction:direction + 3]:
            ni, nj = i + d[0], j + d[1]
            if ni == -1: ni = 0
            if ni == self.m: ni = self.m - 1
            if nj == -1: nj = 0
            if nj == self.n: nj = self.n - 1 
            res.append(self.states[(ni, nj)])

        return res

    def qState(self, i, j, direction):
        possibleState = self.transition(i, j, direction)

        tt = 0
        for (p, v) in zip([self.gamma * state[3] + self.reward(state[0], state[1]) for state in possibleState], self.noise):
            tt += p * v
        return tt

    def reward(self, i, j):
        return 0

    def iteraltion(self, directions, times):

        while times > 0:
            s1 = self.sum()
            for i in range(self.m):
                for j in range(self.n):
                    if self.isTerminal(i, j):
                        continue 

                    if not directions:
                        d = self.states[(i, j)][2]
                        qstate = self.qState(i, j, d)
                        self.states[(i, j)] = [i, j, d, qstate]
                    else:
                        qstates = [self.qState(i, j, d) for d in directions]
                        value = max(qstates)
                        d = qstates.index(value)
                        self.states[(i, j)] = [i, j, d, value]
            s2 = self.sum()

            if s2 - s1 < self.CONVERGE_VALUE:
                break

            times -= 1
        return times

    def value_iteration(self):
        t = MAX_ITERATION - self.iteraltion(range(4), MAX_ITERATION)

        print("Value Iteration: ", t)
        self.display()

    def policy_iteration(self):

        t = 0
        while True:
            s1 = self.sum()

            t += MAX_ITERATION - self.iteraltion(None, MAX_ITERATION)
            t += 1 - self.iteraltion(range(4), 1)

            s2 = self.sum()
            if s2 - s1 < self.CONVERGE_VALUE:
                break

        print("Policy Iteration: ", t)
        self.display()

    def display(self):
        for i in range(self.m):
            print(["%1.2f" % self.states[(i, j)][3] for j in range(self.n)])
        print()

    def isTerminal(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n:
            return self.grid[i][j] != "X"
        else:
            return False
    
    def sum(self):
        return sum([self.states[(i, j)][3] for i in range(self.m) for j in range(self.n)])

    def getStatesFromGrid(self, grid):
        states = {}

        for i in range(0, self.m):
            for j in range(0, self.n):
                # row col direction value, qvalues
                if not self.isTerminal(i, j): 
                    states[(i, j)] = [i, j, 0, 0, 0, 0, 0, 0]
                else:
                    states[(i, j)] = [i, j, 0, int(self.grid[i][j]), 0, 0, 0, 0]

        return states