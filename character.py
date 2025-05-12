import pygame
import grid
import map

class character(map.field):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.bew = 5
        self.img = img

    def move(self, direction, fields):
        movement = 0
        if direction == 1:
            for field in fields:
                if (self.x, self.y - 1) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.y -= 1
        elif direction == 2:
            for field in fields:
                if (self.x, self.y + 1) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.y += 1
        elif direction == 3:
            for field in fields:
                if (self.x - 1, self.y) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.x -= 1
        elif direction == 4:
            for field in fields:
                if (self.x + 1, self.y) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.x += 1
