""" Demo showing static and moving hollow squares in different layers.
Only draws areas of the screen that changed.
"""
from random import randint

import pygame as pg


_img_cache = {} 
def make_squared_hole(color):
    """ make a 50x50 surface with a 30x30 hole in it. Cache it if possible. """
    if color in _img_cache:
        return _img_cache[color]
    surf = pg.Surface((50, 50))
    surf.fill(color)
    surf.fill((255, 0, 255), (10, 10, 30, 30))
    # Run-length encoding is good for img with many of the same pixels in a row.
    # Use magenta as transparent color key.
    surf.set_colorkey((255, 0, 255), pg.RLEACCEL)
    surf.convert()  # fit to screen pixel format
    _img_cache[color] = surf
    return surf
    

class BasicSpr(pg.sprite.DirtySprite):
    def __init__(self, w, h, color, layer=0):
        pg.sprite.DirtySprite.__init__(self)
        self.image = make_squared_hole(color)
        self.layer = layer
        self.rect = self.image.get_rect()
        self.rect.topleft = randint(0, w - self.rect.w), randint(0, h - self.rect.h)
        
class MovingSpr(BasicSpr):
    def __init__(self, w, h, color, layer):
        BasicSpr.__init__(self, w, h, color, layer)
        self.vel = [randint(-1, 1), randint(-1, 1)]
        self.vel = [1, 1] if self.vel == [0, 0] else self.vel  # prevent static
        self.dirty = 1  # alternative: set to 2 if always moving

    def update(self, w, h):
        r = self.rect
        vx, vy = self.vel
        if r.right + vx > w or r.left + vx < 0:
            self.vel[0] = -self.vel[0]
        if r.bottom + vy > h or r.top + vy < 0:
            self.vel[1] = -self.vel[1]
        self.rect.move_ip(self.vel[0], self.vel[1])
        self.dirty = 1  # redraw me
        

def main():
    pg.display.init()
    w, h = (800, 600)
    screen = pg.display.set_mode((w, h))
    # make background
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((222, 111, 111))
    # create sprites
    sprites = pg.sprite.LayeredDirty()
    for _ in range(20):
        sprites.add(BasicSpr(w, h, (111, 55, 55)))
    for _ in range(10):
        sprites.add(MovingSpr(w, h, (111, 111, 111), 1))
    for _ in range(10):
        sprites.add(MovingSpr(w, h, (222, 222, 111), 2))
    
    clock = pg.time.Clock()
    while not pg.event.peek([pg.QUIT, pg.KEYDOWN]):
        # sprites.clear(screen, bg)  # draw bg over sprites. Use if draw has no bg
        sprites.update(w, h)  # update game logic. Can pass any *args
        dirty_rects = sprites.draw(screen, bg)  # draw and track changed areas
        # dirty_rects dont always map exactly to the sprites. For example, 
        # when 2 rects collide, a single bounding rect is returned instead of the 2. 
        pg.display.update(dirty_rects)  # flip only changed areas 
        pg.display.set_caption('%.1f fps' % clock.get_fps())
        clock.tick(60)

if __name__ == "__main__":
    main()
