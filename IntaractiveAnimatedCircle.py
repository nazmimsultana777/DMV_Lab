import pygame

pygame.init()

# Create window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Animated Circle")

clock = pygame.time.Clock()

x = 300
y = 200
speed = 5

running = True

while running:
    clock.tick(60)   # controls animation speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))  # refresh screen

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

    pygame.display.update()

pygame.quit()