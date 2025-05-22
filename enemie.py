import pygame
import grid
import heapq
import random
import sql
from field import field

class enemie(field):
    def __init__(self, x, y, ini, roomId, roomX, roomY, enemieId, data):
        self.x = x
        self.y = y
        self.roomId = roomId
        self.roomX = roomX
        self.roomY = roomY
        self.id = enemieId 

        db = sql.loadEnemie(self.id, data)

        self.maxBew = 3 #
        self.aktBew = self.maxBew
        self.img = None
        self.ini = ini
        self.dmg = db[3] #6 #
        self.health = db[1] #10 #
        self.maxHealth = self.health

    def loadImg(self, blockSize):
        path = ""
        match self.id:
            case 1:
                path = "Images/Enemies/kobold.png"
            case 2:
                path = "Images/Enemies/unicorn.png"
            
        self.img = grid.importImage(path, blockSize)

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def pathFinder(self, fields, cols, rows, charac):
        start = (self.y, self.x)
        goal = (charac.y, charac.x)

        grid = []

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            grid.append(row)

        for i in fields:
            if i.x == self.x and i.y == self.y:
                grid[i.y][i.x] = 0
            else:
                grid[i.y][i.x] = 1
        
        open_set = []
        heapq.heappush(open_set, (0 + self.heuristic(start, goal), 0, start))
        came_from = {}
        cost_so_far = {start: 0}
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while open_set:
            test, current_cost, current = heapq.heappop(open_set)
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                path = path[1:]
                path = path[:-1]
                if path != []:
                    path = path[0]
                    return path
                else:
                    return None
            
            for dx, dy in directions:
                next_node = (current[0] + dx, current[1] + dy)
                x, y = next_node
                if 0 <= x < rows and 0 <= y < cols and grid[int(x)][int(y)] != 1:
                    new_cost = cost_so_far[current] + 1
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + self.heuristic(next_node, goal)
                        heapq.heappush(open_set, (priority, new_cost, next_node))
                        came_from[next_node] = current
        return None

    def move(self, rod, charac):
        result = self.pathFinder(rod.field_list, rod.fild_leng, rod.fild_high, charac)

        if result:
            if self.aktBew > 0:
                if rod.wait == 0:
                    self.x = result[1]
                    self.y = result[0]
                    rod.wait = 1
                    self.aktBew -= 1
        else:
            self.aktBew = 0

        if (charac.x == self.x - 1 or charac.x == self.x + 1) and charac.y == self.y or (charac.y == self.y - 1 or charac.y == self.y + 1) and charac.x == self.x:
            self.aktBew = 0
            self.attack(charac, rod)

        if self.aktBew == 0:
            rod.aktIni += 1

    def drawHealthbar(self, SCREEN, blockSize):
        rec = pygame.Rect((grid.gridCordinat(self.x, self.y - 1, blockSize)), (blockSize, int(blockSize / 3)))
        rec.y += blockSize / 2
        pygame.draw.rect(SCREEN, (255,255,255), rec)

        recHealth = pygame.Rect((grid.gridCordinat(self.x, self.y - 1, blockSize)), (blockSize - 2, int(blockSize / 3) - 2))
        recHealth.x = rec.x + 1
        recHealth.y = rec.y + 1
        recHealth.width = recHealth.width / self.maxHealth * self.health
        pygame.draw.rect(SCREEN, (0,0,0,), recHealth)

    def attack(self, charac, rod):
        dmg = random.randint(1,self.dmg) - charac.shield
        if dmg > 0:
            charac.health -= dmg

        if charac.health <= 0:
            rod.end = 2
