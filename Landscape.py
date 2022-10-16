# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

# Sun + Moon Variables
sun_outer_colour = (254, 204, 81)
sun_inner_colour = (255, 228, 105)
moon_colour = (148, 144, 141)
sun_outer_x = 610
sun_outer_y = 450
sun_outer_y_speed = -2
sun_outer_x_speed = -1.35

# Sky Variables
sky1 = 135
sky2 = 206
sky3 = 235
sky1_colour = 1
sky2_colour = 1
sky3_colour = 1

# House + Grass Variables
grass_colour = (0, 154, 23)
house_base_colour = (253, 221, 230)
roof_colour = (105, 105, 105)
door_colour = (255, 255, 225)
doorknob_colour = (202, 179, 111)
window_colour = (255, 255, 225)

# Cloud Variables
cloud = (255, 255, 255)
cloud1_x = 115
cloud1_y = 60
cloud2_x = 320
cloud2_y = 60
cloud3_x = 525
cloud3_y = 60
cloud1_x_speed = 1
cloud2_x_speed = 1
cloud3_x_speed = 1

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # Sun Animation
    if sun_outer_y > 450:
        sun_outer_x_speed = sun_outer_x_speed * -1
        sun_outer_y_speed = sun_outer_y_speed * -1
        if sun_outer_colour == (254, 204, 81) and sun_inner_colour == (255, 228, 105):
            sun_outer_colour = (148, 144, 141)
            sun_inner_colour = (148, 144, 141)
        else:
            sun_outer_colour = (254, 204, 81)
            sun_inner_colour = (255, 228, 105)
    elif sun_outer_y < 60:
        sun_outer_x_speed = sun_outer_x_speed * 1
        sun_outer_y_speed = sun_outer_y_speed * -1

    sun_outer_y += sun_outer_y_speed
    sun_outer_x += sun_outer_x_speed
    
    # Day & Night Cycle
    if sky1 < 1:
        sky1_colour = 0.3375
    elif sky1 > 135:
        sky1_colour = -0.3375
    if sky2 < 72:
        sky2_colour = 0.3375
    elif sky2 > 206:
        sky2_colour = -0.3375
    if sky3 < 101:
        sky3_colour = 0.3375
    elif sky3 > 235:
        sky3_colour = -0.3375    

    sky1 += sky1_colour
    sky2 += sky2_colour
    sky3 += sky3_colour

    # Clouds
    if cloud1_x < 75:
        cloud1_x_speed = 1
    elif cloud1_x > 565:
        cloud1_x_speed = -1
    if cloud2_x < 75:
        cloud2_x_speed = 1
    elif cloud2_x > 565:
        cloud2_x_speed = -1
    if cloud3_x < 75:
        cloud3_x_speed = 1
    elif cloud3_x > 565:
        cloud3_x_speed = -1

    cloud1_x += cloud1_x_speed
    cloud2_x += cloud2_x_speed
    cloud3_x += cloud3_x_speed

    # ---------------------------

    # Sky (background)
    screen.fill((sky1, sky2, sky3))  # always the first drawing command

    # Sun
    pygame.draw.circle(screen, sun_outer_colour, (sun_outer_x, sun_outer_y), 25)
    pygame.draw.circle(screen, sun_inner_colour, (sun_outer_x, sun_outer_y), 20)

    # Grass
    pygame.draw.rect(screen, grass_colour, (0, 380, 640, 120), 0)

    # Base of House
    pygame.draw.rect(screen, house_base_colour, (50, 280, 130, 130), 0)

    # Roof of House
    pygame.draw.polygon(screen, roof_colour, ((20, 280), (210, 280), (115, 200)), 0)

    # Door of House (+ doorknob)
    pygame.draw.rect(screen, door_colour, (70, 345, 30, 65), 0)
    pygame.draw.circle(screen, doorknob_colour, (95, 380), 3)

    # Window of House
    pygame.draw.rect(screen, window_colour, (130, 345, 30, 32.5), 0)

    # Cloud 1 (Left)
    pygame.draw.circle(screen, cloud, (cloud1_x, cloud1_y), 20)
    pygame.draw.circle(screen, cloud, (cloud1_x-30, cloud1_y), 20)
    pygame.draw.circle(screen, cloud, (cloud1_x+30, cloud1_y), 20)
    pygame.draw.circle(screen, cloud, (cloud1_x-10, cloud1_y-20), 20)
    pygame.draw.circle(screen, cloud, (cloud1_x+10, cloud1_y-20), 20)

    # Cloud 2 (Middle)
    pygame.draw.circle(screen, cloud, (cloud2_x, cloud2_y), 20)
    pygame.draw.circle(screen, cloud, (cloud2_x-20, cloud2_y), 20)
    pygame.draw.circle(screen, cloud, (cloud2_x+20, cloud2_y), 20)
    pygame.draw.circle(screen, cloud, (cloud2_x-15, cloud2_y-30), 20)
    pygame.draw.circle(screen, cloud, (cloud2_x+15, cloud2_y-30), 20)

    # Cloud 3 (Right)
    pygame.draw.circle(screen, cloud, (cloud3_x, cloud3_y), 20)
    pygame.draw.circle(screen, cloud, (cloud3_x-35, cloud3_y), 20)
    pygame.draw.circle(screen, cloud, (cloud3_x+35, cloud3_y), 20)
    pygame.draw.circle(screen, cloud, (cloud3_x, cloud3_y-25), 20)
    pygame.draw.circle(screen, cloud, (cloud3_x-20, cloud3_y-10), 20)
    pygame.draw.circle(screen, cloud, (cloud3_x+20, cloud3_y-10), 20)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
