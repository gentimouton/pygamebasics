from math import sqrt
import pygame

# draw hexagons in (x,y) board coords

def draw_hex(screen, x, y, w, h, color):
    """ x,y are Offset coords of hex cell, in game space """
    # get pixel coords of center
    if y % 2 == 0:  # even rows
        xc = x * w + w / 2 
        yc = y * h * 3 / 2 + h / 2
    else:  # odd rows are shifted right
        xc = x * w + w
        yc = y * h * 3 / 2 - h / 4 
    
    corners = [(xc, yc - h / 2),
               (xc + w / 2, yc - h / 4),
               (xc + w / 2, yc + h / 4),
               (xc, yc + h / 2),
               (xc - w / 2, yc + h / 4),
               (xc - w / 2, yc - h / 4)                   
               ]
    pygame.draw.polygon(screen, color, corners)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False
    clock = pygame.time.Clock()
    
    while not done:
        # process inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
    
        # draw
        screen.fill((111, 111, 111))
        size = 50
        w, h = sqrt(3) * size, 2 * size
        draw_hex(screen, 0, 0, w, h, (0, 0, 222))
        draw_hex(screen, 0, 1, w, h, (0, 222, 0))
        draw_hex(screen, 1, 0, w, h, (222, 0, 0))
        draw_hex(screen, 1, 1, w, h, (222, 222, 0))
        pygame.display.flip()
        clock.tick(60)
    
    # exit
    pygame.quit()

        
if __name__ == "__main__":
    main()
