import pygame
from constants import *
import player

def main():
    clock = pygame.time.Clock()
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player1.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(144) / 1000

if __name__ == "__main__":
    main()