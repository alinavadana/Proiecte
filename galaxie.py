import pygame
import random
import math

# Setări ecran
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aurora Boreală")
clock = pygame.time.Clock()

# Culori
BACKGROUND_COLOR = (5, 5, 20)
AURORA_COLORS = [
    (120, 255, 200),
    (100, 180, 255),
    (200, 120, 255),
    (180, 255, 180)
]

# Clasa pentru benzi de auroră
class AuroraRibbon:
    def __init__(self, y_offset, color):
        self.y_offset = y_offset
        self.color = color
        self.phase = random.uniform(0, math.pi * 2)
        self.amplitude = random.uniform(40, 100)
        self.speed = random.uniform(0.002, 0.004)
        self.points = []

    def update(self, time):
        self.points = []
        for x in range(0, WIDTH, 10):
            y = self.y_offset + math.sin(time * self.speed + x * 0.01 + self.phase) * self.amplitude
            self.points.append((x, y))

    def draw(self, surface):
        if len(self.points) < 2:
            return
        aurora_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for i in range(10):
            offset = i * 2
            alpha = max(0, 80 - i * 8)
            color = (*self.color, alpha)
            pygame.draw.lines(aurora_surface, color, False, [(x, y - offset) for (x, y) in self.points], 3)
        surface.blit(aurora_surface, (0, 0))

# Inițializare aurorae
auroras = [
    AuroraRibbon(HEIGHT // 2 + i * 30, random.choice(AURORA_COLORS)) for i in range(-2, 3)
]

# Main loop
running = True
t = 0
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizează și desenează fiecare auroră
    for aurora in auroras:
        aurora.update(t)
        aurora.draw(screen)

    t += 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
