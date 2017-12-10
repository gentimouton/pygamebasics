""" Script adapted from Korruptor.
http://pygame.org/pcr/numpy_plasma/index.php
The plasma algo itself is pretty simple, just a sum of four cosine values
from a pre-calculated look-up table inserted into a surf buff. It's all 
pretty easy really. The comments explain my thinking... 
"""

import pygame as pg
import numpy as np

RES = np.array((320, 256))

cos_tab = 60 * np.cos(np.arange(256) * np.pi / 32) # precompute/cache cosines 

# Array of indexes to be used on our cos_tab. Could be variables I suppose. 
# Just easier to cut_n_paste! ;-)
pnt_tab = [0, 0, 0, 0]

            
# ------------------------------------------------------------------------------------
def update_sa(sa):
    """An Y by X loop of screen co-ords, summing the values of four cosine values 
    to produce a colour value that'll map to the previously set surface palette.
    """
    
    # Use working indices for the cosine table, save the real ones for later...
    t1 = pnt_tab[0]
    t2 = pnt_tab[1]
    # Loop for all Y screen coords...
    for y in range(0, RES[1] // 8):

        # Save the horizontal indices for later use...
        t3 = pnt_tab[2]
        t4 = pnt_tab[3]
        # Loop accross the screen...
        for x in range(0, RES[0] // 8):
            # Our colour value will equal the sum of four cos_table offsets. 
            # The preset surface palette comes in handy here! We just need to output the value...
            # We mod by 256 to prevent our index going out of range. (C would rely on 8bit byte ints and with no mod?)
            colour = cos_tab[t1 % 256] + cos_tab[t2 % 256] + cos_tab[t3 % 256] + cos_tab[t4 % 256]
                    
            # Arbitrary values, changing these will allow for zooming etc...
            t3 += 3
            t4 += 2
                        
            # Insert the calculated colour value into our working surfarray...
            sa[x][y] = colour

        # Arbitrary values again...
        t1 += 2
        t2 += 1
        
    # Arbitrary values to move along the cos_tab. Play around for something nice...
    # Don't think I need these boundary checkings, but just in case someone decides 
    # to run this code for a couple of weeks non-stop...
    if(pnt_tab[0] < 256): 
        pnt_tab[0] += 1
    else:
        pnt_tab[0] = 1
        
    if(pnt_tab[1] < 256):
        pnt_tab[1] += 2
    else:
        pnt_tab[1] = 2
        
    if(pnt_tab[2] < 256):
        pnt_tab[2] += 3
    else:
        pnt_tab[2] = 3
        
    if(pnt_tab[3] < 256):
        pnt_tab[3] += 4
    else:
        pnt_tab[3] = 4


# ------------------------------------------------------------------------------------
def make_cmap():
    """ Create something trippy... Based on Pete's cmap creator, 
    and without doubt the thing that took the longest... 
    Aaaargh! Decent palettes are hard to find...
    """
    cmap = np.zeros((256, 3))
    
    # We're trying to compress as large a range of colours 
    # into an 8bit palette as possible, so we go for a typical RGB spread.
    # A larger 2 x 2 colour range over 128 indices also works well...
    for i in range(0, 64):
        cmap[i][0] = 255
        cmap[i][1] = i * 4
        cmap[i][2] = 255 - (i * 4)
        
        cmap[i + 64][0] = 255 - (i * 4)
        cmap[i + 64][1] = 255 
        cmap[i + 64][2] = (i * 4)
            
        cmap[i + 128][0] = 0     
        cmap[i + 128][1] = 255 - (i * 4)
        cmap[i + 128][2] = 255
     
        cmap[i + 192][0] = i * 4        
        cmap[i + 192][1] = 0  
        cmap[i + 192][2] = 255    
        
    return cmap

    

def main():
    pg.init()
    screen = pg.display.set_mode(RES, 0, 8) # 8-bit display

    sa = np.zeros(RES // 8) # surfarray we'll repeatedly blit  
    surf = pg.Surface((RES[0] / 8, RES[1] / 8), 0, 8)

    # setup screen palette, and port it to our working surfarray
    cmap = make_cmap()
    screen.set_palette(cmap)
    surf.set_palette(cmap)

    while 1:
        for e in pg.event.get():
            if e.type in (pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN):
                return
         
        update_sa(sa)
        
        # blit surfarray to screen
        pg.surfarray.blit_array(surf, sa)
        s2 = pg.transform.scale(surf, screen.get_size()) # TODO: not efficient?
        screen.blit(s2, (0, 0))
        
        pg.display.flip()
        pg.time.delay(20)


if __name__ == '__main__': 
    main()
