import pygame
import time

def main():
    screen = pygame.display.set_mode((600, 600))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(0, 0, 600, 600))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(10, 10, 580, 580))
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(20, 20, 560, 560))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(30, 30, 540, 540))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(40, 40, 520, 520))
    for i in range (125, 476, 50):
        pygame.draw.line(screen, 'blue', (i, 125), (i, 475))
    for i in range (125, 476, 50):
        pygame.draw.line(screen, 'blue', (125, i), (475, i))
    pygame.display.update()
    time.sleep(1)
    clrs=['red','green','blue','cyan','yellow']
    clr_index = 0
    for r in range (100, 50, -10):
        pygame.draw.circle(screen, clrs[clr_index], (350, 350), r)
        time.sleep(1)
        pygame.display.update()
        clr_index += 1


main()
