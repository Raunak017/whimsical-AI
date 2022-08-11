import numpy as np
from collections import deque



def dfs(initial_state):
    start_node = Node(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()

    frontier = deque()
    frontier.append(start_node)
    explored = []
    killed = []

    print("The starting node is \nDepth=%d\n" % start_node.depth)
    print(str(start_node.state))
    while frontier:
        node = frontier.pop()
        print("\nThe node selected to expand is\nDepth=" + str(node.depth) + "\n" + str(node.state) + "\n")
        explored.append(node.state)

        if node.parent:
            diff = np.subtract(node.parent.state, node.state)
            if node.parent.state[2] == 0:
                diff[0], diff[1] = -diff[0], -diff[1]
        children = node.generate_child()
        if not node.is_killed():
            print("The children nodes of this node are", end="")
            for child in children:
                if child.state not in explored:
                    print("\nDepth=%d" % child.depth)
                    print(str(child.state))
                    if child.goal_test():
                        print("which is the goal state\n")
                        diff = np.subtract(child.parent.state, child.state)
                        if child.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]


                        return child.find_solution()
                    if child.is_valid():
                        frontier.append(child)
                        explored.append(child.state)

        else:
            print("This node is killed")
            killed.append("\"" + str(node.state) + "\"")
    return

class Node:
    goal_state = [0, 0, 0]
    num_of_instances = 0

    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        Node.num_of_instances += 1

    def __str__(self):
        return str(self.state)

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    def is_valid(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        boat = self.state[2]
        if missionaries < 0 or missionaries > 3:
            return False
        if cannibals < 0 or cannibals > 3:
            return False
        if boat > 1 or boat < 0:
            return False
        return True

    def is_killed(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        if cannibals > missionaries > 0:
            return True
        # Check for the other side
        if cannibals < missionaries < 3:
            return True

    def generate_child(self):
        children = []
        depth = self.depth + 1
        op = -1  # Subtract
        if self.state[2] == 0:
            op = 1  # Add
        for x in range(3):
            for y in range(3):
                # by_move = "Move %s missionaries and %s cannibals %s" % (x, y, boat_move)
                new_state = self.state.copy()
                new_state[0], new_state[1], new_state[2] = new_state[0] + op * x, new_state[1] + op * y, new_state[
                    2] + op * 1
                action = [x, y, op]
                new_node = Node(new_state, self, action, depth)
                if 1 <= x + y <= 2:
                    children.append(new_node)
        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        #solution = solution[:-1]
        solution.reverse()
        return solution


initial_state = [3, 3, 1]

Node.num_of_instances = 0

print("**************************************************************")
print("**************************************************************")

print("DFS Search Space and Solution")

print("**************************************************************")
print("**************************************************************")

solution = dfs(initial_state)
print('Solution:', solution)
print('Search Space:', Node.num_of_instances)