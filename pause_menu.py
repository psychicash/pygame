#import libraries
import pygame

#import local files

import src.constants as constants


class Cl_Pause_Menu():
    def __init__(self, screen):
        '''
        Class that when instanced enters into a loop itself, causeing the
        previous loop (aka main game loop) to freeze in its tracks, thus
        pausing the game.

        Pause menu comes with it's own surface to blit to so only that
        surface needs to be updated.
        
        screen is the main pygame surface passed in to reference internally.
        '''
        self.clock = pygame.time.Clock()
        self.screen = screen
        print("This is the pause menu")

        #dimensions aliased and packed for easier reading and mutability
        self.pms_width = constants.PAUSE_SCREEN_WIDTH
        self.pms_height = constants.PAUSE_SCREEN_HEIGHT
        self.pms_dimensions = (self.pms_width, self.pms_height)

        #creates a surface for the pause menu itself
        self.pause_menu_surface = pygame.Surface(self.pms_dimensions)

        #sets the rectangle for the pause_menu_surface and sets the coords
        #this rect will be used to allign the pause menu in the render
        #function
        self.PM_rect = (0, 0, self.pms_width, self.pms_height)
        self.PM_rect.center = (constants.SCREEN_CENTER)

        #sets the pause menu sensor on and executes the loop
        self.pause_menu_active = True
        self.pause_loop()

    def pause_loop(self):
        while self.pause_menu_active:
            #normal game loop supercedes (pauses) the previous game loop
            self.Input()
            self.Update()
            self.Render(self.screen)

    def filtering_events(self):
        pressed_keys = pygame.key.get_pressed()
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
                self.pause_menu_active = False
            else:
                filtered_events.append(event)
        return filtered_events, pressed_keys

    def Input(self):

        events, pressed_keys = self.filtering_events()

        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                # Move to the next scene when the user pressed Enter
                events = []
                pygame.event.clear()

                self.pause_menu_active = False


        pass


    def Update(self):
        #update
        pass



    def Render(self, screen):
        # The game scene is just a blank screen set tot he pause menu color
        self.pause_menu_surface.fill(constants.PAUSE_MENU_COLOR)


        screen.blit(self.pause_menu_surface, self.PM_rect)

        pygame.display.update(self.pause_menu_surface)
        self.clock.tick(constants.FPS)
