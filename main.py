import pygame as pygame
import sys,random
import os
from pygame.math import Vector2
from button import Button

class Snake:
    #To fydi
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)    
        self.new_block = False  
        
        #eikones fydioy 
        
        #head
        self.head_up = pygame.image.load('Graphics/Graphical Elements/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/Graphical Elements/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/Graphical Elements/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/Graphical Elements/head_left.png').convert_alpha()
        
        #tail
        self.tail_up = pygame.image.load('Graphics/Graphical Elements/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/Graphical Elements/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/Graphical Elements/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/Graphical Elements/tail_left.png').convert_alpha()
        
        #body
        self.body_vertical = pygame.image.load('Graphics/Graphical Elements/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/Graphical Elements/body_horizontal.png').convert_alpha()
        
        #tail
        self.tail_tr = pygame.image.load('Graphics/Graphical Elements/body_tr.png').convert_alpha()
        self.tail_tl = pygame.image.load('Graphics/Graphical Elements/body_tl.png').convert_alpha()
        self.tail_br = pygame.image.load('Graphics/Graphical Elements/body_br.png').convert_alpha()
        self.tail_bl = pygame.image.load('Graphics/Graphical Elements/body_bl.png').convert_alpha()
        
        
    def draw_snake(self):
        ''' !!! palio draw, antikathhstatai apo to to apo katw gia na mpainoun oi eikones!!!
        for block in self.body:
            #create rect
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            block_rect = pygame.Rect(x_pos, y_pos ,cell_size ,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
            #draw the rectangle
        '''
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):   #index --> stoixeio ths listas  block --> to Vector2 stoixeio 
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            block_rect = pygame.Rect(x_pos, y_pos ,cell_size ,cell_size)
            
            #snake body part id
            if index == 0 : #kefali
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:#oura
                screen.blit(self.tail,block_rect)
            else :
                previous_block = self.body[index +1 ] - block#== self.body[index]
                next_block = self.body[index - 1 ] - block
                if previous_block.x == next_block.x :#vert
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y :
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.tail_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.tail_bl,block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.tail_tr,block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.tail_br,block_rect)  
            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction )
            self.body=body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction )
            self.body=body_copy[:]
        
    def addblock(self):
        self.new_block = True

    def update_head_graphics(self):
        head_body_relation = self.body[1] - self.body[0]
        if head_body_relation == Vector2(1,0): self.head = self.head_left 
        elif head_body_relation == Vector2(-1,0): self.head = self.head_right
        elif head_body_relation == Vector2(0,1): self.head = self.head_up
        elif head_body_relation == Vector2(0,-1): self.head = self.head_down
        
    def update_tail_graphics(self):
        tail_body_relation = self.body[-2] - self.body[-1]
        if tail_body_relation == Vector2(1,0): self.tail = self.tail_left 
        elif tail_body_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_body_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_body_relation == Vector2(0,-1): self.tail = self.tail_down
        
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class Fruit :
    def __init__(self) :
        #x,y position
        #self.randomize() #oti briskotan sth methodo randmize htan edw alla gia oikonomia xwroi aplws thn kaloume
        self.pos = Vector2(15,10)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        #draw rect

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)#disdiastatos pinakas syntetagmenwn (bloebei anti gia lista argotera)
        

class MAIN :
    if not os.path.isfile("high_score.txt"): 
        with open("high_score.txt", "w") as hs:
            hs.write("0")

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.volume= 0.5
        pygame.mixer.music.set_volume(self.volume)
        self.crunch_sound = pygame.mixer.Sound("sound/Apple-bite.mp3")
        self.turn_sd = pygame.mixer.Sound("sound/turn_2.wav")
        self.button_sd = pygame.mixer.Sound('sound/button.wav')
        self.crunch_sound.set_volume(self.volume)
        self.turn_sd.set_volume(self.volume)
        self.button_sd.set_volume(self.volume)
        
    def update(self):
       self.snake.move_snake() 
       self.check_collision()
       self.check_fail()
       
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    #more like pause menu music
    def play_menu_sd(self):
        pygame.mixer.music.load("sound/jjk.mp3") 
        pygame.mixer.music.play(-1)

    def play_game_over(self):
        pygame.mixer.music.load('sound/Game_over.mp3')
        pygame.mixer.music.play()

    #giam giam noises
    def play_crunch_sound(self):
        self.crunch_sound.play()
        
    def play_button_sd(self):
        self.button_sd.play()
        
    #gia strofes
    def play_turn_sd(self): 
        self.turn_sd.play()
        
    #kapoia genika gia to sound kounabhs geniko
    def open__sd(self):
        pygame.mixer.music.set_volume(self.volume)
        self.crunch_sound.set_volume(self.volume)
        self.turn_sd.set_volume(self.volume)
        self.button_sd.set_volume(self.volume)

    def mute_game_sound(self):
        pygame.mixer.music.set_volume(0) 
        self.crunch_sound.set_volume(0) 
        self.turn_sd.set_volume(0) 
        self.button_sd.set_volume(0)
    
    def higher_sd(self):
        self.volume += 0.1
        if self.volume> 1:
            self.volume = 1
        pygame.mixer.music.set_volume(self.volume)
        self.crunch_sound.set_volume(self.volume)
        self.turn_sd.set_volume(self.volume)
        self.button_sd.set_volume(self.volume)

    def lower_sd(self):
        self.volume -= 0.1
        if self.volume< 0:
            self.volume = 0
        pygame.mixer.music.set_volume(self.volume)
        self.crunch_sound.set_volume(self.volume)
        self.turn_sd.set_volume(self.volume)
        self.button_sd.set_volume(self.volume)
        
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.play_crunch_sound()
            #reposition to mhlo
            self.snake.addblock()
            #+1 block sto snecko
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()
            
    def check_fail(self):
        #check an snake ektos screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y < cell_number:
            self.game_over()
            
        #check kanibalismos
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
            
    def draw_grass(self):
        grass_color = (167,209,61)#skouro
        for row in range(cell_number):
            if row %2 ==0:
                for col in range(cell_number):
                    if col % 2 == 0 :
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0 :
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
                    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        self.high_score = score_text
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x= cell_size*cell_number - 60
        score_y= cell_size*cell_number - 40
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top ,apple_rect.width + score_rect.width + 6 ,apple_rect.height)
        
        pygame.draw.rect(screen,(167,209,61) , bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12) , bg_rect,2)
    
    def game_over(self):
        with open ("high_score.txt", "r") as read_score:
                    if int(self.high_score) > int(read_score.read()):
                        with open ("high_score.txt", "w") as hs:
                            hs.write(f"{self.high_score}")
        self.play_game_over()
        self.snake.reset()  
        self.fruit.pos = Vector2(15,10)
        
def main_menu():
    running = True
    global sound
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("GAME MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Graphics/menu assets/Play Rect.png"), pos=(400, 200), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Graphics/menu assets/Options Rect.png"), pos=(400, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Graphics/menu assets/Quit Rect.png"), pos=(400, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False
                    main_game.play_button_sd()
                    pygame.mixer_music.unload() 
                    pygame.display.set_caption('snake game')
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_game.play_button_sd()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_game.play_button_sd()
                    pygame.quit()
                    sys.exit() 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_m:
                 sound = not sound
                 if sound == False:
                    main_game.mute_game_sound()
                 else:
                    main_game.open__sd()
                if event.key == pygame.K_q:
                  main_game.lower_sd()
                if event.key == pygame.K_e:
                    main_game.higher_sd()
                if event.key == pygame.K_SPACE:
                    pygame.display.set_caption('snake game')
                    running = False
                    pygame.mixer_music.unload()
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption('snake game')
                    running = False
                    pygame.mixer_music.unload() 
        pygame.display.update()
        
def options():
    #Gamemode Status ektos loop + global gia allagh ston kwdika
    global wall_status
    global sound
    wall_status = 'Disabled'
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(20).render("This is the OPTIONS screen.", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 600), 
                            text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        #Gamemode switches
        
        #Wall gamemode
        WALL_GAMEMODE_BUTTON = Button(image = None, pos=(400,400), text_input='Walls: '+ wall_status, font =get_font(35),base_color='#d7fcd4', hovering_color='White')
        
        for button in [WALL_GAMEMODE_BUTTON,OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_game.play_button_sd()
                    return
                if WALL_GAMEMODE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_game.play_button_sd()
                    if wall_status == 'Disabled':
                        wall_status = 'Enabled'
                        #energopoihsh tou mode
                        
                        
                    else:
                        wall_status = 'Disabled'
                        #apenergopoihsh






            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_m:
                 sound = not sound
                 if sound == False:
                    main_game.mute_game_sound()
                 else:
                    main_game.open__sd()
                if event.key == pygame.K_q:
                  main_game.lower_sd()
                if event.key == pygame.K_e:
                    main_game.higher_sd()
                if event.key == pygame.K_ESCAPE:
                    return()
        pygame.display.update()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Graphics/menu assets/font.ttf", size)


pygame.init()#kanei initialize to module (einai aparaitito)
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("snake game")

BG = pygame.image.load("Graphics/menu assets/Background.png")
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))#window
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/Graphical Elements/apple.png').convert_alpha()
game_font = pygame.font.Font(None ,25) #bale font !!!!!!!!
sound = True
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #animation timer
#main game

main_game = MAIN()

while True:
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               pygame.display.set_caption('pause menu')
               main_game.play_menu_sd()
               main_menu()
       if event.type == pygame.QUIT:
           pygame.quit()#kleinei to game
           sys.exit()
       if event.type == SCREEN_UPDATE:
            moved = True
            main_game.update()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               if main_game.snake.direction.y !=1 and moved == True :   
                    main_game.snake.direction = Vector2(0,-1)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_DOWN:
               if main_game.snake.direction.y !=-1 and moved == True :
                    main_game.snake.direction = Vector2(0,1)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_RIGHT:
               if main_game.snake.direction.x !=-1 and moved == True :
                    main_game.snake.direction = Vector2(1,0)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_LEFT:
               if main_game.snake.direction.x !=1 and moved == True :
                    main_game.snake.direction = Vector2(-1,0)
                    main_game.play_turn_sd()
                    moved = False
            #sorry xrhsto alla eprepe         
           if event.key == pygame.K_w:
               if main_game.snake.direction.y !=1 and moved == True:   
                    main_game.snake.direction = Vector2(0,-1)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_s:
               if main_game.snake.direction.y !=-1 and moved == True:
                    main_game.snake.direction = Vector2(0,1)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_d:
               if main_game.snake.direction.x !=-1 and moved == True:
                    main_game.snake.direction = Vector2(1,0)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_a:
               if main_game.snake.direction.x !=1 and moved == True:
                    main_game.snake.direction = Vector2(-1,0)
                    main_game.play_turn_sd()
                    moved = False
           if event.key == pygame.K_m:
               sound = not sound
               if sound == False:
                   main_game.mute_game_sound()
               else:
                   main_game.open__sd()
           if event.key == pygame.K_q:
               main_game.lower_sd()
           if event.key == pygame.K_e:
               main_game.higher_sd()
           if event.key == pygame.K_ESCAPE:
               pygame.quit()
               sys.exit()
                  

               

    screen.fill((175,215,70))
    #backscreen.fill((108, 133, 44))
    main_game.draw_elements()
    #edw pane ta graphic elements
    pygame.display.update()
    clock.tick(60)#framerate --> 60fps locked :)
#ez
