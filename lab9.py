#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:21:10 2024

@author: liutianyun
"""

import random

class Agent:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, grid):
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        dx, dy = random.choice(moves)
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] is None:
            grid[self.x][self.y] = None
            self.x, self.y = new_x, new_y
            grid[new_x][new_y] = self

class World:
    def __init__(self, width, height, num_agents):
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []
        for i in range(num_agents):
            while True:
                x, y = random.randint(0, width-1), random.randint(0, height-1)
                if self.grid[x][y] is None:
                    agent = Agent(f"Agent{i}", x, y)
                    self.grid[x][y] = agent
                    self.agents.append(agent)
                    break

    def simulate(self, steps):
        for _ in range(steps):
            for agent in self.agents:
                agent.move(self.grid)