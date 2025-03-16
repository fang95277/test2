#---------------------#
# DO NOT MODIFY BEGIN #
#---------------------#

import logging

import util
from problems.q1a_problem import q1a_problem

def q1a_solver(problem: q1a_problem):
    astarData = astar_initialise(problem)
    num_expansions = 0
    terminate = False
    while not terminate:
        num_expansions += 1
        terminate, result = astar_loop_body(problem, astarData)
    print(f'Number of node expansions: {num_expansions}')
    return result

#-------------------#
# DO NOT MODIFY END #
#-------------------#

class AStarData:
    # YOUR CODE HERE
    def __init__(self):
        self.frontier = None
        self.visited = None

def astar_initialise(problem: q1a_problem):
    # YOUR CODE HERE
    astarData = AStarData()
    astarData.frontier = util.PriorityQueue()
    astarData.visited = set()
    startState = problem.getStartState()
    # 初始状态的动作序列为空，优先级为0
    astarData.frontier.push((startState, []), 0)
    return astarData

def astar_loop_body(problem: q1a_problem, astarData: AStarData):
    # YOUR CODE HERE
    # 如果优先队列为空，则搜索终止，返回空路径
    if astarData.frontier.isEmpty():
        return True, []
    
    # 从队列中弹出当前状态及其对应的动作序列
    state, actions = astarData.frontier.pop()
    
    # 如果该状态已被访问，则跳过（本次迭代不终止）
    if state in astarData.visited:
        return False, None
    
    # 标记该状态为已访问
    astarData.visited.add(state)
    
    # 若当前状态满足目标条件，则终止搜索，返回动作序列
    if problem.isGoalState(state):
        return True, actions
    
    # 获取目标位置（在 q1a_problem 中假设目标为第一个存在的食物点）
     foodGrid = problem.startingGameState.getFood()
    foodList = foodGrid.asList()
    goal = foodList[0] if foodList else None
    
    # 扩展当前状态的后继节点
    for successor, action, stepCost in problem.getSuccessors(state):
        if successor not in astarData.visited:
            new_actions = actions + [action]
            g = len(new_actions)  # 代价等于动作数（每步代价为1）
            h = astar_heuristic(successor, goal)
            f = g + h
            astarData.frontier.push((successor, new_actions), f)
    
    return False, None

def astar_heuristic(current, goal):
    # YOUR CODE HERE
    # 曼哈顿距离启发函数
    if goal is None:
        return 0
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])
