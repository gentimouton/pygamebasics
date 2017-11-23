import pygame
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE, K_RETURN, K_F4


# constants.py
CMD_SUBMIT = 'submit'
CMD_CANCEL = 'cancel'



# scenes.py
SCN_WORLD = 'world scene'
SCN_MENU = 'menu scene'
class Scene():
    def __init__(self, scene_manager, screen):
        self._scene_manager = scene_manager
        self._screen = screen
    def reset(self, params):
        pass
    def process_input(self):
        pass
    def tick(self):
        pass
    def render(self):
        pass
        
class MainMenuScene(Scene):
    def __init__(self, scene_manager, screen):
        Scene.__init__(self, scene_manager, screen)
        self.frame_num = 0
        self.font = pygame.font.Font(None, 30)
    def process_input(self, cmd):
        if cmd == CMD_SUBMIT:
            params = {'counter': self.frame_num}
            self._scene_manager.change_scene(SCN_WORLD, params)
        elif cmd == CMD_CANCEL:
            self._scene_manager.game_over = True
    def tick(self):
        self.frame_num += 1
    def render(self):
        self._screen.fill((0, 0, 111))
        txt_surf = self.font.render(str(self.frame_num), 1, (255, 255, 255))
        self._screen.blit(txt_surf, (200, 200))
        
class WorldScene(Scene):
    def reset(self, params):
        self.font = pygame.font.Font(None, 30)
        txt = str(params['counter']) if 'counter' in params else '???'
        self.txt_surf = self.font.render(str(txt), 1, (0, 0, 0))
    def process_input(self, cmd):
        if cmd == CMD_CANCEL:
            self._scene_manager.change_scene(SCN_MENU)
    def render(self):
        self._screen.fill((0, 255, 0))
        self._screen.blit(self.txt_surf, (300, 300))


# main.py
pygame.init()

        
class SceneManager():  # main file: state machine
    def __init__(self):
        self.game_over = False
        self.clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((500, 500))
        main_menu_scene = MainMenuScene(self, self._screen)
        world_scene = WorldScene(self, self._screen)
        self.scenes = {SCN_MENU: main_menu_scene, SCN_WORLD: world_scene}
        self.cur_scene = self.scenes[SCN_MENU]
        
    def run(self):
        while not self.game_over:
            self.clock.tick(60)
            pressed_keys = pygame.key.get_pressed()
            alt_held = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_over = True
                if event.type == KEYDOWN:
                    key = event.key
                    if key == K_F4 and alt_held:
                        self.game_over = True
                    elif key == K_ESCAPE:
                        self.cur_scene.process_input(CMD_CANCEL)  # may change cur_scene
                    elif key == K_RETURN:
                        self.cur_scene.process_input(CMD_SUBMIT)  # may change cur_scene
            self.cur_scene.tick()
            self.cur_scene.render()
            pygame.display.update()
    
    def change_scene(self, new_scene_name, new_scene_params={}):
        if new_scene_name in self.scenes.keys():
            self.cur_scene = self.scenes[new_scene_name]
            self.cur_scene.reset(new_scene_params)

if __name__ == "__main__":
    SceneManager().run()
