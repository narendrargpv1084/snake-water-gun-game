import pygame
import sys
import random
import time
Computer_Score = 0
User_Score = 0    
def Get_Weapon():
    weapon =["Snake","Water","Gun"]
    return (random.choice(weapon))
def Winner(user_Weapon,computer_Weapon):
    if(user_Weapon == computer_Weapon):
        return "Draw!"
    win= {
        ("Snake","Water"): "User",
        ("Water","Gun"): "User",
        ("Gun","Snake"): "User",
        ("Water", "Snake"): "Computer",
        ("Gun", "Water"): "Computer",
        ("Snake", "Gun"): "Computer",
    }
    return (win.get((user_Weapon,computer_Weapon)))
User_weapon = ""
pygame.init()
pygame.mixer.init()
user = pygame.font.SysFont("Arial",25)
info = pygame.font.SysFont("Arial",20)
textstyle = pygame.font.SysFont("Arial",30)
heading  = pygame.font.SysFont("Arial",35)
screen = pygame.display.set_mode((750,600))
width = screen.get_width() 
height = screen.get_height() +100
running = True
logo = pygame.image.load('logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption("SNAKE,WATER,GUN GAME")
#images
background_image1 = pygame.image.load('background.png')
background_image1 = pygame.transform.scale(background_image1, (width,height-100))
background_image2 = pygame.image.load('banner.png')
background_image2 = pygame.transform.scale(background_image2, (width,height-100))
background_image5 = pygame.image.load('winner.png')
background_image5 = pygame.transform.scale(background_image5, (width,height-100))
background_image6 = pygame.image.load('end.png')
background_image6 = pygame.transform.scale(background_image6, (width,height-100))

background_image4 = pygame.image.load('background4.png.webp')
background_image4 = pygame.transform.scale(background_image4, (width,height-100))
background_image3 = pygame.image.load('background3.png')
background_image3 = pygame.transform.scale(background_image3, (width,height-100))
blue_back = pygame.image.load("pngwing.com.png")
blue_back = pygame.transform.scale(blue_back,(50,50))
green_back = pygame.image.load("back.png")
green_back = pygame.transform.scale(green_back,(50,50))
green_arrow = pygame.image.load("arrow.png")
green_arrow = pygame.transform.scale(green_arrow,(40,40))
cpu = pygame.image.load("computer.png")
cpu = pygame.transform.scale(cpu,(100,100))
use_icon = pygame.image.load("user.png")
use_icon = pygame.transform.scale(use_icon,(100,100))
snake = pygame.image.load("snake.png")
snake = pygame.transform.scale(snake,(100,100))
water = pygame.image.load("water.png")
water = pygame.transform.scale(water,(100,100))
unknown = pygame.image.load("unknown.png")
unknown = pygame.transform.scale(unknown,(100,100))
unknown1 = pygame.image.load("unknown1.png")
unknown1 = pygame.transform.scale(unknown1,(100,100))
image = pygame.image.load("image.png")
image = pygame.transform.scale(image,(180,180))
blues = pygame.image.load("blue.png")
blues = pygame.transform.scale(blues,(250,120))
greens = pygame.image.load("green.png")
greens = pygame.transform.scale(greens,(250,120))
use_gun = pygame.image.load("gun.png")
use_gun = pygame.transform.scale(use_gun,(100,100))
#text
start = textstyle.render('START' , True , "BLACK") 
rules = textstyle.render('RULES' , True , "BLACK") 
mains = textstyle.render('MENU' , True , "BLACK") 
Quit = textstyle.render('QUIT' , True , "BLACK")
r1 = heading.render('RULES:-' , True , "black") 
r2 = heading.render('1. Snake vs. Water: ' , True , "black") 
r3 = textstyle.render('Snake drinks the water hence Snake wins.' , True , "black")
r4 = heading.render('2. Water vs. Gun: ' , True , "black") 
r5 = textstyle.render('The Gun will drown in water, hence Water wins.' , True , "black") 
r6 = heading.render('3. Gun vsSnake: ' , True , "black")
r7 = textstyle.render('Gun will kill the Snake and win the game.' , True , "black") 
r8 = textstyle.render('4. In situations where both players choose the same object' , True , "black") 
r9 = textstyle.render('the result will be a draw.' , True , "black") 
info1 = info.render('# maximum username length = 8 ' , True , "RED")
username = user.render('User name:- ' , True , "red") 
cpuname = user.render('Computer' , True , "WHITE") 
alert = user.render('Error enter the user name',True,"red")
next_round = user.render('NEXT ROUND',True,"red")
res = user.render("ITS A DRAW",True,"WHITE")
font = pygame.font.Font(None, 32)
input_text = ''
username_length = 0
cpuw = user.render("COMPUTER WIN",True,"White")
userw = user.render(f"{input_text} WIN",True,"White")
mouse = pygame.mouse.get_pos()
text = user.render(input_text, True, "WHITE")

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

def menu():
    screen.blit(background_image1,(0,0))

    mouse = pygame.mouse.get_pos()
    if width//2-80 <= mouse[0] <= width/2+50 and height//2-150 <= mouse[1] <= height/2-104: 
        pygame.draw.rect(screen,"yellow",[width//2-80,height//2-150,130,46])  
    elif width//2-80 <= mouse[0] <= width/2+50 and height//2-80 <= mouse[1] <= height/2-34: 
        pygame.draw.rect(screen,"yellow",[width//2-80,height//2-80,130,46])  
    elif width//2-80 <= mouse[0] <= width/2+50 and height//2-10 <= mouse[1] <= height/2+36: 
        pygame.draw.rect(screen,"yellow",[width//2-80,height//2-10,130,46])  
    screen.blit(start , (width/2-50,height/2-140))
    screen.blit(rules , (width/2-50,height/2-70))
    screen.blit(Quit , (width/2-40,height/2))
def Rule():
    screen.blit(background_image1,(0,0))
    screen.blit(blue_back,(20,20))
    mouse = pygame.mouse.get_pos()
    screen.blit(r1 , (90,50))
    screen.blit(r2 , (40,85))
    screen.blit(r3 , (90,120))
    screen.blit(r4 , (40,155))
    screen.blit(r5 , (90,190))
    screen.blit(r6 , (40,220))
    screen.blit(r7 , (90,255))
    screen.blit(r8 , (40,290))
    screen.blit(r9 , (90,320))
    if width//2-80 <= mouse[0] <= width/2+50 and height//2+40 <= mouse[1] <= height/2+76: 
        pygame.draw.rect(screen,"yellow",[width//2-80,height//2+40,130,46])
    if 20 <= mouse[0] <= 70 and 20 <= mouse[1] <= 70: 
        screen.blit(green_back,(20,20))
    screen.blit(Quit , (width/2-40,height/2+45))
def draw_text(text, position):
        text_surface = user.render(text, True, "WHITE")
        screen.blit(text_surface, position)
def starts():
    screen.blit(background_image2,(0,0))
    screen.blit(blue_back,(20,20))
    screen.blit(green_arrow,(width//2+130,height//2-205))
    pygame.draw.rect(screen,"gray",[width//2-130,height//2-200,270,30])
    screen.blit(username,(width//2-125,height//2-200))
    
    if 20 <= mouse[0] <= 70 and 20 <= mouse[1] <= 70: 
        screen.blit(green_back,(20,20))
    if width//2-80 <= mouse[0] <= width/2+50 and height//2-10 <= mouse[1] <= height/2+36: 
        pygame.draw.rect(screen,"yellow",[width//2-80,height//2-10,130,46])
    draw_text(input_text, (width//2, height//2-200))
    screen.blit(info1 , (width/2-130,height/2-150))
    screen.blit(Quit , (width/2-40,height/2))
def gaming():
    
    # unknown = pygame.image.load("unknown.png")
    # unknown1 = pygame.image.load("unknown1.png")
    screen.blit(background_image3,(0,0))
    screen.blit(cpu,(0,0))
    screen.blit(use_icon,(0,500))
    screen.blit(image,(160,-30))
    screen.blit(image,(360,-30))
    screen.blit(image,(550,-30))
    screen.blit(image,(160,450))
    screen.blit(image,(360,450))
    pygame.draw.rect(screen,"BLACK",[width//2,130,100,100])
    screen.blit(unknown1,(width//2,130))
    screen.blit(image,(550,450))
    screen.blit(snake,(200,10))
    screen.blit(water,(400,10))
    screen.blit(use_gun,(600,10))
    screen.blit(snake,(200,490))
    screen.blit(water,(400,490))
    pygame.draw.rect(screen,"BLACK",[width//2,370,100,100])
    screen.blit(unknown,(width//2,370))
    screen.blit(use_gun,(600,490))
    pygame.draw.line(screen,"black",[100,474],[750,474],10)
    pygame.draw.line(screen,"black",[100,124],[750,124],10)
    pygame.draw.rect(screen,"BLACK",[0,470,100,30])
    pygame.draw.rect(screen,"BLACK",[0,100,100,30])
    pygame.draw.rect(screen,"BLACK",[0,130,100,30])
    cpuscr = user.render(f"Score = {Computer_Score}", True, "white")
    userscr = user.render(f"Score = {User_Score}", True, "white")
    screen.blit(cpuscr,(5,130))
    pygame.draw.rect(screen,"BLACK",[0,440,100,30])
    screen.blit(userscr,(5,440))
    if unknown == snake or unknown == water or unknown == use_gun:
        screen.blit(blues,(550,400))
        if 603 <= mouse[0] <= 747 and 451 <= mouse[1] <= 469: 
            screen.blit(greens,(550,400))
    draw_text(input_text, (5, 470))
    screen.blit(cpuname,(0,100))
menus = 0
Rules = 1
starting = 2
game = 3
battle = 4
leagues = 5
end = 6
def battling():
    screen.blit(background_image4,(0,0))
    screen.blit(unknown1,(100,250))
    screen.blit(unknown,(550,250))
def ending():
    screen.blit(background_image6,(0,0))
    pygame.draw.rect(screen,"yellow",[width//2-80,height//2-10,130,46])
    pygame.draw.rect(screen,"yellow",[width//2-80,height//2-80,130,46])
    pygame.draw.rect(screen,"blue",[95,150,200,30])
    if User_Score == 5:        
        screen.blit(userw,(100,150))
    elif Computer_Score == 5:
        screen.blit(cpuw,(100,150))
    if width//2-80 <= mouse[0] <= width/2+50 and height//2-80 <= mouse[1] <= height/2-34: 
        pygame.draw.rect(screen,"green",[width//2-80,height//2-80,130,46])  
    if width//2-80 <= mouse[0] <= width/2+50 and height//2-10 <= mouse[1] <= height/2+36: 
        pygame.draw.rect(screen,"green",[width//2-80,height//2-10,130,46])   
    screen.blit(mains , (width/2-50,height/2-70))
    screen.blit(Quit , (width/2-40,height/2))
def league():
    screen.blit(background_image5,(0,0))
    if result == "Draw!":
        screen.blit(res,(330,250))
    elif result == "User":
        screen.blit(userw,(320,75))
        screen.blit(unknown,(330,200))
    elif result == "Computer":
        screen.blit(cpuw,(320,75))
        screen.blit(unknown1,(330,200))
    if ( User_Score<5 or Computer_Score<5):
        pygame.draw.rect(screen,"yellow",[width//2-80,height//2+180,180,46])
    if width//2-80 <= mouse[0] <= width/2+100 and height//2+180 <= mouse[1] <= height/2+226 and ( User_Score<5 or Computer_Score<5): 
        pygame.draw.rect(screen,"green",[width//2-80,height//2+180,180,46])
    if ( User_Score<5 or Computer_Score<5):
        screen.blit(next_round,(width//2-60,height//2+185))
input_active = True
current = menus

while running:
    
    for event in pygame.event.get():
        
        screen.fill((255, 255, 255))
        if(current == menus):
            menu()
        elif(current == Rules):
            Rule()
        elif(current == starting ):
            starts()
        elif(current == game ):
            gaming()
        elif(current == battle ):
            battling()
        elif(current == leagues ):
            league()
        elif(current == end ):
            ending()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if (current == menus) and event.type == pygame.MOUSEBUTTONDOWN: 
			
            if width//2-80 <= mouse[0] <= width/2+50 and height//2-10 <= mouse[1] <= height/2+36: 
                running = False
                pygame.quit()
                sys.exit()
            if width//2-80 <= mouse[0] <= width/2+50 and height//2-80 <= mouse[1] <= height/2-34:
                current = Rules
            if width//2-80 <= mouse[0] <= width/2+50 and height//2-150 <= mouse[1] <= height/2-104: 
                current = starting
        if (current == Rules) and event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if width//2-80 <= mouse[0] <= width/2+50 and height//2+40 <= mouse[1] <= height/2+76: 
                running = False
                pygame.quit()
                sys.exit()
            if 20 <= mouse[0] <= 70 and 20 <= mouse[1] <= 70:
                current = menus
                #for string input
        if (current == starting) and event.type == pygame.KEYDOWN and input_active == True:
            if event.key == pygame.K_RETURN: 
                input_active = False
            elif event.key == pygame.K_BACKSPACE and username_length>=1:
                input_text = input_text[:-1] 
                username_length -= 1
            else:
                if username_length<=7:
                    input_text += event.unicode
                    userw = user.render(f"{input_text} WIN",True,"White")
                    username_length += 1

        if (current == starting) and event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if width//2-80 <= mouse[0] <= width/2+50 and height//2-10 <= mouse[1] <= height/2+36: 
                running = False
                pygame.quit()
                sys.exit()
            if 20 <= mouse[0] <= 70 and 20 <= mouse[1] <= 70:
                current = menus
            if  514 <= mouse[0] <= 540 and 150 <= mouse[1] <= 181:
                if username_length == 0:
                    screen.blit(alert,(width//2-125,height//2-235))
                else:
                    current = game
        if (current == game) and event.type == pygame.MOUSEBUTTONDOWN:
            if 192 <= mouse[0] <= 308 and 483 <= mouse[1] <= 599:
                unknown = snake
            if 392 <= mouse[0] <= 508 and 483 <= mouse[1] <= 599:
                unknown = water
            if 572 <= mouse[0] <= 698 and 483 <= mouse[1] <= 599:
                unknown = use_gun
            if 603 <= mouse[0] <= 747 and 451 <= mouse[1] <= 469:
                if(unknown == snake):
                    User_weapon = "Snake"
                elif(unknown == water):
                    User_weapon = "Water"
                elif(unknown == use_gun):
                    User_weapon = "Gun"
                Computer_Weapon = Get_Weapon()
                if(Computer_Weapon == "Snake"):
                    unknown1 = snake
                if(Computer_Weapon == "Gun"):
                    unknown1 = use_gun
                if(Computer_Weapon == "Water"):
                    unknown1 = water
                current = battle
                result = Winner(User_weapon,Computer_Weapon)
                if result == "Draw!":
                    pass
                elif result == "User":
                    User_Score += 1
                elif result == "Computer":
                    Computer_Score += 1
                break
        if (current == battle) and event.type == pygame.MOUSEBUTTONDOWN:
            current = leagues
        if (current == leagues) and event.type == pygame.MOUSEBUTTONDOWN:
            if width//2-80 <= mouse[0] <= width/2+100 and height//2+180 <= mouse[1] <= height/2+226 and ( User_Score<5 or Computer_Score<5):
                current = game
                unknown = pygame.image.load("unknown.png")
                unknown = pygame.transform.scale(unknown,(100,100))
                unknown1 = pygame.image.load("unknown1.png")
                unknown1 = pygame.transform.scale(unknown1,(100,100))
            elif User_Score == 5 or Computer_Score ==5:
                current = end
        if (current == end) and event.type == pygame.MOUSEBUTTONDOWN:
            if width//2-80 <= mouse[0] <= width/2+50 and height//2-10 <= mouse[1] <= height/2+36: 
                running = False
                pygame.quit()
                sys.exit()
            if width//2-80 <= mouse[0] <= width/2+50 and height//2-80 <= mouse[1] <= height/2-34:
                current = menus
                User_Score = 0
                Computer_Score = 0
                input_text = ''
                input_active == True
                username_length = 0
        mouse = pygame.mouse.get_pos()
    pygame.display.flip()