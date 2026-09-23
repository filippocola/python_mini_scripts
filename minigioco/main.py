import pygame
import sys 
from settings import * 
from minigioco.entities import Ship


def main():
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Galaxy game")
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprite = pygame.sprite.Group()

    # Crea il giocatore 
    player = Ship()
    all_sprite.add(player)

    # Game Loop
    running = True
    while running:
        # 1. Eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        # Update 
        all_sprite.update()

        # Disegna   
        screen.fill(BLACK)
        all_sprite.draw(screen)
        pygame.display.flip()

        # FPS
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
