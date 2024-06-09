import pygame, sys
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import QUIT
import random
import time
import math
import numpy as np
import os
from pygame._sdl2 import Window

FPS = 60
COLOR = (255, 0, 0)
PURPLE = (128, 0, 128)
LIGHTPURPLE = (153,84,176)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
CYAN = (0,255,255)
RED = (255, 0, 0)
BG = WHITE
WIDTH = 600
HEIGHT = 500
x = WIDTH / 2
y = HEIGHT / 2
r = 10
HP=100
HPrecording = 100
HPrecording2 = 100
movement = [0, 0]
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.draw.circle(screen, COLOR, (x, y), r)
pygame.display.update()
clock = pygame.time.Clock()
running = True
motion = False
movementsbool = [False, False, False, False]
CD = 5
iframes = 0
pygame.display.set_caption('gameing')
pi23 = math.pi * 2 / 3
pi47 = math.pi * 4 / 7
pi87 = math.pi * 8 / 7
#This is just here for when I add multiple screens in the future

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Choose a circle', True, WHITE, BLACK)
textRect = text.get_rect()


text2 = font.render('Ready?', True, GREEN, BLACK)
text2Rect = text2.get_rect()
# set the center of the rectangular object.
textRect.center = (WIDTH // 2, HEIGHT // 2)
text2Rect.center = (WIDTH // 2, HEIGHT // 2)
ticks = 0
speedx = 1
speedy = 1
Stuff = {}
SpecialStuff = {}
PlatformStuff = {}
VerySpecialStuff = {}
OverlayStuff = {}
laser_sound = pygame.mixer.Sound("laser.wav")
spawn_sound = pygame.mixer.Sound("Spawn.wav")
laugh_sound = pygame.mixer.Sound("DoGLaugh.wav")
break1 = pygame.mixer.Sound("break1.wav")
break2 = pygame.mixer.Sound("break2.wav")
break3 = pygame.mixer.Sound("break3.wav")
break4 = pygame.mixer.Sound("break4.wav")
death = pygame.mixer.Sound("death.wav")
head1 = pygame.image.load("head1.png")
body1 = pygame.image.load("body1.png")
tail1 = pygame.image.load("tail1.png")
head2 = pygame.image.load("head2.png")
body2 = pygame.image.load("body2.png")
tail2 = pygame.image.load("tail2.png")

#obj: object type + id
#color: color (affects properties btw). Special stuff has a sequence at [color, t]. If t is < 0 and there is another color it will delete itself. 
#cords: the place where the object is
#size: the size of the object
#vector: the number added to cords every frame. Special Stuff has a path outlined in it as [[x, y, t], [x, y, t]] where it will swap between vectors and disappear after t ticks
intv = 0
window = Window.from_display_module()
windowpos = window.position
clr = (0, 0, 0)
safeguard = False
safeguard2 = False
safeguard3 = False
safeguard4 = False
gravity = 0
ticksg = 0
gravityh = 0
ticksgh = 0
offset = 0
resetgravity = False
resetgravityh = False
texttoprint = ["", 0]
#limbo = pygame.mixer.Sound("limbojumpscare.mp3") 
def addstuff(obj, color, cords, size, vector, damage=5, gravity=[False, [0, 0]]):
    global Stuff
    global intv
    intv += 1
    Stuff.update({
        f"{obj}{intv}": {
            "color": color,
            "cords": cords,
            "size": size,
            "vector": vector,
            "damage": damage,
            "gravity": gravity
        }
    })
def addoverlaystuff(obj, color, cords, size, vector, damage=5, gravity=[False, [0, 0]]):
    global OverlayStuff
    global intv
    intv += 1
    OverlayStuff.update({
        f"{obj}{intv}": {
            "color": color,
            "cords": cords,
            "size": size,
            "vector": vector,
            "damage": damage,
            "gravity": gravity
        }
    })
def addspecialstuff(obj, color, cords, size, vector, damage=5, gravity=[False, [0, 0]]):
    global SpecialStuff
    global intv
    intv += 1
    SpecialStuff.update({
        f"{obj}{intv}": {
            "color": color,
            "cords": cords,
            "size": size,
            "vector": vector,
            "damage": damage,
            "gravity": gravity
        }
    })
def addplatformstuff(obj, color, cords, size, vector, gravity = [False, [0, 0]]):
    global PlatformStuff
    global intv
    intv += 1
    PlatformStuff.update({
        f"{obj}{intv}": {
            "color": color,
            "cords": cords,
            "size": size,
            "vector": vector,
            "gravity": gravity
            }
        })
#This is reserved for only the pathings that cant be done with vectors, will probably be laggy
    #pathing is a string
def addveryspecialstuff(obj, color, cords, size, pathing, damage=5, sprited = [False, None], gravity = [False, [0, 0]], timecounter=0):
    global VerySpecialStuff
    global intv
    intv += 1
    VerySpecialStuff.update({
        f"{obj}{intv}_special": {
            "color": color,
            "cords": cords,
            "size": size,
            "pathing": pathing,
            "damage": damage,
            "sprited": sprited,
            "gravity": gravity,
            "time": timecounter
            }})
                         
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WIDTH,HEIGHT)


def makeunitvector(vector):
    c = math.sqrt(vector[0]**2 + vector[1]**2)
    if c > 0:
        return [vector[0] / c, vector[1] / c]
    else:
        return [1, 1]
rvar = 10
wormlength = 51
wormspeed = 1
mainmenu = True
movementground = False
ground2 = False
hyperfancystuff = False
deathscreen = False
background = False
debug = False
phase1 = True
phase2 = False
ticks = 0
offset = 0
while True:
    #Main menu
    while mainmenu:

        rvar = 10
        r2var = 10
        r3var = 10
        screen.fill(BLACK)
        #pygame.draw.circle(screen, RED, (WIDTH / 2, HEIGHT / 2), rvar)
        pygame.draw.circle(screen, ORANGE, (200, 250), r2var)
        pygame.draw.circle(screen, GREEN, (400, 250), r3var)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                #if x1 > WIDTH / 2 - r and x1 < WIDTH / 2 + r and y1 < HEIGHT / 2 + r and y1 > HEIGHT / 2 - r:
                #    
                #    print(f"x: {x}, y: {y}")
                #    while rvar > 0:
                #        rvar -= 0.23
                #        screen.fill(BLACK)
                #        pygame.draw.circle(screen, RED, (WIDTH / 2, HEIGHT / 2), rvar)
                #        pygame.display.update()
                #    r = 10
                #    Stuff = {}
                #    SpecialStuff = {}
                #    ticks = 0
                #    HP = 100
                #    x, y = WIDTH / 2, HEIGHT / 2
                #    movementsbool = [False, False, False, False]
                #    movement = [0, 0]
                #    mainmenu = False
                #    movementground = True
                #    COLOR = RED
                #    pygame.mixer.music.set_volume(0.5)
                if x1 > 200 - r and x1 < 200 + r and y1 < 250 + r and y1 > 250 - r:
                    while r2var > 0:
                        r2var -= 0.223
                        screen.fill(BLACK)
                        pygame.draw.circle(screen, ORANGE, (200, 250), r2var)
                        pygame.display.update()
                    r = 10
                    Stuff = {}
                    SpecialStuff = {}
                    ticks = 0
                    HP = 100
                    x, y = WIDTH / 2, HEIGHT / 2
                    movementsbool = [False, False, False, False]
                    movement = [0, 0]
                    mainmenu = False
                    movementground = False
                    ground2 = True
                    COLOR = ORANGE
                    texttoprint = ["", 0]
                    pygame.mixer.music.load('funnylimbosong.wav')
                    pygame.mixer.music.set_volume(0.3)
                                                    
                    pygame.mixer.music.play(1)
                    safeguard = False
                if x1 > 400 - r and x1 < 400 + r and y1 < 250 + r and y1 > 250 - r:
                    print("aaaaaaa")
                    while r3var > 0:
                        r3var -= 0.2
                        screen.fill(BLACK)
                        pygame.draw.circle(screen, GREEN, (400, 250), r3var)
                        pygame.display.update()
                    r = 10
                    Stuff = {}
                    SpecialStuff = {}
                    ticks = 0
                    HP = 100
                    x, y = WIDTH / 2, HEIGHT / 2
                    movementsbool = [False, False, False, False]
                    movement = [0, 0]
                    mainmenu = False
                    movementground = False
                    ground2 = False
                    hyperfancystuff = True
                    phase1 = True
                    phase2 = False
                    phase3 = False
                    BG = WHITE
                    wormspeed = 1
                    wormlength = 51
                    COLOR = GREEN
                    texttoprint = ["", 0]
                    #pygame.mixer.music.load('funnylimbosong.wav')
                    #pygame.mixer.music.set_volume(0.3)
                                                    
                    #pygame.mixer.music.play(1)
                    safeguard = False
                    background = False
        screen.blit(text, (20, 20))
        pygame.display.update()
        clock.tick(FPS)
        
    #Death screen
    while deathscreen:
        ticks += 1
        pygame.mixer.music.stop()
        screen.fill(BLACK)
        if ticks < 15:
            pygame.draw.circle(screen, COLOR, (x, y), r)
        elif ticks == 16:
            for i in range(150):
                addstuff("circle", COLOR, [x, y], [2],[random.uniform(-8, 8), random.uniform(-8, 8)])
        elif ticks == 100:
            deathscreen = False
            mainmenu = True
        
        stf = 0  #just a counter variable
        for i in list(Stuff.keys()):
            Stuff[i]["cords"] = [Stuff[i]["cords"][0] + Stuff[i]["vector"][0],Stuff[i]["cords"][1] + Stuff[i]["vector"][1]]
            addstf = True
            if Stuff[i]["cords"][0] > WIDTH + 100 or Stuff[i]["cords"][0] < -100 or Stuff[i]["cords"][1] > HEIGHT + 100 or Stuff[i]["cords"][1] < -100:
                del Stuff[i]
                continue

            #draw the stuff + collisions (because of course circles are centered but rectangles aren't, which makes sense but still is annoying)
            if "rect" in i:
                pygame.draw.rect(screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1], Stuff[i]["size"][0], Stuff[i]["size"][1]))
                if Stuff[i]["cords"][0] <= x and (Stuff[i]["cords"][0] + Stuff[i]["size"][0]) >= x and Stuff[i]["cords"][1] <= y and (Stuff[i]["cords"][1] + Stuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= 5
                        iframes = 10

            if "circle" in i:
                pygame.draw.circle( screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1]), Stuff[i]["size"][0])
                if (Stuff[i]["cords"][0] + Stuff[i]["size"][0] > x and Stuff[i]["cords"][0] - Stuff[i]["size"][0] < x) and (Stuff[i]["cords"][1] + Stuff[i]["size"][0] > y and Stuff[i]["cords"][1] - Stuff[i]["size"][0] < y):
                    #print("collision with circle obj")
                    #print("y collision")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= 5
                        iframes = 10

            #will not implement arc collision because I will not be using them for anything other than backgrounds
            if "arc" in i:
                pygame.draw.arc(screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1], Stuff[i]["size"][0], Stuff[i]["size"][1]), 0,math.pi * 2)

            #accelerate stuff with the "accel" tag
            if "accel" in i:
                Stuff[i]["vector"] = [Stuff[i]["vector"][0] * 1.05,Stuff[i]["vector"][1] * 1.05]


            stf += 1
        pygame.display.update()
        clock.tick(FPS)
        
    #Green
    while hyperfancystuff:
        ticks += 1
        HP += 0.01
        timev = time.time()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    resetgravity = True
                    movementsbool[2] = True
                if event.key == pygame.K_DOWN:
                    resetgravity = True
                    movementsbool[3] = True
                if event.key == pygame.K_LEFT:
                    movementsbool[0] = True
                if event.key == pygame.K_RIGHT:
                    movementsbool[1] = True
                if event.key == pygame.K_LSHIFT:
                    if CD < 0:
                        movement[0] = movement[0] * 8
                        movement[1] = movement[1] * 8
                        #iframes += 20
                        CD = 5
                
                if event.key == pygame.K_LCTRL:
                    #addstuff("rect", BLUE, [0, 0], [10, 800], [5, 0])
                    #addstuff("circle", BLUE, [300, 0], [10], [random.randint(-5, 5), 5])
                    #addstuff("arc", COLOR, [x, y], [20, 20], [makeunitvector(movement)[0] + movement[0],makeunitvector(movement)[1] + movement[1]])
                    #print(f"x : {x}, y : {y}")
                    #print(f"x : {movement[0]}, y : {movement[1]}")
                    #print(Stuff)
                    #print(makeunitvector(movement))
                    #addspecialstuff("rect", [[BLUE, 100]], [0,0], [10, 50], [[20, 0, 30], [0, 0, 100]], 10)
                    #addstuff("homingcircle", PURPLE, [0, random.randint(0, 500)], [10], [1, 0])
                    #print(SpecialStuff)
                    #print(ticks)
                    print(ticksm)
                    print(1 / timetaken)
                    #print(SpecialStuff["rect1"])
                    #print(SpecialStuff["rect1"]["vector"][0])
                    #print(iframes)
                    #if gravity == 0:
                    #    gravity = 0.8
                    #else:
                    #    gravity = -0.8
                    #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[1, 1, 1000]], 10, [True, 1.8, 1.8])
                    #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 10000]], 10, [True, 1.8, 1.8])
                    #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 10000]], 10, [True, 1.8, 1.8])
                    #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 10000]], 10, [True, 1.8, 1.8])
                    #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 10000]], 10, [True, 1.8, 1.8])
                    #addplatformstuff("rect", [[BLACK, 100]], [-100, 400], [100, 10], [[1, -1, 70]], True)
                    #addplatformstuff("rect", [[BLACK, 100]], [0, 250], [40, 100], [[5, 0, 50], [0, -5, 50]], False)
                    #print(gravity)
                    #print(movement)
                    #print(VerySpecialStuff)
                if event.key == pygame.K_c:
                    texttoprint = ["Challenge mode", 100]
                    pygame.mixer.Sound.play(laugh_sound)
                    addplatformstuff("rect", [[WHITE, 100]], [0, 400], [600, 10], [[0, 0, 25000]])
                    addplatformstuff("rect", [[WHITE, 100]], [0, 200], [600, 10], [[0, 0, 25000]])
                    addspecialstuff("circle", [[WHITE, 100]], [300, 500], [25], [[0, 0, 25000]], 10, [True, 0, 4])
                if event.key == pygame.K_2:
                    offset = 3000 - ticksm
                if event.key == pygame.K_3:
                    safeguard2 = True
                    safeguard3 = False
                    offset = 6600 - ticksm
                if event.key == pygame.K_4:
                    safeguard2 = True
                    safeguard3 = False
                    offset = 11000 - ticksm
                    pos = pygame.mixer.music.set_pos(11000 / 60)
                if event.key == pygame.K_5:
                    safeguard1 = True
                    safeguard2 = True
                    safeguard3 = True
                    safeguard4 = False
                    tickstotp = 0
                    offset = 14000 - ticksm
                    pos = pygame.mixer.music.set_pos(14000 / 60)
                if event.key == pygame.K_h:
                    HP += 100
                    #addspecialstuff("rect", [[BLACK, 100]], [0, 000], [600, 20], [[0, 0, 1000]])
                    #addspecialstuff("rect", [[BLACK, 100]], [0, 400], [600, 20], [[0, 0, 1000]])
                if event.key == pygame.K_d:
                #    addspecialstuff("circle", [[WHITE, 100]], [-50, 250], [25], [[7.5, 0, 30], [1.25, 0, 60], [-15, 0, 20]], 10, [True, -1, -1])
                #    addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [25], "movetocenterfromleft rosecurve", damage=35, timecounter=150)
                #    for i in range(49):
                #        addveryspecialstuff("circle", [[BLUE, 100]], [-1200, 250], [25], "movetocenterfromleft rosecurve", damage=5, timecounter=149-i)
                #    addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [25], "movetocenterfromleft rosecurve", damage=35, timecounter=99)
                #    background = True
                    if debug:
                        debug = False
                    else:
                        debug = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    movementsbool[2] = False
                if event.key == pygame.K_DOWN:
                    movementsbool[3] = False
                if event.key == pygame.K_LEFT:
                    movementsbool[0] = False
                if event.key == pygame.K_RIGHT:
                    movementsbool[1] = False
            if event.type == MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                print(f"x: {x1} y: {y1}")
        

        #Color shenanigans
        if iframes > 0:
            if COLOR[1] > 200:
                COLOR = (0, COLOR[1] - 25, 0)
            if COLOR[1] > 10:
                COLOR = (0, COLOR[1] - 10, 0)
        else:
            if COLOR[1] < 255:
                COLOR = (0, COLOR[1] + 25, 0)
            if COLOR[1] > 255:
                COLOR = (0, 255, 0)
        #print(COLOR)
        
        
        if texttoprint[1] < 0:
            texttoprint[0] = ""
        
        gravity, gravityh = 0, 0
        if ticks == 10:
            #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 1000]], 10, [True, 0.8, 0.8])
            #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 1000]], 10, [True, 0.8, 0.8])
            #addspecialstuff("circle", [[BLACK, 100]], [random.randint(0, 600), random.randint(0, 500)], [25], [[0, 0, 1000]], 10, [True, 0.8, 0.8])
            #addspecialstuff("circle", [[BLACK, 100]], [300, 350], [25], [[0, 0, 1000]], 10, [True, 0.8, 0.8])
            #addspecialstuff("circle", [[BLACK, 100]], [300, 150], [25], [[0, 0, 1000]], 10, [True, 0.8, 0.8])
            pass
        
        #elif ticks < 100:
        #    pass
        #if ticks < 1000:
            
        #    if y > 250:
        #        gravity = -0.8
        #    elif y < 250:
        #        gravity = 0.8
        #    if x > 300:
        #        gravityh = -0.8
        #    elif x < 300:
        #        gravityh = 0.8
        
        
        
        pos = pygame.mixer.music.get_pos()
        ticksm = int((60 / 1000) * pos) + offset#ticksm = music based ticks
        if phase1:
            #really short because phase 1 is boring and I cannot be bothered to make it not boring
            if ticksm < 2400:
                
                if ticks == 100:
                    pygame.mixer.Sound.play(spawn_sound)
                    BG = BLACK
                    pygame.mixer.music.load('DoGMusic1.mp3')
                    pygame.mixer.music.set_volume(0.3)                                     
                    pygame.mixer.music.play(1)
                    addspecialstuff("circle", [[WHITE, 100]], [-50, 250], [25], [[0, 0, 30]], 10, [True, -10, -10])
                    addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [25], "movetocenterfromleft rosecurve", damage=35, timecounter=98*wormspeed, sprited=[True, tail1])
                    for i in range(wormlength):
                        addveryspecialstuff("circle", [[BLUE, 100]], [-1200, 250], [25], "movetocenterfromleft rosecurve", damage=5, timecounter=(99+ 2 * i)*wormspeed, sprited=[True, body1])
                    addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [25], "movetocenterfromleft rosecurve", damage=35, timecounter=(99 + wormlength * 2)*wormspeed, sprited=[True, head1])
                elif ticks > 100:
                    if len(VerySpecialStuff) > 0:
                        ticksfadeout = VerySpecialStuff[list(VerySpecialStuff.keys())[0]]["time"] + 180
                    if ticks%500 == 0:
                        pygame.mixer.Sound.play(laser_sound)
                        addspecialstuff("rect", [[LIGHTPURPLE,100]], [x, -400], [10, 50], [[0, 15, 100]])
                        addspecialstuff("rect", [[LIGHTPURPLE,100]], [x, 900], [10, 50], [[0, -15, 100]])
                        addspecialstuff("rect", [[LIGHTPURPLE,100]], [-400, y], [50, 10], [[15, 0, 100]])
                        addspecialstuff("rect", [[LIGHTPURPLE,100]], [900, y], [50, 10], [[-15, 0, 100]])
                    if (ticks+150)%1500 == 0:
                        wormspeed = 2
                    if (ticks)%1500 == 0:
                        wormspeed = 1
                    #need to add in more attacks and stuff here    
                        
                    
            else:
                for i in list(VerySpecialStuff.keys()):
                    #print(f" {VerySpecialStuff[i]['time']} : {ticks}")
                    if VerySpecialStuff[i]["time"] > ticksfadeout:
                        addspecialstuff("circle", [[LIGHTPURPLE, 100]], [VerySpecialStuff[i]["cords"][0] + random.randint(-10, 10), VerySpecialStuff[i]["cords"][1] + random.randint(-10, 10)], [50], [[0, 0, 10]], 10, gravity=[True, -0.1, -0.1])
                        #print("deleting")
                        del VerySpecialStuff[i]
                    continue
                if len(VerySpecialStuff) == 20:
                    pygame.mixer.music.fadeout(1000)
                if len(VerySpecialStuff) == 0:
                    
                    phase1 = False
                    phase2 = True
                    pygame.mixer.Sound.play(laugh_sound)
                    ticks = 0
                    pygame.mixer.music.load('DoGMusic2.wav')
                    #pygame.mixer.music.set_volume(0.3)                                     
                    #pygame.mixer.music.play(1)
        elif phase2:
            if ticksm == 0:
                #pygame.mixer.music.load('DoGMusic2.wav')
                pygame.mixer.music.set_volume(0.3)                                     
                pygame.mixer.music.play(1)
            elif ticksm < 300:
                if ticks%100 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, -400], [10, 50], [[0, 15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, 900], [10, 50], [[0, -15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [-400, y], [50, 10], [[15, 0, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [900, y], [50, 10], [[-15, 0, 100]])
            elif ticksm < 540:
                if ticks%5 == 0:
                    print(ticksm)
                    addspecialstuff("circle", [[LIGHTPURPLE, 100]], [-5 + random.randint(0, 25), 250 + random.randint(-25, 25)], [50], [[0, 0, 40]], 10, gravity=[True, -0.05, -0.05])
            elif ticksm > 540 and not safeguard:
                #background = False
                safeguard = True
                wormlength = 30
                wormspeed = 3
                addspecialstuff("circle", [[WHITE, 100]], [-50, 250], [25], [[0, 0, 30]], 10, [True, -10, -10])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [35], "movetocenterfromfarleft rose2curve", damage=35, timecounter=97*wormspeed, sprited=[True, tail2])
                for i in range(wormlength):
                    addveryspecialstuff("circle", [[BLUE, 100]], [-1200, 250], [35], "movetocenterfromfarleft rose2curve", damage=5, timecounter=(99+ 4 * i)*wormspeed, sprited=[True, body2])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [40], "movetocenterfromfarleft rose2curve", damage=35, timecounter=(99 + wormlength * 4)*wormspeed, sprited=[True, head2])
            elif ticksm < 1500:
                if ticks%500 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, -400], [10, 50], [[0, 15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, 900], [10, 50], [[0, -15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [-400, y], [50, 10], [[15, 0, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [900, y], [50, 10], [[-15, 0, 100]])
            #bossfight lasts until ticks = 15360
            elif ticksm < 1600:
                wormspeed = 3
            elif ticksm < 3500:
                if ticks%500 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, -400], [10, 50], [[0, 18, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, 900], [10, 50], [[0, -18, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [-400, y], [50, 10], [[18, 0, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [900, y], [50, 10], [[-18, 0, 100]])
                if (ticks+250)%1500 == 0:
                    #pygame.mixer.Sound.play(laugh_sound)
                    wormspeed = 6
                if (ticks)%1500 == 0:
                    wormspeed = 3
                if len(VerySpecialStuff) > 0:
                    ticksfadeout = VerySpecialStuff[list(VerySpecialStuff.keys())[0]]["time"] + 500
            elif ticksm < 3850:
                for i in list(VerySpecialStuff.keys()):
                    #print(f" {VerySpecialStuff[i]['time']} : {ticks}")
                    if VerySpecialStuff[i]["time"] > ticksfadeout:
                        addspecialstuff("circle", [[LIGHTPURPLE, 100]], [VerySpecialStuff[i]["cords"][0] + random.randint(-10, 10), VerySpecialStuff[i]["cords"][1] + random.randint(-10, 10)], [50], [[0, 0, 10]], 10, gravity=[True, -0.1, -0.1])
                        #print("deleting")
                        del VerySpecialStuff[i]
                        soundplayed = False
                    continue
                if len(VerySpecialStuff) == 0:
                    phase1 = False
                    phase2 = True
                    if not soundplayed:
                        pygame.mixer.Sound.play(laugh_sound)
                        soundplayed = True
                    safeguard2 = False
            elif ticksm < 4900:
                if ticks%75 == 0:
                    if random.randint(1,2) == 1:
                        for i in range(20):
                            addspecialstuff("rect", [[LIGHTPURPLE,100]], [-200, random.randint(0,10) + i*40], [250, 10], [[0, 0, 30], [25, 0, 50]])
                    else:
                        for i in range(20):
                            addspecialstuff("rect", [[LIGHTPURPLE,100]], [random.randint(0,10) + i*40, -200], [10, 250], [[0, 0, 30], [0, 25, 50]])
            elif ticksm < 5000:
                pass
            elif ticksm > 5000 and not safeguard2:
                #background = False
                safeguard2 = True
                wormlength = 20
                wormspeed = 3
                addspecialstuff("circle", [[WHITE, 100]], [-50, 250], [25], [[0, 0, 30]], 10, [True, -10, -10])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [35], "movetocenterfromfarleft rose3curve", damage=35, timecounter=97*wormspeed, sprited=[True, tail2])
                for i in range(wormlength):
                    addveryspecialstuff("circle", [[BLUE, 100]], [-1200, 250], [35], "movetocenterfromfarleft rose3curve", damage=5, timecounter=(99+ 4 * i)*wormspeed, sprited=[True, body2])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [40], "movetocenterfromfarleft rose3curve", damage=35, timecounter=(99 + wormlength * 4)*wormspeed, sprited=[True, head2])
            elif ticksm < 5600:
                if ticks%500 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, -400], [10, 50], [[0, 15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, 900], [10, 50], [[0, -15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [-400, y], [50, 10], [[15, 0, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [900, y], [50, 10], [[-15, 0, 100]])
                if (ticks)%250 == 0:
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addstuff("circle", WHITE, headcords, [25], [x*5 for x in makeunitvector([x-headcords[0], y-headcords[1]])], gravity=[True, -2, -2])
            elif ticksm < 7150:

                if ticks%300 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, -400], [10, 50], [[0, 16, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, 900], [10, 50], [[0, -16, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [-400, y], [50, 10], [[16, 0, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [900, y], [50, 10], [[-16, 0, 100]])
                if (ticks+250)%750 == 0:
                    #pygame.mixer.Sound.play(laugh_sound)
                    wormspeed = 8
                if (ticks)%250 == 0:
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addstuff("circle", WHITE, headcords, [25], [x*5 for x in makeunitvector([x-headcords[0], y-headcords[1]])], gravity=[True, -2, -2])
                if (ticks)%1500 == 0:
                    wormspeed = 5
                if len(VerySpecialStuff) > 0:
                    ticksfadeout = VerySpecialStuff[list(VerySpecialStuff.keys())[0]]["time"] + 600
            elif ticksm < 7350:
                for i in list(VerySpecialStuff.keys()):
                    #print(f" {VerySpecialStuff[i]['time']} : {ticks}")
                    if VerySpecialStuff[i]["time"] > ticksfadeout:
                        addspecialstuff("circle", [[LIGHTPURPLE, 100]], [VerySpecialStuff[i]["cords"][0] + random.randint(-10, 10), VerySpecialStuff[i]["cords"][1] + random.randint(-10, 10)], [50], [[0, 0, 10]], 10, gravity=[True, -0.1, -0.1])
                        #print("deleting")
                        del VerySpecialStuff[i]
                        #soundplayed = False
                    continue
                if len(VerySpecialStuff) == 0:
                    #if not soundplayed:
                        #pygame.mixer.Sound.play(laugh_sound)
                        #soundplayed = True
                    safeguard3 = False
            elif ticksm < 7500 and not safeguard3:
                safeguard3 = True
                wormlength = 73
                wormspeed = 1.25
                addspecialstuff("circle", [[WHITE, 100]], [300, -50], [25], [[0, 0, 30]], 10, [True, -10, -10])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [35], "movetocenterfromtop rose4curve",
                                    damage=45, timecounter=97 * wormspeed, sprited=[True, tail2])
                for i in range(wormlength):
                    addveryspecialstuff("circle", [[BLUE, 100]], [-1200, 250], [35],
                                        "movetocenterfromtop rose4curve", damage=10,
                                        timecounter=(99 + 4 * i) * wormspeed, sprited=[True, body2])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [40], "movetocenterfromtop rose4curve",
                                    damage=45, timecounter=(99 + wormlength * 4) * wormspeed, sprited=[True, head2])
            elif ticksm < 8000:
                if (ticks+45)%200 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                if (ticks+30)%200 == 0:
                    addoverlaystuff("rect", LIGHTPURPLE, [x, -50], [12, 50], [0, 18], damage=10)
                    addoverlaystuff("rect", LIGHTPURPLE, [x, 550], [12, 50], [0, -18], damage=10)
                    addoverlaystuff("rect", LIGHTPURPLE, [-50, y], [50, 12], [18, 0], damage=10)    
                    addoverlaystuff("rect", LIGHTPURPLE, [650, y], [50, 12], [-18, 0], damage=10)
                if (ticks)%200 == 0:
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0.1, 0])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [-0.1, 0])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0, 0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0, -0.1])
            elif ticksm < 11400:
                if (ticks+45)%200 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                if (ticks+30)%200 == 0:
                    addoverlaystuff("rect", LIGHTPURPLE, [x, -50], [12, 50], [0, 18], damage=10)
                    addoverlaystuff("rect", LIGHTPURPLE, [x, 550], [12, 50], [0, -18], damage=10)
                    addoverlaystuff("rect", LIGHTPURPLE, [-50, y], [50, 12], [18, 0], damage=10)    
                    addoverlaystuff("rect", LIGHTPURPLE, [650, y], [50, 12], [-18, 0], damage=10)
                    wormspeed = 2.5
                if (ticks)%200 == 0:
                    wormspeed = 1.25
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0.1, 0])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [-0.1, 0])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0, 0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0, -0.1])
                if len(VerySpecialStuff) > 0:
                    ticksfadeout = VerySpecialStuff[list(VerySpecialStuff.keys())[0]]["time"] + 600
            elif ticksm < 12000:

                for i in list(VerySpecialStuff.keys()):
                    if VerySpecialStuff[i]["time"] > ticksfadeout:
                        addspecialstuff("circle", [[LIGHTPURPLE, 100]], [VerySpecialStuff[i]["cords"][0] + random.randint(-10, 10), VerySpecialStuff[i]["cords"][1] + random.randint(-10, 10)], [50], [[0, 0, 10]], 10, gravity=[True, -0.1, -0.1])
                        del VerySpecialStuff[i]
                    continue
                if len(VerySpecialStuff) == 0:
                    safeguard4 = False
            elif ticksm < 12500 and not safeguard4:
                texttoprint = ["A GOD DOES NOT FEAR DEATH", 100]
                safeguard4 = True
                wormlength = 20
                wormspeed = 3
                tickstotp = 0
                addspecialstuff("circle", [[WHITE, 100]], [300, -50], [25], [[0, 0, 30]], 10, [True, -10, -10])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [35], "movetocenterfromtop rose4curve",
                                    damage=45, timecounter=97 * wormspeed, sprited=[True, tail2])
                for i in range(wormlength):
                    addveryspecialstuff("circle", [[BLUE, 100]], [-1200, 250], [35],
                                        "movetocenterfromtop rose4curve", damage=10,
                                        timecounter=(99 + 4 * i) * wormspeed, sprited=[True, body2])
                addveryspecialstuff("circle", [[RED, 100]], [-1200, 250], [40], "movetocenterfromtop rose4curve",
                                    damage=45, timecounter=(99 + wormlength * 4) * wormspeed, sprited=[True, head2])
            elif ticksm < 12500:
                pass
            elif ticksm < 14950:
                HP += 0.05
                if (ticks)%250 == 0:
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addstuff("circle", WHITE, headcords, [25], [x*5 for x in makeunitvector([x-headcords[0], y-headcords[1]])], gravity=[True, -2, -2])
                if (ticks)%200 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, -400], [10, 50], [[0, 15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [x, 900], [10, 50], [[0, -15, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [-400, y], [50, 10], [[15, 0, 100]])
                    addspecialstuff("rect", [[LIGHTPURPLE, 100]], [900, y], [50, 10], [[-15, 0, 100]])
                if (ticks)%300 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    localheadcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [12, 50], [0, 5], damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [12, 50], [0, -5],damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [50, 12], [5, 0], damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [50, 12], [-5, 0],damage=12)
                if (ticks+10)%300 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    localheadcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [12, 50], [0, 5], damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [12, 50], [0, -5], damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [50, 12], [5, 0], damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [50, 12], [-5, 0], damage=12)
                if (ticks+20)%300 == 0:
                    pygame.mixer.Sound.play(laser_sound)
                    localheadcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [12, 50], [0, 5],damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [12, 50], [0, -5],damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [50, 12], [5, 0],damage=12)
                    addoverlaystuff("rect", LIGHTPURPLE, [localheadcords[0], localheadcords[1]], [50, 12], [-5, 0],damage=12)
                if ticks%900 == 0:
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    tickstotp = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["time"] + 250
                if (ticks - 80)%900 == 0:
                    headcords = VerySpecialStuff[list(VerySpecialStuff.keys())[-1]]["cords"]
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0.1, 0])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [-0.1, 0])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0, 0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0, -0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [-0.1, -0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0.1, -0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [-0.1, 0.1])
                    addoverlaystuff("accelcircle", LIGHTPURPLE, headcords, [25], [0.1, 0.1])
                for i in list(VerySpecialStuff.keys()):
                    if VerySpecialStuff[i]["time"] > tickstotp and VerySpecialStuff[i]["time"] < (wormspeed + tickstotp):
                        VerySpecialStuff[i]["time"] += 800
                        addspecialstuff("circle", [[LIGHTPURPLE, 100]], [VerySpecialStuff[i]["cords"][0] + random.randint(-10, 10), VerySpecialStuff[i]["cords"][1] + random.randint(-10, 10)], [50], [[0, 0, 10]], 10, gravity=[True, -0.1, -0.1])
                        temptime = VerySpecialStuff[i]["time"] / 200
                        unitvectvar = makeunitvector([(math.cos(temptime)), (math.sin(temptime))])
                        goto = [x * 350 * math.sin(pi87 * temptime) for x in unitvectvar]
                        print(VerySpecialStuff[i]["cords"])
                        print([300 + goto[0], 250 + goto[1]])
                        addspecialstuff("circle", [[LIGHTPURPLE, 100]],
                                        [300 + goto[0] + random.randint(-10, 10),
                                         250 + goto[1] + random.randint(-10, 10)],
                                        [50], [[0, 0, 10]],
                                        10, gravity=[True, -0.1, -0.1])
                if len(VerySpecialStuff) > 0:
                    ticksfadeout = VerySpecialStuff[list(VerySpecialStuff.keys())[0]]["time"] + 270
            elif ticksm < 15800:
                phase2 = False
                phase3 = True

        elif phase3:
            partlist = list(VerySpecialStuff.keys()) #yes I know this is unoptimized but at this point I do not care
            partlist.reverse()
            if BG[0] < 255 and BG[1] < 255 and BG[2] < 255:
                BG = (BG[0] + 0.8, BG[1] + 0.8, BG[2] + 0.8)
            else:
                BG = (255, 255, 255)
            for i in list(VerySpecialStuff.keys()):
                if VerySpecialStuff[i]["time"] > ticksfadeout:
                    randvar = random.randint(1,4)
                    if randvar == 1:
                        pygame.mixer.Sound.play(break1)
                    elif randvar == 2:
                        pygame.mixer.Sound.play(break2)
                    elif randvar == 3:
                        pygame.mixer.Sound.play(break3)
                    elif randvar == 4:
                        pygame.mixer.Sound.play(break4)
                    for j in range(int(10 / wormspeed)):
                        addspecialstuff("circle", [[PURPLE,100]], VerySpecialStuff[partlist[-1]]["cords"], [4], [[random.uniform(-2, 2), random.uniform(-2, 2), random.randint(360,600)]], damage=1)
                    del VerySpecialStuff[partlist[-1]]

                    wormspeed -= 0.14
                    ticksfadeout += wormspeed * 20
            if len(VerySpecialStuff) == 0:
                pygame.mixer.Sound.play(death)
                phase3 = False
                ticks = 0
        else:
            texttoprint = ["You win", 60]
            if ticks > 1200:
                hyperfancystuff = False
                mainmenu = True

        #reminder to do death animation at 15000 ticksm
        texttoprint[1] -= 1
        screen.fill(BG)
        screen.blit(font.render(texttoprint[0], True, CYAN), (WIDTH / 2 - len(texttoprint[0]) * 9, HEIGHT / 2 - 50))

        #Projectiles moving & drawing:
        stf = 0  #just a counter variable
        for i in list(Stuff.keys()):
            Stuff[i]["cords"] = [Stuff[i]["cords"][0] + Stuff[i]["vector"][0],Stuff[i]["cords"][1] + Stuff[i]["vector"][1]]
            addstf = True
            if Stuff[i]["cords"][0] > WIDTH + 100 or Stuff[i]["cords"][0] < -100 or Stuff[i]["cords"][1] > HEIGHT + 100 or Stuff[i]["cords"][1] < -100:
                del Stuff[i]
                continue

            #draw the stuff + collisions (because of course circles are centered but rectangles aren't, which makes sense but still is annoying)
            if "rect" in i:
                pygame.draw.rect(screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1], Stuff[i]["size"][0], Stuff[i]["size"][1]))
                if Stuff[i]["cords"][0] <= x and (Stuff[i]["cords"][0] + Stuff[i]["size"][0]) >= x and Stuff[i]["cords"][1] <= y and (Stuff[i]["cords"][1] + Stuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= Stuff[i]["damage"]
                        iframes = 10

            if "circle" in i:
                pygame.draw.circle( screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1]), Stuff[i]["size"][0])
                if (Stuff[i]["cords"][0] + Stuff[i]["size"][0] > x and Stuff[i]["cords"][0] - Stuff[i]["size"][0] < x) and (Stuff[i]["cords"][1] + Stuff[i]["size"][0] > y and Stuff[i]["cords"][1] - Stuff[i]["size"][0] < y):
                    #print("collision with circle obj")
                    #print("y collision")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= Stuff[i]["damage"]
                        iframes = 10

            #accelerate stuff with the "accel" tag
            if "accel" in i:
                Stuff[i]["vector"] = [Stuff[i]["vector"][0] * 1.05,Stuff[i]["vector"][1] * 1.05]
            #home in the homing stuff
            if "homing" in i:
                unitvect = makeunitvector([x - Stuff[i]["cords"][0], y - Stuff[i]["cords"][1]])
                Stuff[i]["vector"] = [Stuff[i]["vector"][0] + 0.1 * unitvect[0], Stuff[i]["vector"][1] + 0.1 * unitvect[1]]

            if Stuff[i]["gravity"][0]:
                #print(SpecialStuff[i]["gravity"])
                dist = math.sqrt(((crdvar[0] - x) ** 2) + ((crdvar[1] - y) ** 2))
                if x > crdvar[0]:
                    gravityh -= Stuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                elif x < crdvar[0]:
                    gravityh += Stuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                if y > crdvar[1]:
                    gravity -= Stuff[i]["gravity"][2] / ((dist * 0.04) + 1)
                elif y < crdvar[1]:
                    gravity += Stuff[i]["gravity"][2] / ((dist * 0.04) + 1)
            stf += 1
        spcstf = 0
        for i in list(SpecialStuff.keys()):
            crdvar = SpecialStuff[i]["cords"]
            if len(SpecialStuff[i]["vector"]) > 0:
                if SpecialStuff[i]["vector"][0][2] > 0:
                    SpecialStuff[i]["cords"] = [crdvar[0] + SpecialStuff[i]["vector"][0][0],crdvar[1] + SpecialStuff[i]["vector"][0][1]]
                    SpecialStuff[i]["vector"][0][2] = SpecialStuff[i]["vector"][0][2] - 1
                if SpecialStuff[i]["vector"][0][2] <= 0:
                    del SpecialStuff[i]["vector"][0]
            else:
                del SpecialStuff[i]
                continue
            if len(SpecialStuff[i]["color"]) > 1:
                if SpecialStuff[i]["color"][0][1] > 0:
                    SpecialStuff[i]["color"][0][1] = SpecialStuff[i]["color"][0][1] - 1
                if SpecialStuff[i]["color"][0][1] <= 0:
                    del SpecialStuff[i]["color"][0]
            clr = SpecialStuff[i]["color"][0][0]
            if "rect" in i:
                pygame.draw.rect(screen, clr, (crdvar[0], crdvar[1], SpecialStuff[i]["size"][0], SpecialStuff[i]["size"][1]))
                if crdvar[0] <= x and (crdvar[0] + SpecialStuff[i]["size"][0]) >= x and crdvar[1] <= y and (crdvar[1] + SpecialStuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        #print("insert damage here")
                        HP -= SpecialStuff[i]["damage"]
                        iframes = 10
            if "circle" in i:
                pygame.draw.circle(screen, clr, (crdvar[0], crdvar[1]), SpecialStuff[i]["size"][0])
                if (crdvar[0] + SpecialStuff[i]["size"][0] > x and crdvar[0] - SpecialStuff[i]["size"][0] < x) and (crdvar[1] + SpecialStuff[i]["size"][0] > y and crdvar[1] - SpecialStuff[i]["size"][0] < y):
                    if iframes <= 0:
                        #print("insert damage here")
                        HP -= SpecialStuff[i]["damage"]
                        iframes = 10
            if SpecialStuff[i]["gravity"][0]:
                #print(SpecialStuff[i]["gravity"])
                dist = math.sqrt(((crdvar[0] - x) ** 2) + ((crdvar[1] - y) ** 2))
                if x > crdvar[0]:
                    gravityh -= SpecialStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                elif x < crdvar[0]:
                    gravityh += SpecialStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                if y > crdvar[1]:
                    gravity -= SpecialStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
                elif y < crdvar[1]:
                    gravity += SpecialStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
        
        
        
        for i in list(VerySpecialStuff.keys()):
            crdvar = VerySpecialStuff[i]["cords"]
            VerySpecialStuff[i]["time"] += wormspeed
            timetemp = VerySpecialStuff[i]["time"] / 100


            #movetocenter
            if "movetocenterfromleft" in VerySpecialStuff[i]["pathing"]:
                vctr = [3000, 0]
                goto = [(-3500 * int(wormlength / 51) * wormspeed) + (300 * timetemp * 4), 250]
                VerySpecialStuff[i]["cords"] = goto
                if VerySpecialStuff[i]["sprited"][0] == True:
                    offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size() 
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], 270), [goto[0] - offsetx / 2, 250 - offsety / 2])
                if int(VerySpecialStuff[i]["cords"][0]) > 299:
                    VerySpecialStuff[i]["pathing"] = VerySpecialStuff[i]["pathing"][20:]
                    VerySpecialStuff[i]["time"] = 0
            elif "movetocenterfromfarleft" in VerySpecialStuff[i]["pathing"]:
                vctr = [3000, 0]
                goto = [(-3000 * int((51 + wormlength) / 51) * wormspeed) + (300 * timetemp * 4), 250]
                VerySpecialStuff[i]["cords"] = goto
                if VerySpecialStuff[i]["sprited"][0] == True:
                    offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size() 
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], 270), [goto[0] - offsetx / 2, 250 - offsety / 2])
                if int(VerySpecialStuff[i]["cords"][0]) > 299:
                    VerySpecialStuff[i]["pathing"] = VerySpecialStuff[i]["pathing"][20:]
                    VerySpecialStuff[i]["time"] = 0
            elif "movetocenterfromtop" in VerySpecialStuff[i]["pathing"]:
                goto = [300, (-2600 * int((51 + wormlength) / 51) * wormspeed) + (1200 * timetemp)]
                VerySpecialStuff[i]["cords"] = goto
                if VerySpecialStuff[i]["sprited"][0] == True:
                    offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size()
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], 180), [300 - offsetx / 2, goto[1] - offsety / 2])
                if int(VerySpecialStuff[i]["cords"][1]) > 249:
                    VerySpecialStuff[i]["pathing"] = VerySpecialStuff[i]["pathing"][20:]
                    VerySpecialStuff[i]["time"] = 0
            #sine rose curve pathing
            elif "rosecurve" in VerySpecialStuff[i]["pathing"]:
                unitvectvar = makeunitvector([(math.cos(timetemp)), (math.sin(timetemp))])
                goto = [x * 350 * math.sin(4*timetemp) for x in unitvectvar]
                VerySpecialStuff[i]["cords"] = [300 + goto[0], 250 + goto[1]]
                #angle = math.sin(unitvectvar[1])
                
                #angle = -(4*timetemp)
                if VerySpecialStuff[i]["sprited"][0] == True:
                    if "circle" in i:
                        offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size()
                    else:
                        offsetx, offsety = 0, 0
                    deltaX = goto[0] - (unitvectvar[0])
                    deltaY = goto[1] - (unitvectvar[1])
                    #deltaX = unitvectvar[0]
                    #deltaY = unitvectvar[1]
                    angle = math.atan2(deltaX, deltaY) *180 / math.pi
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], angle), [300 + goto[0] - offsetx / 2, 250 + goto[1] - offsety / 2])
            elif "rose2curve" in VerySpecialStuff[i]["pathing"]:
                temptime = timetemp/2
                unitvectvar = makeunitvector([(math.cos(temptime)), (math.sin(temptime))])
                goto = [x * 430 * math.sin(pi23*temptime) for x in unitvectvar]
                VerySpecialStuff[i]["cords"] = [300 + goto[0], 250 + goto[1]]
                #angle = math.sin(unitvectvar[1])
                
                #angle = -(4*timetemp)
                if VerySpecialStuff[i]["sprited"][0] == True:
                    if "circle" in i:
                        offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size()
                    else:
                        offsetx, offsety = 0, 0
                    deltaX = goto[0] - unitvectvar[0]
                    deltaY = goto[1] - unitvectvar[1]
                    angle = math.atan2(deltaX, deltaY) *180 / math.pi
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], angle), [300 + goto[0] - offsetx / 2, 250 + goto[1] - offsety / 2])
            elif "rose3curve" in VerySpecialStuff[i]["pathing"]:
                temptime = timetemp / 2
                unitvectvar = makeunitvector([(math.cos(temptime)), (math.sin(temptime))])
                goto = [x * 550 * math.sin(pi47 * temptime) for x in unitvectvar]
                VerySpecialStuff[i]["cords"] = [300 + goto[0], 250 + goto[1]]
                # angle = math.sin(unitvectvar[1])

                # angle = -(4*timetemp)
                if VerySpecialStuff[i]["sprited"][0] == True:
                    if "circle" in i:
                        offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size()
                    else:
                        offsetx, offsety = 0, 0
                    deltaX = goto[0] - unitvectvar[0]
                    deltaY = goto[1] - unitvectvar[1]
                    angle = math.atan2(deltaX, deltaY) * 180 / math.pi
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], angle), [300 + goto[0] - offsetx / 2, 250 + goto[1] - offsety / 2])
            elif "rose4curve" in VerySpecialStuff[i]["pathing"]:
                temptime = timetemp / 2
                unitvectvar = makeunitvector([(math.cos(temptime)), (math.sin(temptime))])
                goto = [x * 350 * math.sin(pi87 * temptime) for x in unitvectvar]
                VerySpecialStuff[i]["cords"] = [300 + goto[0], 250 + goto[1]]
                # angle = math.sin(unitvectvar[1])

                # angle = -(4*timetemp)
                if VerySpecialStuff[i]["sprited"][0] == True:
                    if "circle" in i:
                        offsetx, offsety = VerySpecialStuff[i]["sprited"][1].get_size()
                    else:
                        offsetx, offsety = 0, 0
                    deltaX = goto[0] - unitvectvar[0]
                    deltaY = goto[1] - unitvectvar[1]
                    angle = math.atan2(deltaX, deltaY) * 180 / math.pi
                    screen.blit(pygame.transform.rotate(VerySpecialStuff[i]["sprited"][1], angle), [300 + goto[0] - offsetx / 2, 250 + goto[1] - offsety / 2])
            if len(VerySpecialStuff[i]["color"]) > 1:
                if VerySpecialStuff[i]["color"][0][1] > 0:
                    VerySpecialStuff[i]["color"][0][1] = VerySpecialStuff[i]["color"][0][1] - 1
                if VerySpecialStuff[i]["color"][0][1] <= 0:
                    del VerySpecialStuff[i]["color"][0]
            clr = VerySpecialStuff[i]["color"][0][0]
            if "rect" in i:
                if VerySpecialStuff[i]["sprited"][0] == False or debug:
                    pygame.draw.rect(screen, clr, (crdvar[0], crdvar[1], VerySpecialStuff[i]["size"][0], VerySpecialStuff[i]["size"][1]))
                if crdvar[0] <= x and (crdvar[0] + VerySpecialStuff[i]["size"][0]) >= x and crdvar[1] <= y and (crdvar[1] + VerySpecialStuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        #print("insert damage here")
                        HP -= VerySpecialStuff[i]["damage"]
                        iframes = 10
            if "circle" in i:
                if VerySpecialStuff[i]["sprited"][0] == False or debug:
                    pygame.draw.circle(screen, clr, (crdvar[0], crdvar[1]), VerySpecialStuff[i]["size"][0])
                if (crdvar[0] + VerySpecialStuff[i]["size"][0] > x and crdvar[0] - VerySpecialStuff[i]["size"][0] < x) and (crdvar[1] + VerySpecialStuff[i]["size"][0] > y and crdvar[1] - VerySpecialStuff[i]["size"][0] < y):
                    if iframes <= 0:
                        #print("insert damage here")
                        HP -= VerySpecialStuff[i]["damage"]
                        iframes = 10
            if VerySpecialStuff[i]["gravity"][0]:
                #print(SpecialStuff[i]["gravity"])
                dist = math.sqrt(((crdvar[0] - x) ** 2) + ((crdvar[1] - y) ** 2))
                if x > crdvar[0]:
                    gravityh -= VerySpecialStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                elif x < crdvar[0]:
                    gravityh += VerySpecialStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                if y > crdvar[1]:
                    gravity -= VerySpecialStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
                elif y < crdvar[1]:
                    gravity += VerySpecialStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
        
        if resetgravity:
            resetgravity = False
            movement[1] = 0
            gravity = 0
        #Figure out what to move the character by:
        if movementsbool[0]:
            movement[0] += -1.1 + gravityh
            ticksgh = 0
        else:
            ticksgh += 1
            movement[0] += gravityh * math.log(ticksgh, 8)
        if movementsbool[1]:
            movement[0] += 1.1 + gravityh
            ticksgh = 0
        else:
            ticksgh += 1
            movement[0] += gravityh * math.log(ticksgh, 8)
        if movementsbool[2]:
            movement[1] += -1.1 + gravity
            ticksg = 0
        else:
            ticksg += 1
            movement[1] += gravity * math.log(ticksg, 8)
        if movementsbool[3]:
            movement[1] += 1.1 + gravity
            ticksg = 0
        else:
            ticksg += 1
            movement[1] += gravity * math.log(ticksg, 8)
        
        absmovement = [abs(x) for x in movement]
        if absmovement[0] > 0:
            movement[0] = movement[0] * 0.8
        if absmovement[1] > 0:
            movement[1] = movement[1] * 0.8
        if absmovement[0] > 5.8 or absmovement[1] > 5.8:
            if absmovement[0] > 15 or absmovement[1] > 15:
                #print("Very fast!")
                CD -= 0.05
            #print(f"fast: {absmovement[0]} ; {absmovement[1]}")
            if 4 < CD and 5 > CD: 
                #print("dashiframes")
                iframes = 10
        iframes -= 1
        
        #platforms   
        for i in list(PlatformStuff.keys()):
            crdvar = PlatformStuff[i]["cords"]
            if len(PlatformStuff[i]["vector"]) > 0:
                if PlatformStuff[i]["vector"][0][2] > 0:
                    PlatformStuff[i]["cords"] = [crdvar[0] + PlatformStuff[i]["vector"][0][0],crdvar[1] + PlatformStuff[i]["vector"][0][1]]
                    PlatformStuff[i]["vector"][0][2] = PlatformStuff[i]["vector"][0][2] - 1
                if PlatformStuff[i]["vector"][0][2] <= 0:
                    del PlatformStuff[i]["vector"][0]
            if len(PlatformStuff[i]["vector"]) <= 0:
                del PlatformStuff[i]
                continue
            if len(PlatformStuff[i]["color"]) > 1:
                if PlatformStuff[i]["color"][0][1] > 0:
                    PlatformStuff[i]["color"][0][1] = PlatformStuff[i]["color"][0][1] - 1
                if PlatformStuff[i]["color"][0][1] <= 0:
                    del PlatformStuff[i]["color"][0]
            clr = PlatformStuff[i]["color"][0][0]
            if "rect" in i:
                pygame.draw.rect(screen, clr, (crdvar[0], crdvar[1], PlatformStuff[i]["size"][0], PlatformStuff[i]["size"][1]))
                if crdvar[0] <= x and (crdvar[0] + PlatformStuff[i]["size"][0]) >= x and crdvar[1] <= y+r and (crdvar[1] + PlatformStuff[i]["size"][1]) >= y+r:
                    if not movementsbool[3] and not movementsbool[2]:
                        movement[1] = 0
                    if not movementsbool[1] and not movementsbool[0]:
                        movement[0] = 0
                    x += PlatformStuff[i]["vector"][0][0]
                    y += PlatformStuff[i]["vector"][0][1] 
            if "circle" in i:
                pygame.draw.circle(screen, clr, (crdvar[0], crdvar[1]), PlatformStuff[i]["size"][0])
                if (crdvar[0] + PlatformStuff[i]["size"][0] > x and crdvar[0] - PlatformStuff[i]["size"][0] < x) and (crdvar[1] + PlatformStuff[i]["size"][0] > y and crdvar[1] - PlatformStuff[i]["size"][0] < y):
                    if iframes <= 0:
                        #print("insert damage here")
                        y -= 1 + abs(gravity) * math.log(ticksg, 8) * 5
            if PlatformStuff[i]["gravity"][0]:
                #print(SpecialStuff[i]["gravity"])
                dist = math.sqrt(((crdvar[0] - x) ** 2) + ((crdvar[1] - y) ** 2))
                if x > crdvar[0]:
                    gravityh -= PlatformStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                elif x < crdvar[0]:
                    gravityh += PlatformStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                if y > crdvar[1]:
                    gravity -= PlatformStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
                elif y < crdvar[1]:
                    gravity += PlatformStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
                    
                    
        stf = 0  #just a counter variable
        for i in list(OverlayStuff.keys()):
            OverlayStuff[i]["cords"] = [OverlayStuff[i]["cords"][0] + OverlayStuff[i]["vector"][0],OverlayStuff[i]["cords"][1] + OverlayStuff[i]["vector"][1]]
            addstf = True
            if OverlayStuff[i]["cords"][0] > WIDTH + 100 or OverlayStuff[i]["cords"][0] < -100 or OverlayStuff[i]["cords"][1] > HEIGHT + 100 or OverlayStuff[i]["cords"][1] < -100:
                del OverlayStuff[i]
                continue

            #draw the stuff + collisions (because of course circles are centered but rectangles aren't, which makes sense but still is annoying)
            if "rect" in i:
                pygame.draw.rect(screen, OverlayStuff[i]["color"], (OverlayStuff[i]["cords"][0], OverlayStuff[i]["cords"][1], OverlayStuff[i]["size"][0], OverlayStuff[i]["size"][1]))
                if OverlayStuff[i]["cords"][0] <= x and (OverlayStuff[i]["cords"][0] + OverlayStuff[i]["size"][0]) >= x and OverlayStuff[i]["cords"][1] <= y and (OverlayStuff[i]["cords"][1] + OverlayStuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= OverlayStuff[i]["damage"]
                        iframes = 10

            if "circle" in i:
                pygame.draw.circle( screen, OverlayStuff[i]["color"], (OverlayStuff[i]["cords"][0], OverlayStuff[i]["cords"][1]), OverlayStuff[i]["size"][0])
                if (OverlayStuff[i]["cords"][0] + OverlayStuff[i]["size"][0] > x and OverlayStuff[i]["cords"][0] - OverlayStuff[i]["size"][0] < x) and (OverlayStuff[i]["cords"][1] + OverlayStuff[i]["size"][0] > y and OverlayStuff[i]["cords"][1] - OverlayStuff[i]["size"][0] < y):
                    #print("collision with circle obj")
                    #print("y collision")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= OverlayStuff[i]["damage"]
                        iframes = 10

            #accelerate stuff with the "accel" tag
            if "accel" in i:
                OverlayStuff[i]["vector"] = [OverlayStuff[i]["vector"][0] * 1.05,OverlayStuff[i]["vector"][1] * 1.05]
            #home in the homing stuff
            if "homing" in i:
                unitvect = makeunitvector([x - OverlayStuff[i]["cords"][0], y - OverlayStuff[i]["cords"][1]])
                OverlayStuff[i]["vector"] = [OverlayStuff[i]["vector"][0] + 0.1 * OverlayStuff[0], OverlayStuff[i]["vector"][1] + 0.1 * unitvect[1]]

            if OverlayStuff[i]["gravity"][0]:
                #print(SpecialStuff[i]["gravity"])
                dist = math.sqrt(((crdvar[0] - x) ** 2) + ((crdvar[1] - y) ** 2))
                if x > crdvar[0]:
                    gravityh -= OverlayStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                elif x < crdvar[0]:
                    gravityh += OverlayStuff[i]["gravity"][1] / ((dist * 0.04) + 1)
                if y > crdvar[1]:
                    gravity -= OverlayStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
                elif y < crdvar[1]:
                    gravity += OverlayStuff[i]["gravity"][2] / ((dist * 0.04) + 1)
            stf += 1
        #Move the character:
        x += movement[0] * speedx
        y += movement[1] * speedy
        #Fix character position:
        if x > WIDTH:
            x = WIDTH
        if x < 0:
            x = 0
        if y > HEIGHT:
            y = HEIGHT
        if y < 0:
            y = 0
        #Draw healthbar + player:
        if HP > 0:
            pygame.draw.rect(screen, COLOR, (0, 10, HP, 20))
            pygame.draw.polygon(screen, COLOR, [(HP, 10), (HP + 2*math.log(HP,2), 10), (HP, 29)])
            pygame.draw.circle(screen, COLOR, (x, y), r)
        if HP <= 0:
            pygame.mixer.Sound.play(laugh_sound)
            hyperfancystuff = False
            deathscreen = True
            ticks = 0
            VerySpecialStuff = {}
            SpecialStuff = {}
            Stuff = {}
            COLOR = GREEN
        
        pygame.display.update()
        CD -= 0.1
        clock.tick(FPS)
        timetaken = time.time() - timev
        
        
        if timetaken > 0.1:
            print(f"Long frame! {timetaken}")
        
        #if HP <= 0:
            #pygame.mixer.music.stop()
            #print("l")
            #movementground = False
            #mainmenu = True
            #ground2 = False
            #COLOR = (255, 0, 0)
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
    #orang
    while ground2:
        ticks += 1
        timev = time.time()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movementsbool[2] = True
                if event.key == pygame.K_DOWN:
                    movementsbool[3] = True
                if event.key == pygame.K_LEFT:
                    movementsbool[0] = True
                if event.key == pygame.K_RIGHT:
                    movementsbool[1] = True
                if event.key == pygame.K_LSHIFT:
                    if CD < 0:
                        movement[0] = movement[0] * 8
                        movement[1] = movement[1] * 8
                        #iframes += 20
                        CD = 5
                
                if event.key == pygame.K_LCTRL:
                    #addstuff("rect", BLUE, [0, 0], [10, 800], [5, 0])
                    #addstuff("circle", BLUE, [300, 0], [10], [random.randint(-5, 5), 5])
                    #addstuff("arc", COLOR, [x, y], [20, 20], [makeunitvector(movement)[0] + movement[0],makeunitvector(movement)[1] + movement[1]])
                    #print(f"x : {x}, y : {y}")
                    #print(f"x : {movement[0]}, y : {movement[1]}")
                    #print(Stuff)
                    #print(makeunitvector(movement))
                    #addspecialstuff("rect", [[BLUE, 100]], [0,0], [10, 50], [[20, 0, 30], [0, 0, 100]], 10)
                    #addstuff("homingcircle", PURPLE, [0, random.randint(0, 500)], [10], [1, 0])
                    #print(SpecialStuff)
                    print(ticks)
                    #print(SpecialStuff["rect1"])
                    #print(SpecialStuff["rect1"]["vector"][0])
#                    print(iframes)
                if event.key == pygame.K_l:
                    pygame.mixer.music.stop()
                    ticks = 10420
                    pygame.mixer.music.play(1, 10420 / 60)
                if event.key == pygame.K_x:
                    pygame.mixer.music.stop()
                    ticks = 9500
                    pygame.mixer.music.play(1, ticks/60)
                    pygame.mixer.music.set_pos(ticks / 60)
                    pos = pygame.mixer.music.get_pos()
                    ticksm = int((60 / 1000) * ticks / 60)
                    ticksm = 9500
                if event.key == pygame.K_h:
                    HP += 50
                if event.key == pygame.K_0:
                    pygame.mixer.music.stop()
                    ticks = 0
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_1:
                    pygame.mixer.music.stop()
                    ticks = 780
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_2:
                    pygame.mixer.music.stop()
                    ticks = 1320
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_3:
                    pygame.mixer.music.stop()
                    ticks = 2160
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_4:
                    pygame.mixer.music.stop()
                    ticks = 4200
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_5:
                    pygame.mixer.music.stop()
                    ticks = 4750
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_6:
                    pygame.mixer.music.stop()
                    ticks = 5940
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_7:
                    pygame.mixer.music.stop()
                    ticks = 7080
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_8:
                    pygame.mixer.music.stop()
                    ticks = 8160
                    pygame.mixer.music.play(1, ticks / 60)
                if event.key == pygame.K_9:
                    pygame.mixer.music.stop()
                    ticks = 9360
                    pygame.mixer.music.play(1, ticks / 60)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    movementsbool[2] = False
                if event.key == pygame.K_DOWN:
                    movementsbool[3] = False
                if event.key == pygame.K_LEFT:
                    movementsbool[0] = False
                if event.key == pygame.K_RIGHT:
                    movementsbool[1] = False
            if event.type == MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                print(f"x: {x1} y: {y1}")
        #Figure out what to move the character by:
        if movementsbool[0]:
            movement[0] += -1.1
        if movementsbool[1]:
            movement[0] += 1.1
        if movementsbool[2]:
            movement[1] += -1.1
        if movementsbool[3]:
            movement[1] += 1.1

        absmovement = [abs(x) for x in movement]
        if absmovement[0] > 0:
            movement[0] = movement[0] * 0.8
        if absmovement[1] > 0:
            movement[1] = movement[1] * 0.8
        if absmovement[0] > 5.8 or absmovement[1] > 5.8:
            if absmovement[0] > 15 or absmovement[1] > 15:
                #print("Very fast!")
                CD -= 0.05
            #print(f"fast: {absmovement[0]} ; {absmovement[1]}")
            if 4 < CD and 5 > CD: 
                #print("dashiframes")
                iframes = 10
        iframes -= 1

        #Color shenanigans
        if iframes > 0:
            if COLOR[0] > 200 and COLOR[1] > 100:
                COLOR = (COLOR[0] - 25, COLOR[1] - 10, 0)
            if COLOR[0] > 10 and COLOR[1] > 10:
                COLOR = (COLOR[0] - 10, COLOR[1] - 7, 0)
        else:
            if COLOR[0] < 255 or COLOR[1] < 165:
                COLOR = (COLOR[0] + 25, COLOR[1] + 10, 0)
            if COLOR[0] > 255 or COLOR[1] > 165:
                COLOR = (255, 165, 0)
        #Move the character:
        x += movement[0] * speedx
        y += movement[1] * speedy
        #Fix character position:
        if x > WIDTH:
            x = WIDTH
        if x < 0:
            x = 0
        if y > HEIGHT:
            y = HEIGHT
        if y < 0:
            y = 0
        
        
        pos = pygame.mixer.music.get_pos()
        ticksm = int((60 / 1000) * pos) #ticksm = music based ticks
        if ticksm == 1:
            texttoprint = ["Arrow keys to move. SHIFT to dash", 200]
            pygame.mixer.music.set_pos(ticks / 60)
        if ticksm < 50:
            pass
        elif ticksm < 780:
            if ticks % 75 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 300], [3, 0])
                addstuff("rect", BLUE, [600, 200], [10, 300], [-3, 0])

            if ticks % 20 == 0:
                addstuff("circle", BLUE, [300, 0], [3],
                         [random.uniform(-2, 2), 1]) 
            if (ticks + 37) % 225 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 600], [3, 0])
        elif ticksm < 980:
            if ticks%12 == 0:
                addspecialstuff("rect", [[BLUE, 120], [RED, 100]], [0, random.randint(0, 410)], [20, 100], [[5.8, 0, 100], [0, 0, 20], [-6, 0, 100]], 10)
        elif ticksm < 1020:
            HP += 0.5
        elif ticksm < 1320:
            if ticks%10 == 0:
                addstuff("homingcircle", PURPLE, [0, random.randint(0, 500)], [10], [1, 0])
        elif ticksm < 1845:
            if ticks%10 == 0:
                addspecialstuff("rect", [[RED, 100]], [random.randint(0,600), -600], [50, 600], [[0, 1, 50], [0, 45, 10], [0, 0, 15]], 10)
        elif ticksm < 1920:
            HP += 0.1
        elif ticksm < 2160:
            if ticks%50 == 0:
                addstuff(random.choice(["homingaccelcircle", "homingaccelcircle", "homingcircle"]), PURPLE, [0, random.randint(0, 500)], [10], [1, 0])
                addstuff(random.choice(["homingaccelcircle", "homingaccelcircle", "homingcircle"]), PURPLE, [600, random.randint(0, 500)], [10], [-1, 0])
                
                addstuff(random.choice(["homingaccelcircle", "homingaccelcircle", "homingcircle"]), PURPLE, [random.randint(0,600), 0], [10], [0, 1])
                addstuff(random.choice(["homingaccelcircle", "homingaccelcircle", "homingcircle"]), PURPLE, [random.randint(0,600), 500], [10], [0, -1])
                
        elif ticksm < 2420:
            a = random.randint(1,2)
            if a == 2:
                randvar = random.randint(0,100)
                addspecialstuff("circle", [[BLUE, randvar], [RED, 100]], [300, 0], [8], [[0, 5, randvar], [random.randint(-5,5), 0, 100], [random.randint(-3, 3), random.randint(-1, 1), 50]], 5)
            else:
                addstuff("circle", BLUE, [300, 0], [8], [0, 5])
        elif ticksm < 2480:
            HP += 0.1
        elif ticksm == 2481:
            #pygame.mixer.music.rewind()
            #pygame.mixer.music.set_pos(ticks / 60)
            Stuff = {}
        #elif ticksm == 2570:
            #pygame.mixer.music.play(1, (ticks) / 60, fade_ms=1000)
        elif ticksm < 2720:
            movement[0] = 50
            texttoprint = [">>>>>", 1]
            if ticks % 25 == 0:
                addstuff("accelrect", BLUE, [0, random.randint(0, 400)], [20, 100], [3, 0])
        elif ticksm < 3000:
            movement[0] = 50
            texttoprint = [">>>>>", 1]
            if ticks % 15 == 0:
                addstuff("accelrect", BLUE, [0, random.randint(0, 400)], [20, 100], [3, 0])
            if ticks % 10 == 0:
                addstuff("homingcircle", PURPLE, [0, random.randint(0, 500)], [10], [3, 0])                
        elif ticksm < 3360:
            if ticks%8 == 0:
                addstuff("homingcircle", RED, [abs(math.sin(ticks/30)) * 600, 0], [10], [0, 5], 3)
                #addstuff("circle", PURPLE, [0, abs(math.cos(ticks/30)) * 500], [10], [5, 0])
        elif ticksm < 3500:
            if ticks%8 == 0:
                addstuff("homingcircle", RED, [abs(math.sin(ticks/30)) * 600, 0], [10], [0, 5], 3)
            if ticks%2 == 0:
                addstuff("circle", BLUE, [0, abs(math.cos(ticks/30)) * 500], [10], [5, 0])
        elif ticksm < 3600:
            HP += 0.2
        elif ticksm < 4100:
            if ticks%18 == 0:
                addspecialstuff("rect", [[RED, 100]], [random.randint(0,600), -600], [50, 600], [[0, 1, 50], [0, 45, 10], [0, 0, 15]], 10)
            if ticks%30 == 0:
                addstuff("homingcircle", PURPLE, [abs(math.sin(ticks/30)) * 600, 0], [10], [0, 5])
        elif ticksm < 4200:
            HP += 0.1
        elif ticksm == 4201:
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play(1, ticks / 60)
            SpecialStuff = {}
        elif ticksm < 4500:
            if ticks % 20 == 0:
                addstuff("accelcircle", BLUE, [600, y], [10],[-4, random.uniform(-0.1, 0.1)])
            if (ticks + 8) % 20 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10],[4, random.uniform(-0.1, 0.1)])
            if (ticks + 16) % 20 == 0:
                addstuff("accelcircle", BLUE, [x, 0], [10], [random.uniform(-0.1, 0.1), 4])
            if (ticks + 24) % 20 == 0:
                addstuff("accelcircle", BLUE, [x, 500], [10], [random.uniform(-0.1, 0.1), -4])
        elif ticksm < 4750:
            if ticks % 40 == 0:
                addstuff("homingaccelcircle", BLUE, [600, y], [10],[-1, random.uniform(-2, 2)], 10)
            if (ticks + 8) % 40 == 0:
                addstuff("homingaccelcircle", BLUE, [0, y], [10],[1, random.uniform(-2, 2)], 10)
            if (ticks + 16) % 40 == 0:
                addstuff("homingaccelcircle", BLUE, [x, 0], [10], [random.uniform(-2, 2), 1], 10)
            if (ticks + 24) % 40 == 0:
                addstuff("homingaccelcircle", BLUE, [x, 500], [10], [random.uniform(-2, 2), -1], 10)
        elif ticksm < 5240:
            if ticks%24 == 0:
                randvar = random.randint(60, 100)
                addspecialstuff("rect", [[BLUE, randvar], [RED, 100]], [0, random.randint(0, 410)], [20, 100], [[5, 0, randvar], [0, 0, 20], [-6, 0, 100]], 10)
            if ticks%32 == 0:
                addstuff("rect", BLUE, [0, 0], [100, 20], [0, 5], 10)
                addstuff("rect", BLUE, [500, 0], [100, 20], [0, 5], 10)
        elif ticksm < 5340:
            HP += 0.1
        elif ticksm < 5640:
            if ticks%40 == 0:
                addstuff("homingcircle", BLUE, [random.choice([0, 600]), random.choice([0, 500])], [20], [0, 0])
        elif ticksm < 5940:
            if ticks%30 == 0:
                addstuff("homingcircle", PURPLE, [abs(math.sin(ticks/30)) * 600, 0], [10], [0, 5])
            if ticks%10 == 0:
                addstuff("rect", BLUE, [0, 100], [20, 300], [8, 0])
                addstuff("rect", BLUE, [150, 0], [300, 20], [0, 8])
        elif ticksm == 5941:
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play(1, ticks / 60)
            Stuff = {}
            if x > 300:
                movement[0] = -50
            if x < 300:
                movement[0] = 50
            if y > 300:
                movement[1] = -50
            if y < 300:
                movement[1] = 50
        elif ticksm < 6240:
            if ticks%40 == 0:
                addstuff("rect", BLUE, [0, 0], [310, 20], [0, 5])
                addstuff("rect", BLUE, [290, 500], [310, 20], [0, -5])
        elif ticksm < 6480:
            if ticks%20 == 0:
                addspecialstuff("rect", [[RED, 100]], [-600, random.randint(0,500)], [600, 50], [[1, 0, 50], [55, 0, 10], [0, 0, 15]], 10)
        elif ticksm < 7080:
            if ticks % 35 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 600], [5, 0])
            if ticks%5 == 0:
                addstuff("accelcircle", BLUE, [300, 0], [10], [0, 5])
            if ticks % 50 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10], [8, 0])
                addstuff("accelcircle", BLUE, [x, 0], [10], [0, 8])
                #addstuff("homingaccelcircle", BLUE, [600, 200], [10],[-4, random.randint(-2, 2)])
                #addstuff("homingaccelcircle", BLUE, [000, 200], [10],[4, random.randint(-2, 2)])
        elif ticksm == 7081:
            HP += 10
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play(1, ticks / 60)
        elif ticksm < 7100:
            HP += 0.1
        elif ticksm == 7101:
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play(1, ticks / 60)
            Stuff = {}
            HP += 0.1
        elif ticksm < 7120:
            HP += 0.1
        elif ticksm < 7320:
            cords = [300-(math.cos(ticks/15))*349, 250-(math.sin(ticks/15))*299]
            addstuff("accelcircle", BLUE, cords, [10], [x*-7 for x in makeunitvector([cords[0]-x, cords[1]-y])], 10)
        elif ticksm < 7440:
            randvar = random.randint(0,100)
            addspecialstuff("circle", [[BLUE, randvar], [RED, 100]], [300, 0], [8], [[0, 5, randvar], [random.randint(-5,5), 0, 150]], 5)
        elif ticksm < 7680:
            HP += 0.1
        elif ticksm < 7920:
            if ticks%5 == 0:
                cords = [300-(math.cos(ticks/15))*349, 250-(math.sin(ticks/15))*299]
                addstuff("homingcircle", PURPLE, cords, [10], [x*-7 for x in makeunitvector([cords[0]-x, cords[1]-y])], 10)
            if ticks%100 == 0:
                addspecialstuff("rect", [[RED, 100]], [-600, random.randint(0,500)], [600, 50], [[1, 0, 50], [55, 0, 10], [0, 0, 15]], 10)
        elif ticksm < 8160:
            if ticks%35 == 0:
                addspecialstuff("rect", [[RED, 100]], [-600, random.randint(0,500)], [600, 50], [[1, 0, 50], [55, 0, 10], [0, 0, 15]], 10)
                addspecialstuff("rect", [[RED, 100]], [random.randint(0,600), -600], [50, 600], [[0, 1, 50], [0, 45, 10], [0, 0, 15]], 10)
        elif ticksm < 8700:
            if ticks%25 == 0:
                cords1 = [random.randint(0, 600), random.choice([0, 500])]
                unitvect = makeunitvector([cords1[0]-x, cords1[1]-y])
                bruhwhyisthisactuallycomplicated = [x*-15 for x in makeunitvector([cords1[0]-x, cords1[1]-y])]
                addspecialstuff("circle", [[BLUE, 30], [RED, 100]], [cords1[0], cords1[1]], [15], [[-unitvect[0] * 3, -unitvect[1] * 3, 30], [0, 0, 20], [bruhwhyisthisactuallycomplicated[0], bruhwhyisthisactuallycomplicated[1], 100]], 10)
            if (ticks+12)%25 == 0:
                cords1 = [random.choice([0, 600]), random.randint(0, 500)]
                unitvect = makeunitvector([cords1[0]-x, cords1[1]-y])
                bruhwhyisthisactuallycomplicated = [x*-15 for x in makeunitvector([cords1[0]-x, cords1[1]-y])]
                addspecialstuff("circle", [[BLUE, 30], [RED, 100]], [cords1[0], cords1[1]], [15], [[-unitvect[0] * 3, -unitvect[1] * 3, 30], [0, 0, 20], [bruhwhyisthisactuallycomplicated[0], bruhwhyisthisactuallycomplicated[1], 100]], 10)    
        elif ticksm < 8820:
            pass
        elif ticksm < 9360:
            if ticks %5 == 0:
                cords = [300-(math.cos(ticks/20))*349, 250-(math.sin(ticks/20))*299]
                unitvect = makeunitvector([cords[0]-300, cords[1]-250])
                bruhwhyisthisactuallycomplicated = [q*-15 for q in unitvect]
                addspecialstuff("circle", [[BLUE, 10], [RED, 100]], [cords[0], cords[1]], [15], [[-unitvect[0] * 5, -unitvect[1] * 5, 10], [0, 0, 20], [bruhwhyisthisactuallycomplicated[0], bruhwhyisthisactuallycomplicated[1], 100]], 10)
        elif ticksm < 9960:
            if ticks%3 == 0:
                addstuff("circle", RED, [abs(math.sin(ticks/30)) * 600, 0], [10], [0, 5])
                addstuff("circle", BLACK, [0, y], [10], [5, 0])
        
        elif ticksm < 10390:
            if ticks%50 == 0:
                addstuff("rect", BLUE, [0, 0], [300, 20], [0, 7])
                addstuff("rect", BLUE, [300, 500], [300, 20], [0, -7])
            if ticks%50 == 0:
                cords1 = [random.randint(0, 600), random.choice([0, 500])]
                unitvect = makeunitvector([cords1[0]-x, cords1[1]-y])
                bruhwhyisthisactuallycomplicated = [x*-15 for x in makeunitvector([cords1[0]-x, cords1[1]-y])]
                addspecialstuff("circle", [[BLUE, 10], [RED, 100]], [cords1[0], cords1[1]], [15], [[-unitvect[0] * 5, -unitvect[1] * 5, 10], [0, 0, 20], [bruhwhyisthisactuallycomplicated[0], bruhwhyisthisactuallycomplicated[1], 100]], 10)
            if (ticks+25)%50 == 0:
                cords1 = [random.choice([0, 600]), random.randint(0, 500)]
                unitvect = makeunitvector([cords1[0]-x, cords1[1]-y])
                bruhwhyisthisactuallycomplicated = [x*-15 for x in makeunitvector([cords1[0]-x, cords1[1]-y])]
                addspecialstuff("circle", [[BLUE, 10], [RED, 100]], [cords1[0], cords1[1]], [15], [[-unitvect[0] * 5, -unitvect[1] * 5, 10], [0, 0, 20], [bruhwhyisthisactuallycomplicated[0], bruhwhyisthisactuallycomplicated[1], 100]], 10)    
        #elif ticksm == 10440:
        #    pygame.mixer.music.fadeout(3500)
        elif ticksm < 10450:
            pass
        elif ticksm < 10500 and not safeguard:
            safeguard = True
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play(1, ticks / 60, fade_ms=500)
            texttoprint = ["FOCUS", 100]
            addspecialstuff("rect", [[RED, 100], [RED, 650], [RED, 50]], [0,0], [40, 40],
                            [[11, 1, 50], [0, 0, 50], [0, 10, 10], [0, 0, 10], [0, 10, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10], [0, -30, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10], [0, -30, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10], [0, -30, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10], [0, -30, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10], [0, -30, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10], [0, 0, 10],
                             [0, 10, 10],
                             [0, 0, 150]],
                            10)
            addspecialstuff("rect", [[GREEN, 100], [RED, 650], [GREEN, 50]], [0,10], [40, 40],
                            [[11, 3, 50], [0, 0, 50], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10], [0, 00, 10], [0, 0, 10],
                             [0, -10, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10], [0, 00, 10], [0, 0, 10],
                             [0, -10, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10], [0, 00, 10], [0, 0, 10],
                             [0, -10, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10], [0, 00, 10], [0, 0, 10],
                             [0, -10, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, 10, 10], [0, 0, 10], [0, 10, 10], [0, 00, 10], [0, 0, 10],
                             [0, -10, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10], [0, 10, 10], [0, 0, 10],
                             [0, 0, 10],
                             [0, 0, 600]],
                            10)
            addspecialstuff("rect", [[RED, 100], [RED, 650], [RED, 50]], [0,20], [40, 40],
                            [[11, 5, 50], [0, 0, 50], [0, 10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10],[0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 10, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10],[0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 10, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10],[0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 10, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10],[0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 10, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10],[0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10],
                             [0, 10, 10], [0, 10, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10],
                             [0, -12, 10],
                             [0, 0, 150]],
                            10)
            addspecialstuff("rect", [[RED, 100], [RED, 650], [RED, 50]], [0,30], [40, 40],
                            [[11, 7, 50], [0, 0, 50], [0, -10, 10], [0, 0, 10], [0, -10, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10], [0, 30, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, -10, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10], [0, 30, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, -10, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10], [0, 30, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, -10, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10], [0, 30, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, -10, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, 0, 10], [0, 30, 10], [0, 0, 10],
                             [0, 0, 10], [0, -10, 10], [0, 0, 10], [0, -10, 10], [0, -10, 10], [0, 0, 10],
                             [0, 0, 10],
                             
                             [0, 0, 150]],
                            10)
            addspecialstuff("rect", [[RED, 100]], [-1200, 0], [1200, 120], [[0.51, 0, 750], [50, 0, 12], [0, 0, 50]], 75)
            addspecialstuff("rect", [[RED, 100]], [-1200, 120], [1200, 130], [[0.51, 0, 750], [-10, 0, 12], [0, 0, 50]], 75)
            addspecialstuff("rect", [[RED, 100]], [-1200, 250], [1200, 100], [[0.51, 0, 750], [50, 0, 12], [0, 0, 50]], 75)
            addspecialstuff("rect", [[RED, 100]], [-1200, 350], [1200, 150], [[0.51, 0, 750], [50, 0, 12], [0, 0, 50]], 75)
        elif ticksm < 10500:
            pass
        elif ticksm < 11000:
            if ticks%20 == 0:
                addstuff("circle", BLUE, [x, 0], [10], [0, 5], 1)
        elif ticksm == 11380:
            texttoprint = ["You win", 200]
        elif ticksm == 11580:
            ground2 = False
            mainmenu = True
        
        if texttoprint[1] < 0:
            texttoprint[0] = ""
        
        texttoprint[1] -= 1
        screen.fill(WHITE)
        screen.blit(font.render(texttoprint[0], True, GREEN), (WIDTH / 2 - len(texttoprint[0]) * 9, HEIGHT / 2 - 50))

        #Projectiles moving & drawing:
        stf = 0  #just a counter variable
        for i in list(Stuff.keys()):
            Stuff[i]["cords"] = [Stuff[i]["cords"][0] + Stuff[i]["vector"][0],Stuff[i]["cords"][1] + Stuff[i]["vector"][1]]
            addstf = True
            if Stuff[i]["cords"][0] > WIDTH + 100 or Stuff[i]["cords"][0] < -100 or Stuff[i]["cords"][1] > HEIGHT + 100 or Stuff[i]["cords"][1] < -100:
                del Stuff[i]
                continue

            #draw the stuff + collisions (because of course circles are centered but rectangles aren't, which makes sense but still is annoying)
            if "rect" in i:
                pygame.draw.rect(screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1], Stuff[i]["size"][0], Stuff[i]["size"][1]))
                if Stuff[i]["cords"][0] <= x and (Stuff[i]["cords"][0] + Stuff[i]["size"][0]) >= x and Stuff[i]["cords"][1] <= y and (Stuff[i]["cords"][1] + Stuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= Stuff[i]["damage"]
                        iframes = 10

            if "circle" in i:
                pygame.draw.circle( screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1]), Stuff[i]["size"][0])
                if (Stuff[i]["cords"][0] + Stuff[i]["size"][0] > x and Stuff[i]["cords"][0] - Stuff[i]["size"][0] < x) and (Stuff[i]["cords"][1] + Stuff[i]["size"][0] > y and Stuff[i]["cords"][1] - Stuff[i]["size"][0] < y):
                    #print("collision with circle obj")
                    #print("y collision")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= Stuff[i]["damage"]
                        iframes = 10

            #accelerate stuff with the "accel" tag
            if "accel" in i:
                Stuff[i]["vector"] = [Stuff[i]["vector"][0] * 1.05,Stuff[i]["vector"][1] * 1.05]
            #home in the homing stuff
            if "homing" in i:
                unitvect = makeunitvector([x - Stuff[i]["cords"][0], y - Stuff[i]["cords"][1]])
                Stuff[i]["vector"] = [Stuff[i]["vector"][0] + 0.1 * unitvect[0], Stuff[i]["vector"][1] + 0.1 * unitvect[1]]
            stf += 1
        spcstf = 0
        for i in list(SpecialStuff.keys()):
            crdvar = SpecialStuff[i]["cords"]
            if len(SpecialStuff[i]["vector"]) > 0:
                if SpecialStuff[i]["vector"][0][2] > 0:
                    SpecialStuff[i]["cords"] = [crdvar[0] + SpecialStuff[i]["vector"][0][0],crdvar[1] + SpecialStuff[i]["vector"][0][1]]
                    SpecialStuff[i]["vector"][0][2] = SpecialStuff[i]["vector"][0][2] - 1
                if SpecialStuff[i]["vector"][0][2] <= 0:
                    del SpecialStuff[i]["vector"][0]
            else:
                del SpecialStuff[i]
                continue
            if len(SpecialStuff[i]["color"]) > 1:
                if SpecialStuff[i]["color"][0][1] > 0:
                    SpecialStuff[i]["color"][0][1] = SpecialStuff[i]["color"][0][1] - 1
                if SpecialStuff[i]["color"][0][1] <= 0:
                    del SpecialStuff[i]["color"][0]
            clr = SpecialStuff[i]["color"][0][0]
            if "rect" in i:
                pygame.draw.rect(screen, clr, (crdvar[0], crdvar[1], SpecialStuff[i]["size"][0], SpecialStuff[i]["size"][1]))
                if crdvar[0] <= x and (crdvar[0] + SpecialStuff[i]["size"][0]) >= x and crdvar[1] <= y and (crdvar[1] + SpecialStuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= SpecialStuff[i]["damage"]
                        iframes = 10
            if "circle" in i:
                pygame.draw.circle(screen, clr, (crdvar[0], crdvar[1]), SpecialStuff[i]["size"][0])
                if (crdvar[0] + SpecialStuff[i]["size"][0] > x and crdvar[0] - SpecialStuff[i]["size"][0] < x) and (crdvar[1] + SpecialStuff[i]["size"][0] > y and crdvar[1] - SpecialStuff[i]["size"][0] < y):
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= SpecialStuff[i]["damage"]
                        iframes = 10
        #Draw healthbar:
        if HP > 0:
            pygame.draw.rect(screen, COLOR, (0, 10, HP, 20))
            pygame.draw.polygon(screen, COLOR, [(HP, 10), (HP + 2*math.log(HP,2), 10), (HP, 29)])
        pygame.draw.circle(screen, COLOR, (x, y), r)
        pygame.display.update()
        CD -= 0.1
        clock.tick(FPS)
        timetaken = time.time() - timev
        if timetaken > 0.1:
            print(f"Long frame! {timetaken}")
        if HP <= 0:
            ground2 = False
            deathscreen = True
            ticks = 0
            VerySpecialStuff = {}
            SpecialStuff = {}
            Stuff = {}
            COLOR = ORANGE
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #RED CIRCLE
    while movementground:
        ticks += 1
        timev = time.time()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movementsbool[2] = True
                if event.key == pygame.K_DOWN:
                    movementsbool[3] = True
                if event.key == pygame.K_LEFT:
                    movementsbool[0] = True
                if event.key == pygame.K_RIGHT:
                    movementsbool[1] = True
                if event.key == pygame.K_LSHIFT:
                    if CD < 0:
                        movement[0] = movement[0] * 8
                        movement[1] = movement[1] * 8
                        #iframes += 20
                        CD = 5
                if event.key == pygame.K_0:
                    ticks = 0
                if event.key == pygame.K_1:
                    ticks = 11300
                if event.key == pygame.K_2:
                    ticks = 19000
                if event.key == pygame.K_3:
                    ticks = 22400
                if event.key == pygame.K_4:
                    ticks = 23000

                if event.key == pygame.K_5:
                    ticks = 24100
                if event.key == pygame.K_6:
                    ticks = 12500
                if event.key == pygame.K_7:
                    ticks = 14600
                if event.key == pygame.K_7:
                    ticks = 17000
                if event.key == pygame.K_8:
                    ticks = 18000
                if event.key == pygame.K_9:
                    ticks = 21000
                if event.key == pygame.K_LCTRL:
                    addstuff("rect", BLUE, [0, 0], [10, 800], [5, 0])
                    print(iframes)
                if event.key == pygame.K_h:
                    HP += 50
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    movementsbool[2] = False
                if event.key == pygame.K_DOWN:
                    movementsbool[3] = False
                if event.key == pygame.K_LEFT:
                    movementsbool[0] = False
                if event.key == pygame.K_RIGHT:
                    movementsbool[1] = False
            if event.type == MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                print(f"x: {x1} y: {y1}")
        #Figure out what to move the character by:
        if movementsbool[0]:
            movement[0] += -1.1
        if movementsbool[1]:
            movement[0] += 1.1
        if movementsbool[2]:
            movement[1] += -1.1
        if movementsbool[3]:
            movement[1] += 1.1

        absmovement = [abs(x) for x in movement]
        if absmovement[0] > 0:
            movement[0] = movement[0] * 0.8
        if absmovement[1] > 0:
            movement[1] = movement[1] * 0.8
        if absmovement[0] > 5.8 or absmovement[1] > 5.8:
            if absmovement[0] > 15 or absmovement[1] > 15:
                #print("Very fast!")
                CD -= 0.05
            #print(f"fast: {absmovement[0]} ; {absmovement[1]}")
            if 4 < CD and 5 > CD: 
                print("dashiframes")
                iframes = 10
        iframes -= 1

        #Color shenanigans
        if iframes > 0:
            if COLOR[0] > 200:
                COLOR = (COLOR[0] - 25, 0, 0)
            if COLOR[0] > 10:
                COLOR = (COLOR[0] - 10, 0, 0)
            if COLOR[2] > 200:
                COLOR = (0, 0, COLOR[2] - 25)
            if COLOR[2] > 10:
                COLOR = (0, 0, COLOR[2] - 25)
        else:
            if COLOR[0] < 255:
                COLOR = (COLOR[0] + 25, 0, 0)
            if COLOR[0] > 255:
                COLOR = (255, 0, 0)
        #Move the character:
        x += movement[0] * speedx
        y += movement[1] * speedy
        #Fix character position:
        if x > WIDTH:
            x = WIDTH
        if x < 0:
            x = 0
        if y > HEIGHT:
            y = HEIGHT
        if y < 0:
            y = 0
        texttoprint = ""
        if ticks < 200:
            texttoprint = "Use arrow keys to dodge"
            if ticks % 75 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 300], [3, 0])
                addstuff("rect", BLUE, [600, 200], [10, 300], [-3, 0])

            if ticks % 100 == 0:
                addstuff("circle", BLUE, [300, 0], [10],
                         [random.randint(-3, 3), 1])  
        if ticks < 1500:
            if ticks % 75 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 300], [3, 0])
                addstuff("rect", BLUE, [600, 200], [10, 300], [-3, 0])

            if ticks % 100 == 0:
                addstuff("circle", BLUE, [300, 0], [10],
                         [random.randint(-3, 3), 1])


        elif ticks < 1700:
            texttoprint = "SHIFT to dash past obstacles"
            if ticks % 75 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 600], [3, 0])
            if ticks % 50 == 0:
                addstuff("circle", BLUE, [600, 200], [10],[-4, random.randint(-2, 2)])
                addstuff("circle", BLUE, [000, 200], [10],[4, random.randint(-2, 2)])
        elif ticks < 3000:
            if ticks % 75 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 600], [3, 0])
            if ticks % 50 == 0:
                addstuff("circle", BLUE, [600, 200], [10],[-4, random.randint(-2, 2)])
                addstuff("circle", BLUE, [000, 200], [10],[4, random.randint(-2, 2)])
        elif ticks < 3100:
            HP += 0.5
            texttoprint = "Good luck!"
        elif ticks < 5000:
            if ticks%25 == 0:
                addstuff("rect", BLUE, [0, 0], [100, 20], [0, 5])
                addstuff("rect", BLUE, [500, 500], [100, 20], [0, -5])
                addstuff("rect", BLUE, [0, 0], [20, 100], [5, 0])
                addstuff("rect", BLUE, [500, 400], [20, 100], [-5, 0])
            if ticks % 40 == 0:
                addstuff("circle", BLUE, [600, 250], [10],[-4, random.uniform(-2, 2)])
            if (ticks + 8) % 40 == 0:
                addstuff("circle", BLUE, [0, 250], [10],[4, random.uniform(-2, 2)])
            if (ticks + 16) % 40 == 0:
                addstuff("circle", BLUE, [300, 0], [10], [random.uniform(-2, 2), 4])
            if (ticks + 24) % 40 == 0:
                addstuff("circle", BLUE, [300, 500], [10], [random.uniform(-2, 2), -4])
        elif ticks < 6500:
            if ticks%25 == 0:
                addstuff("rect", BLUE, [0, 0], [200, 40], [0, 6])
                addstuff("rect", BLUE, [400, 0], [200, 40], [0, 6])
            if ticks%75 == 0:
                addstuff("rect", BLUE, [0, 0], [300, 10], [0, 4])
                addstuff("rect", BLUE, [300, 500], [300, 10], [0, -4])
                addstuff("circle", BLUE, [300, 0], [10], [0, 0.8])
        elif ticks < 6550:
            Stuff = {}
            texttoprint = "Take a break"
            HP += 1
            HPrecording = HP
        elif ticks < 6650:
            texttoprint = "Take a break"
            if ticks%10 == 0:
                addstuff("rect", BLUE, [0, 100], [20, 300], [8, 0])
                addstuff("rect", BLUE, [150, 0], [300, 20], [0, 8])
            HPrecording2 = HP
        elif ticks < 6740:
            if HPrecording > HPrecording2:
                texttoprint = "Bro got caught lacking"
                HP += 0.3
            else:
                texttoprint = "Take a break"
        elif ticks < 7600:
            if ticks%10 == 0:
                addstuff("circle", BLUE, [0, y], [10], [8, 0])
                addstuff("circle", BLUE, [x, 0], [10], [0, 8])
        elif ticks < 8800:
            if ticks%4 == 0:
                addstuff("rect", BLUE, [random.randint(0, 600), 0], [20, 20], [0,3])
        elif ticks < 9400:
            if ticks%3 == 0:
                addstuff("rect", BLUE, [random.randint(0, 600), 0], [20, 20], [0,4])
        elif ticks < 10000:
            if ticks%2 == 0:
                addstuff("rect", BLUE, [random.randint(0, 600), 0], [20, 20], [0,6])
        elif ticks < 10100:
            texttoprint = "Stuff is going to get real now"
            HP += 1
        elif ticks < 11000:
            if ticks%4 == 0:
                addstuff("rect", BLUE, [random.randint(0, 600), 0], [20, 20], [0,1])
                addstuff("rect", ORANGE, [0, random.randint(0, 600)], [20, 20], [1,0])
        elif ticks < 11200:
            if ticks%10 == 0:
                addstuff("rect", BLUE, [0, 100], [20, 300], [8, 0])
                addstuff("rect", BLUE, [150, 0], [300, 20], [0, 8])
        elif ticks < 11500:
            if ticks%25 == 0:
                addstuff("circle", BLUE, [0, y], [10], [8, 0])
                addstuff("circle", BLUE, [x, 0], [10], [0, 8])
        elif ticks < 11800:
            HP += 0.1
            texttoprint = "Good luck."
            Stuff = {}
        elif ticks < 13200:
            if ticks % 35 == 0:
                addstuff("rect", BLUE, [0, 0], [10, 600], [3, 0])

                addstuff("circle", BLUE, [300, 0], [10], [0, 0.8])
            if ticks % 50 == 0:
                addstuff("circle", BLUE, [0, y], [10], [8, 0])
                addstuff("circle", BLUE, [x, 0], [10], [0, 8])
                addstuff("circle", BLUE, [600, 200], [10],[-4, random.randint(-2, 2)])
                addstuff("circle", BLUE, [000, 200], [10],[4, random.randint(-2, 2)])
        elif ticks < 13500:
            if ticks%25 == 0:
                addstuff("circle", BLUE, [0, y], [10], [8, 0])
                addstuff("circle", BLUE, [x, 0], [10], [0, 8])

        elif ticks < 14600:
            if ticks%1000 == 0:
                addstuff("circle", BLUE, [0, y], [10], [8, 0])
                addstuff("circle", BLUE, [x, 0], [10], [0, 8])
                addstuff("rect", BLUE, [150, 0], [100, 20], [0, 5])
                addstuff("rect", BLUE, [350, 500], [100, 20], [0, -5])
            if ticks%15 == 0:
                addstuff("rect", BLUE, [0, 0], [150, 20], [0, 5])
                addstuff("rect", BLUE, [450, 500], [150, 20], [0, -5])
                addstuff("rect", BLUE, [0, 0], [20, 150], [5, 0])
                addstuff("rect", BLUE, [500, 350], [20, 150], [-5, 0])
            if ticks % 30 == 0:
                addstuff("circle", BLUE, [600, 250], [10],[-4, random.uniform(-2, 2)])
            if (ticks + 8) % 30 == 0:
                addstuff("circle", BLUE, [0, 250], [10],[4, random.uniform(-2, 2)])
            if (ticks + 16) % 30 == 0:
                addstuff("circle", BLUE, [300, 0], [10], [random.uniform(-2, 2), 4])
            if (ticks + 24) % 30 == 0:
                addstuff("circle", BLUE, [300, 500], [10], [random.uniform(-2, 2), -4])
        elif ticks < 15500:
            if ticks%15 == 0:
                addstuff("circle", BLUE, [0, y], [10], [8, 0])
                addstuff("circle", BLUE, [x, 0], [10], [0, 8])
                addstuff("circle", BLUE, [600, y], [10], [-8, 0])
                addstuff("circle", BLUE, [x, 500], [10], [0, -8])
        elif ticks < 15600:
            texttoprint = "Still alive?"
            HP += 0.2
        elif ticks < 15700:
            texttoprint = "Check this out"
        elif ticks == 15701:
            movement[1] = 50
        elif ticks < 16500:
            if ticks%25==0:
                addstuff("rect", BLUE, [600, 400], [10, 100], [-6, 0])
            if ticks%100==0:
                movement[1] = 150
                iframes = 0
            if (ticks+1)%100==0:
                iframes = 0
                movement[1] = 0
        elif ticks < 17000:
            if ticks % 75 == 0:
                addstuff("accelrect", BLUE, [0, 0], [10, 300], [3, 0])
                addstuff("accelrect", BLUE, [600, 200], [10, 300], [-3, 0])

            if ticks % 100 == 0:
                addstuff("accelcircle", BLUE, [300, 0], [10],[random.randint(-3, 3), 1])
                addstuff("accelcircle", BLUE, [300, 0], [10],[random.randint(-3, 3), 1])
        elif ticks < 18000:
            movement[0] = 50
            #COLOR = (255, 0, 0)
            if ticks % 25 == 0:
                addstuff("accelrect", BLUE, [0, random.randint(0, 400)], [20, 100], [3, 0])
        elif ticks < 18100:
            texttoprint = "I think this level is long enough"
            HP += 1
        elif ticks < 18200:
            texttoprint = "You die now"
            HP += 0.5
        elif ticks < 18500:
            if ticks%15 == 0:
                addstuff("accelrect", RED, [random.randint(0, 500), -10], [100, 25], [0, 6])
        elif ticks < 19000:
            if ticks%15 == 0:
                addstuff("accelrect", RED, [random.randint(0, 500), -10], [100, 25], [0, 6])
                addstuff("accelrect", RED, [0, random.randint(0, 400)], [20, 100], [3, 0])
        elif ticks < 19500:
            if ticks%2 == 0:
                addstuff("circle", ORANGE, [abs(math.sin(ticks/30)) * 600, 0], [10], [0, 5])
                addstuff("circle", PURPLE, [0, abs(math.cos(ticks/30)) * 500], [10], [5, 0])
        elif ticks < 20000:
            speedx = -1
            speedy = -1
            COLOR = (0, 0, 255)
            if ticks % 75 == 0:
                addstuff("rect", RED, [0, 0], [10, 600], [3, 0])
            if ticks % 50 == 0:
                addstuff("circle", RED, [600, 200], [10],[-4, random.randint(-2, 2)])
                addstuff("circle", RED, [000, 200], [10],[4, random.randint(-2, 2)])
        elif ticks < 20100:
            COLOR = (0, 0, 255)
            HP += 0.01
        elif ticks < 21000:
            speedx = 1
            speedy = 1
            if ticks%15 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10], [8, 0])
                addstuff("accelcircle", BLUE, [x, 0], [10], [0, 8])
                addstuff("accelcircle", BLUE, [600, y], [10], [-8, 0])
                addstuff("accelcircle", BLUE, [x, 500], [10], [0, -8])
        elif ticks < 22000:
            if ticks%2 == 0:
                cords = [300-(math.cos(ticks/30))*300, 250-(math.sin(ticks/30))*250]
                addstuff("accelcircle", BLUE, cords, [10], [x*-7 for x in makeunitvector([cords[0]-x, cords[1]-y])])
        elif ticks < 22400:
            cords = [300-(math.cos(ticks/30))*300, 250-(math.sin(ticks/30))*250]
            addstuff("accelcircle", BLUE, cords, [10], [x*-7 for x in makeunitvector([cords[0]-x, cords[1]-y])])
            if ticks%15 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10], [8, 0])
                addstuff("accelcircle", BLUE, [x, 0], [10], [0, 8])
                addstuff("accelcircle", BLUE, [600, y], [10], [-8, 0])
                addstuff("accelcircle", BLUE, [x, 500], [10], [0, -8])
        elif ticks < 23000:
            if (ticks+90)%100==0:
                movement[random.randint(0,1)] = random.choice([-150, 150])
            if (ticks+91)%100==0:
                movement[1] = 0
                CD = 0
            if ticks%50==0:
                addstuff("rect", BLUE, [600, 400], [10, 100], [-6, 0])
                addstuff("rect", BLUE, [0, 0], [10, 100], [6, 0])
                addstuff("rect", BLUE, [500, 0], [100, 10], [0, 6])
                addstuff("rect", BLUE, [0, 400], [100, 10], [0, -6])
        elif ticks < 23500:
            if ticks % 40 == 0:
                addstuff("accelcircle", BLUE, [600, 250], [10],[-4, random.uniform(-2, 2)])
            if (ticks + 8) % 40 == 0:
                addstuff("accelcircle", BLUE, [0, 250], [10],[4, random.uniform(-2, 2)])
            if (ticks + 16) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 0], [10], [random.uniform(-2, 2), 4])
            if (ticks + 24) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 500], [10], [random.uniform(-2, 2), -4])
        elif ticks < 24000:
            if ticks % 40 == 0:
                addstuff("accelcircle", BLUE, [600, 250], [10],[-4, random.uniform(-2, 2)])
            if (ticks + 8) % 40 == 0:
                addstuff("accelcircle", BLUE, [0, 250], [10],[4, random.uniform(-2, 2)])
            if (ticks + 16) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 0], [10], [random.uniform(-2, 2), 4])
            if (ticks + 24) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 500], [10], [random.uniform(-2, 2), -4])
            if ticks%15 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10], [8, 0])
                addstuff("accelcircle", BLUE, [x, 0], [10], [0, 8])
                addstuff("accelcircle", BLUE, [600, y], [10], [-8, 0])
                addstuff("accelcircle", BLUE, [x, 500], [10], [0, -8])
        elif ticks < 24100:
            windowpos = window.position
            if ticks%10 == 0:
                addstuff("rect", BLUE, [0, 100], [20, 300], [8, 0])
                addstuff("rect", BLUE, [150, 0], [300, 20], [0, 8])
            if ticks % 40 == 0:
                addstuff("accelcircle", BLUE, [600, 250], [10],[-4, random.uniform(-2, 2)])
            if (ticks + 8) % 40 == 0:
                addstuff("accelcircle", BLUE, [0, 250], [10],[4, random.uniform(-2, 2)])
            if (ticks + 16) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 0], [10], [random.uniform(-2, 2), 4])
            if (ticks + 24) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 500], [10], [random.uniform(-2, 2), -4])
            if ticks%15 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10], [8, 0])
                addstuff("accelcircle", BLUE, [x, 0], [10], [0, 8])
                addstuff("accelcircle", BLUE, [600, y], [10], [-8, 0])
                addstuff("accelcircle", BLUE, [x, 500], [10], [0, -8])
        elif ticks < 25000:
            window.position = (windowpos[0] - random.randint(-20, 20),windowpos[1] - random.randint(-20, 20))
            screen = pygame.display.set_mode((WIDTH - random.randint(-25,25), HEIGHT - random.randint(-25,25)))
            if ticks % 40 == 0:
                addstuff("accelcircle", BLUE, [600, 250], [10],[-4, random.uniform(-2, 2)])
            if (ticks + 8) % 40 == 0:
                addstuff("accelcircle", BLUE, [0, 250], [10],[4, random.uniform(-2, 2)])
            if (ticks + 16) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 0], [10], [random.uniform(-2, 2), 4])
            if (ticks + 24) % 40 == 0:
                addstuff("accelcircle", BLUE, [300, 500], [10], [random.uniform(-2, 2), -4])
            if ticks%15 == 0:
                addstuff("accelcircle", BLUE, [0, y], [10], [8, 0])
                addstuff("accelcircle", BLUE, [x, 0], [10], [0, 8])
                addstuff("accelcircle", BLUE, [600, y], [10], [-8, 0])
                addstuff("accelcircle", BLUE, [x, 500], [10], [0, -8])
            if ticks % 75 == 0:
                addstuff("accelrect", BLUE, [0, 0], [10, 600], [3, 0])
            if ticks % 50 == 0:
                addstuff("accelcircle", BLUE, [600, 200], [10],[-4, random.randint(-2, 2)])
                addstuff("accelcircle", BLUE, [000, 200], [10],[4, random.randint(-2, 2)])
        elif ticks < 25100:
            texttoprint = "oh you lived"
        elif ticks < 25200:
            texttoprint = "ok I guess you win"
            movementground = False
            mainmenu = True
        screen.fill(WHITE)
        screen.blit(font.render(texttoprint, True, GREEN), (WIDTH / 2 - len(texttoprint) * 9, HEIGHT / 2 - 50))

        #Projectiles moving & drawing:
        stf = 0  #just a counter variable
        for i in list(Stuff.keys()):
            Stuff[i]["cords"] = [Stuff[i]["cords"][0] + Stuff[i]["vector"][0],Stuff[i]["cords"][1] + Stuff[i]["vector"][1]]
            addstf = True
            if Stuff[i]["cords"][0] > WIDTH + 100 or Stuff[i]["cords"][0] < -100 or Stuff[i]["cords"][1] > HEIGHT + 100 or Stuff[i]["cords"][1] < -100:
                del Stuff[i]
                continue

            #draw the stuff + collisions (because of course circles are centered but rectangles aren't, which makes sense but still is annoying)
            if "rect" in i:
                pygame.draw.rect(screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1], Stuff[i]["size"][0], Stuff[i]["size"][1]))
                if Stuff[i]["cords"][0] <= x and (Stuff[i]["cords"][0] + Stuff[i]["size"][0]) >= x and Stuff[i]["cords"][1] <= y and (Stuff[i]["cords"][1] + Stuff[i]["size"][1]) >= y:
                    #print("collision with rect obj")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= 5
                        iframes = 10

            if "circle" in i:
                pygame.draw.circle( screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1]), Stuff[i]["size"][0])
                if (Stuff[i]["cords"][0] + Stuff[i]["size"][0] > x and Stuff[i]["cords"][0] - Stuff[i]["size"][0] < x) and (Stuff[i]["cords"][1] + Stuff[i]["size"][0] > y and Stuff[i]["cords"][1] - Stuff[i]["size"][0] < y):
                    #print("collision with circle obj")
                    #print("y collision")
                    if iframes <= 0:
                        print("insert damage here")
                        HP -= 5
                        iframes = 10

            #will not implement arc collision because I will not be using them for anything other than backgrounds
            if "arc" in i:
                pygame.draw.arc(screen, Stuff[i]["color"], (Stuff[i]["cords"][0], Stuff[i]["cords"][1], Stuff[i]["size"][0], Stuff[i]["size"][1]), 0,math.pi * 2)

            #accelerate stuff with the "accel" tag
            if "accel" in i:
                Stuff[i]["vector"] = [Stuff[i]["vector"][0] * 1.05,Stuff[i]["vector"][1] * 1.05]


            stf += 1
            #except:
            #    continue
        #Draw healthbar:
        if HP > 0:
            pygame.draw.rect(screen, COLOR, (0, 10, HP, 20))
            pygame.draw.polygon(screen, COLOR, [(HP, 10), (HP + 2*math.log(HP,2), 10), (HP, 29)])
        pygame.draw.circle(screen, COLOR, (x, y), r)
        pygame.display.update()
        CD -= 0.1
        clock.tick(FPS)
        timetaken = time.time() - timev
        if timetaken > 0.1:
            print(f"Long frame! {timetaken}")
        if HP <= 0:
            print("l")
            movementground = False
            mainmenu = True
            COLOR = (255, 0, 0)
        #print(f"Frame time: {time.time() - timev}")




