import pygame

pygame.init()

screen_height = 400
screen_width = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Loading screen")
icon = pygame.image.load("images/circle.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.display.update()

angle = 0
running = True

circle = pygame.image.load("images/circle.png")
circle_sized = pygame.transform.rotozoom(circle, 0, 0.4)

bar = pygame.image.load("images/loading_bar.png")
bar_sized = pygame.transform.rotozoom(bar, 0, 0.4)
bar_rect = bar_sized.get_rect(center = (screen_width / 2, screen_height / 1.5))

cube = pygame.image.load("images/loading_cube.png")
cube_sized = pygame.transform.rotozoom(cube, 0, 0.24)

finished = pygame.image.load("images/done.png")
finished_sized = pygame.transform.rotozoom(finished, 0, 0.7)
finished_rect = finished_sized.get_rect(center = (screen_width / 2, screen_height / 2))

cube_position = 35
cube_positions = []

end = 265

cube_rect = cube_sized.get_rect(center = (cube_position, 246))

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rotated_circle = pygame.transform.rotate(circle_sized, angle)
    rotated_circle_rect = rotated_circle.get_rect(center = (screen_width / 2, screen_height / 3))

    screen.blit(rotated_circle, rotated_circle_rect)
    screen.blit(bar_sized, bar_rect)

    if cube_position < end:
        cube_position += 1

    cube_positions.append(cube_position)

    for pos in cube_positions:
        rect = cube_sized.get_rect(center=(pos, 246))
        screen.blit(cube_sized, rect)

    angle += -2

    if cube_position >= end:
        screen.blit(finished_sized, finished_rect)

    pygame.display.update()
    clock.tick(60)

else:
    pygame.quit()

