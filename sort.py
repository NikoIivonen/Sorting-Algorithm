import pygame
import sys
from random import randrange, randint
from math import floor

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()


def get_neighs(bar):
    right = None
    left = None

    for b in bar_list:
        if b.x - bar.x == -xdiff:
            left = b
            continue
        if b.x - bar.x == xdiff:
            right = b

    return left, right


class Bar:
    def __init__(self, x, height):
        self.x = x
        self.y = 700-height
        self.height = height
        self.bar = pygame.Rect(self.x, self.y, 15, self.height)
        self.r = randrange(0, 180)
        self.g = randrange(0, 180)
        self.b = randrange(0, 180)

    def draw(self):
        self.bar = pygame.Rect(self.x, self.y, xdiff - 1, self.height)
        pygame.draw.rect(screen, (self.r, self.g, self.b), self.bar)

    def move(self):
        left, right = get_neighs(self)

        if left is not None and left.height > self.height:
            self.x, left.x = left.x, self.x
            return 1
        elif right is not None and right.height < self.height:
            self.x, right.x = right.x, self.x
            return 1

        return 0


bars = 200
xdiff = floor(1000/bars)
hdiff = 700/bars*0.95

xs = [i*xdiff for i in range(bars)]

bar_list = []

for i in range(bars):
    ri = randint(0, len(xs)-1)
    bar_list.append(Bar(xs[ri], 10+i*hdiff))
    del xs[ri]


while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((230, 230, 230))

    for bar in bar_list:
        bar.draw()

    for bar in bar_list:
        if bar.move() == 1:
            pass

    pygame.display.flip()
    clock.tick(20)

