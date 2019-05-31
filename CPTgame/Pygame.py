import pygame
pygame.init()

#this is making a window for the game
window = pygame.display.set_mode((640, 480))

#this is for naming the window
pygame.display.set_caption("Another Chance")

#character position
x = 270
y = 240

#Character size
width = 40
height = 60
vel  = 10

#running the code
run= True
while run == True:
  pygame.time.delay(100)

#checking if events have happened
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    x -= vel
  
  if keys[pygame.K_RIGHT]:
    x += vel
  
  if keys[pygame.K_UP]:
    y -= vel
    
  if keys[pygame.K_DOWN]:
    y += vel

  window.fill((0,0,0))
  pygame.draw.rect(window, (225, 0, 0), (x, y, width, height))
  pygame.display.update()


pygame.quit()
