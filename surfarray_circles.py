from random import randint

import numpy as np
import pygame as pg

# fix of http://pygame.org/pcr/numpy_circles/index.php 

def make_circle(radius, color):
    """ returns surface with a disk of radius, filled with color """
    
    # prepare surface and color
    # option A: same surface depth as screen, ie probably 32 bits
    surf = pg.Surface((radius * 2, radius * 2))
    mapped_color = pg.display.get_surface().map_rgb(color)
    # option B: use 8-bit palette
    # surf = pg.Surface((radius * 2, radius * 2), 0, 8)
    # surf.set_palette(((0, 0, 0), color)) # palette of {0: black, 1: color}
    # mapped_color = surf.map_rgb(color) # 1
    
    # compute x2+y2 for each pixel
    d = np.abs(np.arange(radius * 2) - (radius - 0.5)).astype(np.int32) ** 2  
    sa = d[np.newaxis, :] + d[:, np.newaxis]
    
    # mask: set pixels outside circle to black, inside circle to color
    # option 1: ufunc https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs
    sa = np.less(sa, radius ** 2).astype(np.int32) * mapped_color
    # option 2: vectorize (slower than ufunc) https://stackoverflow.com/a/6824389
    # sa = np.vectorize(lambda x: mapped_color if x <= radius **2 else 0)(sa)
    
    # blit array and set transparency
    pg.surfarray.blit_array(surf, sa)
    surf.set_colorkey(0, pg.RLEACCEL)  # set black as transparent
    return surf

def make_square(radius, color):
    """ returns surface entirely filled with color. Using numpy array. """
    sa = np.zeros((radius * 2, radius * 2, 3), np.int32)
    sa[:] = color
    surf = pg.Surface((radius * 2, radius * 2))
    # alternative using 8-bit palette
    # surf = pg.Surface((radius * 2, radius * 2), 0, 8)  # initialized with zeros
    # surf.set_palette((color, (0, 0, 0)))  # replace zeros by color
    pg.surfarray.blit_array(surf, sa)
    return surf

if __name__ == '__main__':
    pg.init()
    res = (400, 300)
    screen = pg.display.set_mode(res)
    while not pg.event.peek([pg.QUIT, pg.KEYDOWN]):
        radius = randint(10, 20)
        pos = randint(0, res[0]), randint(0, res[1])
        color = randint(20, 200), randint(20, 200), randint(20, 200)
        surf = make_circle(radius, color)
        screen.blit(surf, pos)     
        pg.display.update((pos, (radius * 2, radius * 2)))
        pg.time.delay(50)
