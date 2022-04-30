import pygame

pygame.display.init()

screen = pygame.display.set_mode((1000, 600))

screen.fill((230, 230, 230))

pygame.display.flip()

running = True
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False