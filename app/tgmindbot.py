import pygame
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mindbot")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
