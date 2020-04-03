from algorithm import MDP

grid0 = [
    ["X", "X", "X", "1"],
    ["X", "0", "X", "-1"],
    ["X", "X", "X", "X"],
]

grid1 = [
["X","X","X","1","X","X","X"],
["X","X","X","-1","X","1","X"],
["-1","X","X","-1","X","4","X"],
["X","1","X","-1","X","1","X"],
["X","100","X","-100","X","3","X"],
["X","2","X","-1","X","3","X"],
["0","X","X","-1","X","1","X"]
]

grid2 = [
["X","X","X","1","X","X"],
["X","X","X","-1","X","1"],
["-1","X","X","-1","X","4"],
["X","1","X","-1","X","1"],
["X","2","X","-1","X","3"],
["0","X","X","-1","X","1"]
]

def wrap(grid):
    for row in grid:
        row.insert(0, 0)
        row.append(0)
    return grid


if __name__ == "__main__":

    mdp = MDP(grid1, 0.9, [0.1, 0.8, 0.1])
    mdp.value_iteration()
    mdp2 = MDP(grid1, 0.9, [0.1, 0.8, 0.1])
    mdp2.policy_iteration()

    mdp3 = MDP(grid2, 0.8, [0.2, 0.5, 0.2, 0.1])
    mdp3.value_iteration()
    mdp4 = MDP(grid2, 0.8, [0.2, 0.5, 0.2, 0.1])
    mdp4.policy_iteration()

