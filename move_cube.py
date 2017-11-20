import pygame


# http://www.nerdparadise.com/programming/pygame/part1
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0: y -= 3
    if pressed[pygame.K_DOWN] and y < 300-60: y += 3
    if pressed[pygame.K_LEFT] and x > 0: x -= 3
    if pressed[pygame.K_RIGHT] and x < 400-60: x += 3
    
    screen.fill((0, 0, 0))
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, (x, y, 60, 60))
    
    pygame.display.flip()
    clock.tick(60)
