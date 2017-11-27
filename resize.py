import pygame


# adapted from https://stackoverflow.com/a/20002295
pygame.init()
res0 = 500, 500
flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
img0 = pygame.image.load("img.png")
s0 = (200, 200)  # img size in resolution res0
p0 = (50, 20)  # position in res0


def refresh(res):
    screen = pygame.display.set_mode(res, flags) 
    s = s0[0] * res[0] // res0[0], s0[1] * res[1] // res0[1]
    p = p0[0] * res[0] // res0[0], p0[1] * res[1] // res0[1]
    screen.blit(pygame.transform.scale(img0, s), p)
    pygame.display.flip()

refresh(res0) # will fire a pygame.VIDEORESIZE event
    
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.VIDEORESIZE: 
        res = event.dict['size']
        refresh(res)
