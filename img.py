import os
import string

import pygame
from pygame.constants import RLEACCEL

# blit an image, and blit an image with transparency

# util
TRANSPARENT_COLOR = (255, 0, 255)  # magenta is rendered as transparent
_image_library = {}
def get_image(img_path, use_alpha_key=0):
    global _image_library
    path = string.lower(img_path)
    cache_key = '#'.join((path,str(use_alpha_key)))
    image = _image_library.get(cache_key)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert()
        if use_alpha_key:
            image.set_colorkey(TRANSPARENT_COLOR, RLEACCEL) 
        _image_library[path] = image
    return image


# main
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((111, 111, 111))
    
    screen.blit(get_image('img.png'), (20, 20))
    screen.blit(get_image('img.png', 1), (100, 120))
    
    pygame.display.flip()
    clock.tick(60)
