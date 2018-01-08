""" Draw Mandelbrot set with pygame.
Update of 2001 code at http://pygame.org/pcr/mandelbrot/index.php
See also https://rosettacode.org/wiki/Mandelbrot_set#Python
Fractals pics: https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension
"""


import numpy as np
import pygame as pg
import time
 
def slow_mandelbrot(LowX, HighX, LowY, HighY, stepx, stepy, maxiter):
    xx = np.arange(LowX, HighX, (HighX - LowX) / stepx)
    yy = np.arange(HighY, LowY, (LowY - HighY) / stepy) * 1j
    c = np.ravel(xx + yy[:, np.newaxis])
    z = np.zeros(c.shape, np.complex128)
    output = np.zeros(c.shape) + 1
    for iteration in range(maxiter):
        z = z * z + c
        finished = np.greater(abs(z), 2.0)
        c = np.where(finished, 0 + 0j, c)
        z = np.where(finished, 0 + 0j, z)
        output = np.where(finished, iteration, output)
    output.shape = (stepy, stepx)
    return np.transpose(output)



def fast_mandelbrot(LowX, HighX, LowY, HighY, stepx, stepy, maxiter):
    """creates a numeric array of the mandelbrot function. 
    ~2x faster version, but overflows for maxiter>10. """
    if maxiter > 10: maxiter = 10  # overflows at 11
    xx = np.arange(LowX, HighX, (HighX - LowX) / stepx)
    yy = np.arange(HighY, LowY, (LowY - HighY) / stepy) * 1.0j
    # sometimes these arrays are too big by one element???
    xx = xx[:stepx]
    yy = yy[:stepy]
    c = np.ravel(xx + yy[:, np.newaxis])
    z = np.zeros(c.shape, np.complex128)
    output = np.zeros(c.shape) + 1
    for _ in range(maxiter):
        np.multiply(z, z, z)
        np.add(z, c, z)
        np.add(output, np.greater(abs(z), 2.0), output)
    output.shape = (stepy, stepx)
    return np.transpose(output)


def draw_mandelbrot(screen, l_val, r_val, t_val, b_val, res, iterations, 
                    mfunc=slow_mandelbrot):
    t = time.time()
    mand = mfunc(l_val, r_val, t_val, b_val, res[0], res[1], iterations)
    np.multiply(mand, 32, mand)  # this just chooses 'prettier' color index values
    screen.fill((0, 0, 0))
    pg.surfarray.blit_array(screen, mand)
    txt = 'n=%d, t=%dms' % (iterations, round((time.time() - t)*1000))
    font = pg.font.Font(None, 40)
    txt_surf = font.render(txt, True, (0, 128, 0))
    txt_surf.convert()
    screen.blit(txt_surf , (0, 0))
    pg.display.flip()


def main():
    res = 800, 600
    max_iterations = 20
    iterations = max_iterations
    pg.init()
    screen = pg.display.set_mode(res, 0)
    clock = pg.time.Clock()
    
    l_val, r_val = -2.1, 0.7
    t_val, b_val = -1.2, 1.2
#     l_inc, r_inc = .03, -.02
#     t_inc, b_inc = .03, -.005  
    
    while 1:
        if pg.event.peek([pg.QUIT, pg.KEYDOWN]): break
        iterations = iterations % max_iterations + 1
        draw_mandelbrot(screen, l_val, r_val, t_val, b_val, res, iterations)
#         l_val += l_inc
#         r_val += r_inc
#         t_val += t_inc
#         b_val += b_inc
        clock.tick(4)


if __name__ == '__main__': 
    main()

