import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("MP3")
music_dict = {}



musicStore = "C:\\Users\\bayan\\OneDrive\\Desktop\\musics"

canMusStore = musicStore.replace("\\",os.sep).replace("/",os.sep)



songs = [os.path.join(musicStore, f) for f in os.listdir(musicStore) if f.endswith(".mp3")]
current = 0

pygame.mixer.init()

print(songs)
#if songs:
#    pygame.mixer.music.load(songs[current])

for el in songs:
    music_dict[el] = pygame.mixer.Sound(el)


def playSong():
    global current
    if songs:
        music_dict.get(songs[current]).play()

def stopSong():
    global current
    music_dict.get(songs[current]).stop()

def nextSong():
    global current
    
    
    if songs:
        stopSong()
        current = (current + 1) % len(songs)
        music_dict.get(songs[current]).play()

def previousSong():
    global current
    if songs:
        stopSong()
        current = (current - 1) % len(songs)
        music_dict.get(songs[current]).play()


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_p:
                playSong()
            elif i.key == pygame.K_s:
                stopSong()
            elif i.key == pygame.K_n:
                nextSong()
            elif i.key == pygame.K_b:
                previousSong()

    screen.fill((255,255,255))

    if songs:
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(os.path.basename(songs[current]), True, (0,0,0))
        screen.blit(text, (50, 50))
    pygame.display.flip()

pygame.quit()