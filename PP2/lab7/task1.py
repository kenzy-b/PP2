import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Mickey's clock")

clock = pygame.image.load("C:\\Users\\bayan\\AppData\\Local\\Temp\\4b63a19f-ae2a-40cf-8fdc-9ef0d353a003_images for clock.zip.003\\images\\clock.png")
rightHand = pygame.image.load("C:\\Users\\bayan\\AppData\\Local\\Temp\\2c9ad50b-1481-4aeb-b53c-1f284e91863a_images for clock.zip.63a\\images\\rightarm.png")
leftHand = pygame.image.load("C:\\Users\\bayan\\AppData\\Local\\Temp\\c4bd615b-43b5-4b60-9f9a-e387840b8dfd_images for clock.zip.dfd\\images\\leftarm.png")

clockCenter = (500, 500)

def rotate(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    second_change = -seconds * 6
    minute_change = -minutes * 6

    rotated_left_hand, left_rec = rotate(leftHand, second_change, clockCenter)
    rotated_right_hand, right_rec = rotate(rightHand, minute_change, clockCenter)

    screen.blit(clock, (-200, 0))
    screen.blit(rotated_left_hand, left_rec)
    screen.blit(rotated_right_hand, right_rec)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()