import pickle

import pygame


# 3 ways to process keyboard:
# 1) for event in pygame.event.get():
# 2) pressed_keys = pygame.key.get_pressed()
# 3) ctrl_held = pygame.key.get_mods() & pygame.KMOD_CTRL # for modifiers
# adapted from http://www.nerdparadise.com/programming/pygame/part1
# more details: https://wiki.python.org/moin/UsingPickle
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

class State():
    is_blue = True
    x = 30
    y = 30


filename = 'save.pickle'
try:
    state = pickle.load(open(filename, 'rb'))
except:
    state = State()

clock = pygame.time.Clock()
while not done:
    ctrl_held = pygame.key.get_mods() & pygame.KMOD_CTRL
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            state.is_blue = not state.is_blue
        # save state with ctrl-s
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and ctrl_held:
            try:
                pickle.dump(state, open(filename, 'wb'))
                print('Saved state')
            except:
                print('Error saving state')
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and state.y > 0: state.y -= 3
    if pressed_keys[pygame.K_DOWN] and state.y < 300 - 60: state.y += 3
    if pressed_keys[pygame.K_LEFT] and state.x > 0: state.x -= 3
    if pressed_keys[pygame.K_RIGHT] and state.x < 400 - 60: state.x += 3
    
    screen.fill((0, 0, 0))
    if state.is_blue: 
        color = (0, 128, 255)
    else: 
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, (state.x, state.y, 60, 60))
    
    pygame.display.flip()
    clock.tick(60)
