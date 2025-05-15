import pygame
import grid
import map

class character(map.field):
    def __init__(self, x, y, img, ini):
        self.x = x
        self.y = y
        self.maxBew = 5
        self.aktBew = 5
        self.img = img
        self.ini = ini
        self.direction = 0

    def move(self, fields):
        movement = 0
        self.aktBew -= 1
        if self.direction == 1:
            for field in fields:
                if (self.x, self.y - 1) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.y -= 1
        elif self.direction == 2:
            for field in fields:
                if (self.x, self.y + 1) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.y += 1
        elif self.direction == 3:
            for field in fields:
                if (self.x - 1, self.y) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.x -= 1
        elif self.direction == 4:
            for field in fields:
                if (self.x + 1, self.y) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.x += 1
