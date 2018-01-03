import pygame as pg


# constants.py
BTN_SUBMIT = 'submit'
BTN_CANCEL = 'cancel'


# scenes.py
SCN_WORLD = 'world scene'
SCN_MENU = 'menu scene'
SCN_QUIT = 'quit scene'  # not a real scene, but a convenient value to quit

class Scene():
    def resume(self, **kwargs):
        """ Called by scene manager. kwargs are passed by previous scene """ 
        pass
    def tick(self, buttons):
        """ Based on buttons being pressed, run scene logic and render it. 
        Return next_scene_id, kwargs for next scene, if any. """
        return None, {}
    
        
class MainMenuScene(Scene):
    def __init__(self):
        self.ticks = 0
        
    def tick(self, buttons):
        if buttons[BTN_SUBMIT]:
            return SCN_WORLD, {'counter': self.ticks}
        elif buttons[BTN_CANCEL]:
            return SCN_QUIT, {}
        self.ticks += 1
        pg.display.get_surface().fill((55, 55, 111))
        blit_txt('Menu- %d ticks.' % self.ticks, (111, 222, 55), (50, 200))
        blit_txt('[Enter]: world, [ESC]: quit', (111, 222, 55), (50, 300))
        pg.display.flip()
        return None, {}

    
class WorldScene(Scene):
    def resume(self, **kwargs):
        self.counter = kwargs.get('counter', -1)  # -1 if counter not passed
            
    def tick(self, buttons):
        if buttons[BTN_CANCEL]:
            return SCN_MENU, {}
        pg.display.get_surface().fill((55, 111, 222))
        blit_txt('World- received %d.' % self.counter, (111, 55, 55), (50, 100))
        blit_txt('[ESC]: menu', (111, 55, 55), (50, 150))
        pg.display.flip()
        return None, {}


def blit_txt(txt, color, pos):  # blit text onto screen
    surf = pg.font.Font(None, 30).render(txt, 1, color)
    pg.display.get_surface().blit(surf, pos)
    

# main.py
def main():  # scene manager, state machine
    pg.init()
    pg.display.set_mode((500, 500))
    # setup scenes
    scenes = { SCN_MENU: MainMenuScene(), SCN_WORLD: WorldScene() }
    cur_scene = scenes[SCN_MENU]
    # map keyboard keys to abstract commands understood by scenes
    key2cmd = { pg.K_ESCAPE: BTN_CANCEL, pg.K_RETURN: BTN_SUBMIT }
    # loop
    clock = pg.time.Clock()
    done = False
    while not done:
        clock.tick(10)
        # find which buttons were pressed this tick
        buttons_pressed = { BTN_CANCEL: 0, BTN_SUBMIT: 0}
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN and event.key in key2cmd:
                cmd = key2cmd[event.key]
                buttons_pressed[cmd] = 1
        # tick current scene, pass it the state of the buttons
        next_scene_id, kwargs = cur_scene.tick(buttons_pressed)
        if next_scene_id == SCN_QUIT:
            done = True
        elif next_scene_id:
            cur_scene = scenes[next_scene_id]
            cur_scene.resume(**kwargs)

if __name__ == "__main__":
    main()
