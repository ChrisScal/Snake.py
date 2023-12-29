import pygame as pygame
import sys,random
import os
from pygame.math import Vector2

class Snake:
    #To fydi
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)    
        self.new_block = False  
        
        #eikones fydioy 
        
        #head
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        
        #tail
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
        
        #body
        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        
        #tail
        self.tail_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.tail_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.tail_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.tail_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        
        
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
        self.randomize() #oti briskotan sth methodo randmize htan edw alla gia oikonomia xwroi aplws thn kaloume

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        #draw rect

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)#disdiastatos pinakas syntetagmenwn (bloebei anti gia lista argotera)
        
class Bomb():
    #Class Bombas
    def __init__(self) :
        #x,y position
        self.randomize() 

    def draw_bomb(self):
            bomb_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
            screen.blit(bomb,bomb_rect)

             
    def randomize(self):
            self.x = random.randint(0,cell_number-1)
            self.y = random.randint(0,cell_number-1)
            self.pos = Vector2(self.x, self.y)#disdiastatos pinakas syntetagmenwn (bloebei anti gia lista argoter)
    
class MAIN :
    if not os.path.isfile("high_score.txt"): 
        with open("high_score.txt", "w") as hs:
            hs.write("0")
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        #Xrhsh listas gia thn apothhkeush stoixeiwn Bomb , kaleste me self.bomb[<arithmos>]
        self.bomb=[]
        for i in range(5):
            bomb_obj=Bomb()
            self.bomb.append(bomb_obj)
    def update(self):
       self.snake.move_snake() 
       self.check_collision()
       self.check_fail()
       
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        
        #Bombes ana 3 mhla (3-->0 , 6-->1 kok mexri tis 5 vomves )
        #H akeraia diairesh ayth dinei ton arithmo twn vomvwn kai tis kanei draw analoga to score 
        for i in range((len(self.snake.body)-3)//3):
            self.bomb[i].draw_bomb()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            #reposition to mhlo
            self.snake.addblock()
            #+1 block sto snecko
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()
        '''
        #prepei ta for loop na leitourgoun me basei ta index pou periexontai sto grid
        for bomb in self.bomb[0:((len(self.snake.body)-3)//3)]:
            if bomb.pos == self.snake.body[0] :
                bomb.randomize()
            #reposition to bomb
            self.subtractblock()
            #-1 block
        for block in self.snake.body[1:]:
            for bomb in self.bomb[0:((len(self.snake.body)-3)//3)]:
                if block == bomb.pos:
                    bomb.randomize()
            #THELEI DOULEIA ''''''''
            #if self.bomb[0].pos in [self.snake.direction.x,self.snake.direction.y]:
            #    self.bomb[0].randomize()
            '''
            
            
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
    
    def subtractblock(self):
        if len(self.snake.body) >3:
            self.snake.body.pop(0)
        else:
            self.game_over()
    
                    
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
    
        self.snake.reset()
        self.fruit.pos = Vector2(15,10)


pygame.init()#kanei initialize to module (einai aparaitito)
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))#window
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
bomb=pygame.image.load("Graphics/bomb1.png").convert_alpha()
game_font = pygame.font.Font(None ,25) #bale font !!!!!!!!
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #animation timer
#main game

main_game = MAIN()
moved = False

while True:
    for event in pygame.event.get():
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
                    moved = False
           if event.key == pygame.K_DOWN:
               if main_game.snake.direction.y !=-1 and moved == True :
                     
                    main_game.snake.direction = Vector2(0,1)
                    moved = False
           if event.key == pygame.K_RIGHT:
               if main_game.snake.direction.x !=-1 and moved == True :
                     
                    main_game.snake.direction = Vector2(1,0)
                    moved = False
           if event.key == pygame.K_LEFT and moved == True:
               if main_game.snake.direction.x !=1 :
                    
                    
                    main_game.snake.direction = Vector2(-1,0)
                    moved = False
               

    screen.fill((175,215,70))
    main_game.draw_elements()
    #edw pane ta graphic elements
    pygame.display.update()
    clock.tick(60)#framerate --> 60fps locked :)

