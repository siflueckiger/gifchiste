import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800,400))
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
done = False
font_h1 = pygame.font.SysFont('Comic Sans MS', 300)
font_h2 = pygame.font.SysFont('Comic Sans MS', 66)

# VARIABLES
STATE = 0
width, height = pygame.display.get_surface().get_size()
xText = width  // 2 - 50
yText = height // 2 - 50

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# FUNCTIONS
def showScreenText(txt, font):
    textsurface = font.render(txt, False, (0, 0, 0))
    textWidth = textsurface.get_width()
    textHeight = textsurface.get_height()
    screen.blit(textsurface,(width // 2 - textWidth // 2 ,height // 2 - textHeight // 2))
    pygame.display.update()

def cameraTrigger():
    screen.fill((255,0,0))
    pygame.display.update()
    time.sleep(0.1)
    screen.fill((255,255,255))
    pygame.display.update()


def screen_standby():
    showScreenText("standby", font_h2)
    #pygame.display.update()

def screen_getReady():
    #showScreenText("get ready 3..2..1..")
    showScreenText("GET READY!!!", font_h2)
    time.sleep(2)
    screen.fill((255,255,255))
    pygame.display.update()
    showScreenText("3", font_h1)
    time.sleep(1)
    screen.fill((255,255,255))
    pygame.display.update()
    showScreenText("2", font_h1)
    time.sleep(1)
    screen.fill((255,255,255))
    pygame.display.update()
    showScreenText("1", font_h1)
    time.sleep(1)
    #pygame.display.update()

def screen_takePicture():
    sleeptime = 1.3
    #showScreenText("0..clickclickclick...", font_h2)
    showScreenText("pic 1", font_h2)
    time.sleep(sleeptime)
    cameraTrigger()

    showScreenText("pic 2", font_h2)
    time.sleep(sleeptime)
    cameraTrigger()

    showScreenText("pic 3", font_h2)
    time.sleep(sleeptime)
    cameraTrigger()

    showScreenText("pic 4", font_h2)
    time.sleep(sleeptime)
    cameraTrigger()

    showScreenText("pic 5", font_h2)
    time.sleep(sleeptime)
    cameraTrigger()

    time.sleep(1)
    #pygame.display.update()

def screen_saveImage():
    showScreenText("save image", font_h2)
    time.sleep(3)
    #pygame.display.update()

def screen_showImage():
    showScreenText("show gif -> again?", font_h2)
    #pygame.display.update()


# APP LOOP
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                STATE += 1
                print(STATE)
            elif event.key == pygame.K_s:
                STATE -= 1
                print(STATE)
            elif event.key == pygame.K_q:
                done = True

    screen.fill((255,255,255))

    if STATE == 0:
        screen_standby()
    elif STATE == 1:
        screen_getReady()
        STATE += 1
    elif STATE == 2:
        screen_takePicture()
        STATE += 1
    elif STATE == 3:
        screen_saveImage()
        STATE += 1
    elif STATE == 4:
        screen_showImage()
