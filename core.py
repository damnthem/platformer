# modules and scripts import
import pygame
from pygame import *

# window params
window_name = 'Platformer'
window_params = (800, 600)
window_background_color= (0,0,51)

def main():
    pygame.init()
    screen = pygame.display.set_mode(window_params)
    pygame.display.set_caption(window_name)
    screen.fill(window_background_color)

    game_running = True
    while game_running:
        for game_state_event in pygame.event.get():
            if game_state_event.type == QUIT:
                game_running = False
                raise SystemExit, "QUIT"
        pygame.display.update()

if __name__ == "__main__":
    main()
