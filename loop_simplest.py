import pygame
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE


pygame.init()
game_over = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        if event.type == KEYDOWN:
            key = event.key
            if key == K_ESCAPE:
                game_over = True        
    pygame.draw.rect(screen, (0, 128, 255), (30, 30, 60, 60))
    pygame.display.flip()
    clock.tick(60)
