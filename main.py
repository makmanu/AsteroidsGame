import pygame
from constants import *
import player
import asteroid
import asteroidfield
import sys

def main():
    clock = pygame.time.Clock()
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield.AsteroidField.containers = (updatable)
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield1 = asteroidfield.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        for thing in drawable:
            thing.draw(screen)
        for thing in asteroids:
            if thing.has_collision(player1):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(144) / 1000

if __name__ == "__main__":
    main()