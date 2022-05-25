import sys, pygame
pygame.init()
size=1200,800
screem=pygame.display.set_mode(size)
pygame.display.set_caption("Star Wars")
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: run=False

pygame.quit()

