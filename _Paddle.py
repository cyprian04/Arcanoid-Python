import pygame

class Paddle():
    def __init__(self, screen, pos_x, pos_y, width, height):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.paddle_color = (0,200,0)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.paddle_color, (self.pos_x, self.pos_y, self.width, self.height))

    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.pos_x = min(700 - self.width, self.pos_x + 8)
        elif keys[pygame.K_LEFT]:
            self.pos_x = max(0, self.pos_x - 8)
