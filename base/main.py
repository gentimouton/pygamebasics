import pygame
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE

pygame.init()

FPS = 60

if __name__ == "__main__":
    
    game_over = False
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500,500))
    
    while not game_over:
        # process inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == KEYDOWN:
                key = event.key
                if key == K_ESCAPE:
                    game_over = True
                
        clock.tick(FPS)
