import pygame,  sys #this part is to import the important modules
from pygame.locals import * #To simplificate the functions on the code. WIth this, I can call functions from the module without writing the whole path/name

pygame.init() #begins the game. This part is in all pygame codes.
DISPLAYSURF = pygame.display.set_mode((300, 100)) #set the window size
pygame.display.set_caption('Hello World!') #here is the title of the window
while True:#the main game loop, here is where the whole game will "works"
    for event in pygame.event.get():#It's an event. Pygame works in loops, refreshing and using events to know what to do in the next iteration
        if event.type==QUIT:#QUIT is a function of pygame
         pygame.quit()#the end of the program. It's the opposite of line 4 
         sys.exit()#exit sys module
        pygame.display.update()#here is the comand to pygame refresh and do the next iteration
