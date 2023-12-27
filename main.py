import pygame as pygame
import sys,random
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
class Bomb:
     def __init__(self) :
        #x,y position
        self.randomize() #oti briskotan sth methodo randmize htan edw alla gia oikonomia xwroi aplws thn kaloume

     def draw_bomb(self):
            bomb_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
            screen.blit(bomb,bomb_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        #draw rect
            
     def draw_bomb1(self):
         bomb1_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
         screen.blit(bomb1,bomb1_rect)
     def draw_bomb2(self):
            bomb2_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
            screen.blit(bomb2,bomb2_rect)
     def draw_bomb3(self):
            bomb3_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
            screen.blit(bomb3,bomb3_rect)
     def draw_bomb4(self):
         bomb4_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
         screen.blit(bomb4,bomb4_rect)
     def draw_bomb5(self):
            bomb5_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
            screen.blit(bomb5,bomb5_rect)
             
     def randomize(self):
            self.x = random.randint(0,cell_number-1)
            self.y = random.randint(0,cell_number-1)
            self.pos = Vector2(self.x, self.y)#disdiastatos pinakas syntetagmenwn (bloebei anti gia lista argoter)
class Minibomb:
    def __init__(self) :
        #x,y position
        self.randomize() #oti briskotan sth methodo randmize htan edw alla gia oikonomia xwroi aplws thn kaloume

    def draw_minibomb(self):
        minibomb_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(minibomb,minibomb_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        #draw rect

    def draw_minibomb1(self):
        minibomb1_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(minibomb1,minibomb1_rect)
        
    def draw_minibomb2(self):
        minibomb2_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(minibomb2,minibomb2_rect)

    def draw_minibomb3(self):
        minibomb3_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(minibomb3,minibomb3_rect)

    def draw_minibomb4(self):
        minibomb4_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(minibomb4,minibomb4_rect)
        
    def draw_minibomb5(self):
        minibomb5_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(minibomb5,minibomb5_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)


class Dark_block:
    def __init__(self) :
        #x,y position
        self.randomize() #oti briskotan sth methodo randmize htan edw alla gia oikonomia xwroi aplws thn kaloume

    def draw_dark_block(self):
        block_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(dark_block,block_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        #draw rect

    def draw_dark_block1(self):
        dark_block1_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(dark_block1,dark_block1_rect)

    def draw_dark_block2(self):
        dark_block2_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(dark_block2,dark_block2_rect)

    def draw_dark_block3(self):
        dark_block3_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(dark_block3,dark_block3_rect)

    def draw_dark_block4(self):
        dark_block4_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(dark_block4,dark_block4_rect)

    def draw_dark_block5(self):
        dark_block5_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        screen.blit(dark_block5,dark_block5_rect) 

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)


    
        

        

class MAIN :
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

        self.bomb=Bomb()
        self.bomb1=Bomb()
        self.bomb2=Bomb()
        self.bomb3=Bomb()
        self.bomb4=Bomb()
        self.bomb5=Bomb()
        
        
        
        self.minibomb=Minibomb()
        self.minibomb1=Minibomb()
        self.minibomb2=Minibomb()
        self.minibomb3=Minibomb()
        self.minibomb4=Minibomb()
        self.minibomb5=Minibomb()

        self.dark_block=Dark_block()
        self.dark_block1=Dark_block()
        self.dark_block2=Dark_block()
        self.dark_block3=Dark_block()
        self.dark_block4=Dark_block()
        self.dark_block5=Dark_block()
        
        
    def update(self):
       self.snake.move_snake() 
       self.check_collision()
       self.check_fail()
       
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()

        if len(self.snake.body)>25:
         self.bomb.draw_bomb()
        
        
        if len(self.snake.body)>27:
         self.bomb1.draw_bomb1()

        if len(self.snake.body)>29:
         self.bomb2.draw_bomb2()

        if len(self.snake.body)>31:
         self.bomb3.draw_bomb3()
        
        
        if len(self.snake.body)>33:
         self.bomb4.draw_bomb4()

        if len(self.snake.body)>35:
         self.bomb5.draw_bomb5()

        
        if len(self.snake.body)>3:
         self.minibomb.draw_minibomb()

        if len(self.snake.body)>5:

         self.minibomb1.draw_minibomb()

        if len(self.snake.body)>7:

         self.minibomb2.draw_minibomb2() 
          
        if len(self.snake.body)>9:
         self.minibomb3.draw_minibomb3()

        if len(self.snake.body)>11:

         self.minibomb4.draw_minibomb4()

        if len(self.snake.body)>13:

         self.minibomb5.draw_minibomb5()

        if len(self.snake.body)>14:

         self.dark_block.draw_dark_block()

        if len(self.snake.body)>16:

         self.dark_block1.draw_dark_block1()

        if len(self.snake.body)>18:
            self.dark_block2.draw_dark_block2()

        if len(self.snake.body)>20:

         self.dark_block3.draw_dark_block3()

        if len(self.snake.body)>22:

         self.dark_block4.draw_dark_block4()

        if len(self.snake.body)>24:
            self.dark_block5.draw_dark_block5()
        
        self.snake.draw_snake()
        self.draw_score()
        
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
        #reposition to mhlo


        
            self.snake.addblock()
            #+1 block sto snecko
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

        #check syntetagmenes empodia me snake kai mhlo
        if self.snake.body==self.bomb.pos:
            self.bomb.randomize()
        if self.snake.body==self.bomb1.pos:
            self.bomb1.randomize()
        if self.snake.body==self.bomb2.pos:
            self.bomb2.randomize()
        if self.snake.body==self.bomb3.pos:
            self.bomb3.randomize()
        if self.snake.body==self.bomb4.pos:
            self.bomb4.randomize()
        if self.snake.body==self.bomb5.pos:
            self.bomb5.randomize()
        
        if self.snake.body==self.minibomb.pos:
            self.minibomb.randomize()
        if self.snake.body==self.minibomb1.pos:
            self.minibomb1.randomize()
        if self.snake.body==self.minibomb2.pos:
            self.minibomb2.randomize()
        if self.snake.body==self.minibomb3.pos:
            self.minibomb3.randomize()
        if self.snake.body==self.minibomb4.pos:
            self.minibomb4.randomize()
        if self.snake.body==self.minibomb5.pos:
            self.minibomb5.randomize()
        
        if self.snake.body==self.dark_block.pos:
            self.dark_block.randomize()
        if self.snake.body==self.dark_block1.pos:
            self.dark_block1.randomize()
        if self.snake.body==self.dark_block2.pos:
            self.dark_block2.randomize()
        if self.snake.body==self.dark_block3.pos:
            self.dark_block3.randomize()
        if self.snake.body==self.dark_block4.pos:
            self.dark_block4.randomize()
        if self.snake.body==self.dark_block5.pos:
            self.dark_block5.randomize()


        if self.fruit.pos==self.bomb.pos:
            self.bomb.randomize()
        if self.fruit.pos==self.bomb1.pos:
            self.bomb1.randomize()
        if self.fruit.pos==self.bomb2.pos:
            self.bomb2.randomize()
        if self.fruit.pos==self.bomb3.pos:
            self.bomb3.randomize()
        if self.fruit.pos==self.bomb4.pos:
            self.bomb4.randomize()
        if self.fruit.pos==self.bomb5.pos:
            self.bomb5.randomize()
        
        if self.fruit.pos==self.minibomb.pos:
            self.minibomb.randomize()
        if self.fruit.pos==self.minibomb1.pos:
            self.minibomb1.randomize()
        if self.fruit.pos==self.minibomb2.pos:
            self.minibomb2.randomize()
        if self.fruit.pos==self.minibomb3.pos:
            self.minibomb3.randomize()
        if self.fruit.pos==self.minibomb4.pos:
            self.minibomb4.randomize()
        if self.fruit.pos==self.minibomb5.pos:
            self.minibomb5.randomize()
        
        if self.fruit.pos==self.dark_block.pos:
            self.dark_block.randomize()
        if self.fruit.pos==self.dark_block1.pos:
            self.dark_block1.randomize()
        if self.fruit.pos==self.dark_block2.pos:
            self.dark_block2.randomize()
        if self.fruit.pos==self.dark_block3.pos:
            self.dark_block3.randomize()
        if self.fruit.pos==self.dark_block4.pos:
            self.dark_block4.randomize()
        if self.fruit.pos==self.dark_block5.pos:
            self.dark_block5.randomize()
        
        #checking positions of blocks because we do not want them to spawn on the same square
        if self.bomb.pos==self.minibomb.pos:
            self.bomb.randomize()
        if self.bomb.pos==self.minibomb1.pos:
            self.bomb.randomize() 
        if self.bomb.pos==self.minibomb2.pos:
            self.bomb.randomize() 
        if self.bomb.pos==self.minibomb3.pos:
            self.bomb.randomize() 
        if self.bomb.pos==self.minibomb4.pos:
            self.bomb.randomize() 
        if self.bomb.pos==self.minibomb5.pos:
            self.bomb.randomize()

        if self.bomb1.pos==self.minibomb.pos:
            self.bomb1.randomize()
        if self.bomb1.pos==self.minibomb1.pos:
            self.bomb1.randomize() 
        if self.bomb1.pos==self.minibomb2.pos:
            self.bomb1.randomize() 
        if self.bomb1.pos==self.minibomb3.pos:
            self.bomb1.randomize() 
        if self.bomb1.pos==self.minibomb4.pos:
            self.bomb1.randomize() 
        if self.bomb1.pos==self.minibomb5.pos:
            self.bomb1.randomize()

        if self.bomb2.pos==self.minibomb.pos:
            self.bomb2.randomize()
        if self.bomb2.pos==self.minibomb1.pos:
            self.bomb2.randomize() 
        if self.bomb2.pos==self.minibomb2.pos:
            self.bomb2.randomize() 
        if self.bomb2.pos==self.minibomb3.pos:
            self.bomb2.randomize() 
        if self.bomb2.pos==self.minibomb4.pos:
            self.bomb2.randomize() 
        if self.bomb2.pos==self.minibomb5.pos:
            self.bomb2.randomize() 

        if self.bomb3.pos==self.minibomb.pos:
            self.bomb3.randomize()
        if self.bomb3.pos==self.minibomb1.pos:
            self.bomb3.randomize() 
        if self.bomb3.pos==self.minibomb2.pos:
            self.bomb3.randomize() 
        if self.bomb3.pos==self.minibomb3.pos:
            self.bomb3.randomize() 
        if self.bomb3.pos==self.minibomb4.pos:
            self.bomb3.randomize() 
        if self.bomb3.pos==self.minibomb5.pos:
            self.bomb3.randomize()

        if self.bomb4.pos==self.minibomb.pos:
            self.bomb4.randomize()
        if self.bomb4.pos==self.minibomb1.pos:
            self.bomb4.randomize() 
        if self.bomb4.pos==self.minibomb2.pos:
            self.bomb4.randomize() 
        if self.bomb4.pos==self.minibomb3.pos:
            self.bomb4.randomize() 
        if self.bomb4.pos==self.minibomb4.pos:
            self.bomb4.randomize() 
        if self.bomb4.pos==self.minibomb5.pos:
            self.bomb4.randomize()

        if self.bomb5.pos==self.minibomb.pos:
            self.bomb5.randomize()
        if self.bomb5.pos==self.minibomb1.pos:
            self.bomb5.randomize() 
        if self.bomb5.pos==self.minibomb2.pos:
            self.bomb5.randomize() 
        if self.bomb5.pos==self.minibomb3.pos:
            self.bomb5.randomize() 
        if self.bomb5.pos==self.minibomb4.pos:
            self.bomb5.randomize() 
        if self.bomb5.pos==self.minibomb5.pos:
            self.bomb5.randomize()

        if self.bomb.pos==self.dark_block.pos:
            self.dark_block.randomize()
        if self.bomb1.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.bomb2.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.bomb3.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.bomb4.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.bomb5.pos==self.dark_block.pos:
            self.dark_block.randomize()

        if self.bomb.pos==self.dark_block1.pos:
            self.dark_block1.randomize()
        if self.bomb1.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.bomb2.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.bomb3.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.bomb4.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.bomb5.pos==self.dark_block1.pos:
            self.dark_block1.randomize()

        if self.bomb.pos==self.dark_block2.pos:
            self.dark_block2.randomize()
        if self.bomb1.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.bomb2.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.bomb3.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.bomb4.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.bomb5.pos==self.dark_block2.pos:
            self.dark_block2.randomize()            
          
        if self.bomb.pos==self.dark_block3.pos:
            self.dark_block3.randomize()
        if self.bomb1.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.bomb2.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.bomb3.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.bomb4.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.bomb5.pos==self.dark_block3.pos:
            self.dark_block3.randomize() 

        if self.bomb.pos==self.dark_block4.pos:
            self.dark_block4.randomize()
        if self.bomb1.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.bomb2.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.bomb3.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.bomb4.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.bomb5.pos==self.dark_block4.pos:
            self.dark_block4.randomize() 

        if self.bomb.pos==self.dark_block5.pos:
            self.dark_block5.randomize()
        if self.bomb1.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.bomb2.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.bomb3.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.bomb4.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.bomb5.pos==self.dark_block5.pos:
            self.dark_block5.randomize()

        if self.minibomb.pos==self.dark_block.pos:
            self.dark_block.randomize()
        if self.minibomb1.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.minibomb2.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.minibomb3.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.minibomb4.pos==self.dark_block.pos:
            self.dark_block.randomize()  
        if self.minibomb5.pos==self.dark_block.pos:
            self.dark_block.randomize()

        if self.minibomb.pos==self.dark_block1.pos:
            self.dark_block1.randomize()
        if self.minibomb1.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.minibomb2.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.minibomb3.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.minibomb4.pos==self.dark_block1.pos:
            self.dark_block1.randomize()  
        if self.minibomb5.pos==self.dark_block1.pos:
            self.dark_block1.randomize() 

        if self.minibomb.pos==self.dark_block2.pos:
            self.dark_block2.randomize()
        if self.minibomb1.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.minibomb2.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.minibomb3.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.minibomb4.pos==self.dark_block2.pos:
            self.dark_block2.randomize()  
        if self.minibomb5.pos==self.dark_block2.pos:
            self.dark_block2.randomize()

        if self.minibomb.pos==self.dark_block3.pos:
            self.dark_block3.randomize()
        if self.minibomb1.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.minibomb2.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.minibomb3.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.minibomb4.pos==self.dark_block3.pos:
            self.dark_block3.randomize()  
        if self.minibomb5.pos==self.dark_block3.pos:
            self.dark_block3.randomize()

        if self.minibomb.pos==self.dark_block4.pos:
            self.dark_block4.randomize()
        if self.minibomb1.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.minibomb2.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.minibomb3.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.minibomb4.pos==self.dark_block4.pos:
            self.dark_block4.randomize()  
        if self.minibomb5.pos==self.dark_block4.pos:
            self.dark_block4.randomize()

        if self.minibomb.pos==self.dark_block5.pos:
            self.dark_block5.randomize()
        if self.minibomb1.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.minibomb2.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.minibomb3.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.minibomb4.pos==self.dark_block5.pos:
            self.dark_block5.randomize()  
        if self.minibomb5.pos==self.dark_block5.pos:
            self.dark_block5.randomize()                                                                                   
 
  
  

                


        
        
        


        
        if len(self.snake.body)>25:
            if self.bomb.pos==self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.fruit.randomize()
                self.game_over()
        if len(self.snake.body)>27:
            if self.bomb1.pos==self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize() 
                self.fruit.randomize()
                self.game_over()

        if len(self.snake.body)>29:
            if self.bomb2.pos==self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.fruit.randomize()
                self.game_over()

        if len(self.snake.body)>31:
            if self.bomb3.pos==self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.fruit.randomize()
                self.game_over()
        if len(self.snake.body)>33:
            if self.bomb4.pos==self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.fruit.randomize()
                self.game_over()

        if len(self.snake.body)>35:
            if self.bomb5.pos==self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.fruit.randomize()
                self.game_over()

        if len(self.snake.body)>14:
            if self.dark_block.pos==self.snake.body[0]:
                self.snake.body.pop(0)
                self.dark_block.randomize()
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize() 
                self.fruit.randomize()
                self.point_subtraction()
        if len(self.snake.body)>16:
            if self.dark_block1.pos==self.snake.body[0]:
                self.snake.body.pop(0)

                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
               
                self.fruit.randomize()
                self.point_subtraction()
        if len(self.snake.body)>18:
            if self.dark_block2.pos==self.snake.body[0]:
                self.snake.body.pop(0)

                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.fruit.randomize()
                self.point_subtraction()
        
        if len(self.snake.body)>14:
            if self.dark_block3.pos==self.snake.body[0]:
                self.snake.body.pop(0)
                
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()

                self.point_subtraction()
        if len(self.snake.body)>16:
            if self.dark_block4.pos==self.snake.body[0]:
                self.snake.body.pop(0)
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()

        if len(self.snake.body)>18:
            if self.dark_block5.pos==self.snake.body[0]:
                self.snake.body.pop(0)
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()





        if len(self.snake.body)>3:    
            if self.minibomb.pos == self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()
        if len(self.snake.body)>5:    
            if self.minibomb1.pos == self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()
        
        if len(self.snake.body)>7:    
            if self.minibomb2.pos == self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()


        if len(self.snake.body)>3:    
            if self.minibomb4.pos == self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()
        if len(self.snake.body)>5:    
            if self.minibomb4.pos == self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()
        
        if len(self.snake.body)>7:    
            if self.minibomb5.pos == self.snake.body[0]:
                self.minibomb.randomize()
                self.minibomb1.randomize()
                self.minibomb2.randomize()
                self.minibomb3.randomize()
                self.minibomb4.randomize()
                self.minibomb5.randomize()

                self.bomb.randomize()
                self.bomb1.randomize()
                self.bomb2.randomize()
                self.bomb3.randomize()
                self.bomb4.randomize()
                self.bomb5.randomize()

                self.dark_block.randomize()
                self.dark_block1.randomize()
                self.dark_block2.randomize()
                self.dark_block3.randomize()
                self.dark_block4.randomize() 
                self.dark_block5.randomize()
                self.fruit.randomize()
                self.point_subtraction()
            
    def check_fail(self):
        #check an snake ektos screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y < cell_number:
            self.game_over()
        #check if blocks spawn in front of the snake
        if self.bomb.pos==Vector2(1,0):
            self.bomb.randomize()
        if self.bomb.pos==Vector2(-1,0):
            self.bomb.randomize()
        if self.bomb.pos==Vector2(0,1):
            self.bomb.randomize()
        if self.bomb.pos==Vector2(0,-1):
            self.bomb.randomize()

        if self.bomb1.pos==Vector2(1,0):
            self.bomb1.randomize()
        if self.bomb1.pos==Vector2(-1,0):
            self.bomb1.randomize()
        if self.bomb1.pos==Vector2(0,1):
            self.bomb1.randomize()
        if self.bomb1.pos==Vector2(0,-1):
            self.bomb1.randomize()
        
        if self.bomb.pos2==Vector2(1,0):
            self.bomb2.randomize()
        if self.bomb2.pos==Vector2(-1,0):
            self.bomb2.randomize()
        if self.bomb2.pos==Vector2(0,1):
            self.bomb2.randomize()
        if self.bomb2.pos==Vector2(0,-1):
            self.bomb2.randomize()
        
        if self.bomb3.pos==Vector2(1,0):
            self.bomb3.randomize()
        if self.bomb3.pos==Vector2(-1,0):
            self.bomb3.randomize()
        if self.bomb3.pos==Vector2(0,1):
            self.bomb3.randomize()
        if self.bomb3.pos==Vector2(0,-1):
            self.bomb3.randomize()

        if self.bomb4.pos==Vector2(1,0):
            self.bomb4.randomize()
        if self.bomb4.pos==Vector2(-1,0):
            self.bomb4.randomize()
        if self.bomb4.pos==Vector2(0,1):
            self.bomb4.randomize()
        if self.bomb4.pos==Vector2(0,-1):
            self.bomb4.randomize()
        
        if self.bomb5.pos==Vector2(1,0):
            self.bomb5.randomize()
        if self.bomb5.pos==Vector2(-1,0):
            self.bomb5.randomize()
        if self.bomb5.pos==Vector2(0,1):
            self.bomb5.randomize()
        if self.bomb5.pos==Vector2(0,-1):
            self.bomb5.randomize()
        
        
            
             
        
        
        
        
            
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
    def point_subtraction(self):
        #afairesh enos pontou
        if len(self.snake.body) > 3:
            self.snake.body.pop(0)  
        else:
            self.fruit.randomize()
            self.minibomb.randomize()
            self.bomb.randomize()
            self.game_over()  

                    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
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
        self.snake.reset()


pygame.init()#kanei initialize to module (einai aparaitito)
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))#window
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

bomb=pygame.image.load("Graphics/bomb1.png").convert_alpha() 
bomb1=pygame.image.load("Graphics/bomb1.png").convert_alpha() 
bomb2=pygame.image.load("Graphics/bomb1.png").convert_alpha()
bomb3=pygame.image.load("Graphics/bomb1.png").convert_alpha() 
bomb4=pygame.image.load("Graphics/bomb1.png").convert_alpha() 
bomb5=pygame.image.load("Graphics/bomb1.png").convert_alpha()

minibomb=pygame.image.load("Graphics/minibomb.png").convert_alpha()
minibomb1=pygame.image.load('Graphics/minibomb.png').convert_alpha()
minibomb2=pygame.image.load('Graphics/minibomb.png').convert_alpha()
minibomb3=pygame.image.load("Graphics/minibomb.png").convert_alpha()
minibomb4=pygame.image.load('Graphics/minibomb.png').convert_alpha()
minibomb5=pygame.image.load('Graphics/minibomb.png').convert_alpha()

dark_block=pygame.image.load('Graphics/Block.png').convert_alpha() 
dark_block1=pygame.image.load('Graphics/Block.png').convert_alpha()
dark_block2=pygame.image.load('Graphics/Block.png').convert_alpha()
dark_block3=pygame.image.load('Graphics/Block.png').convert_alpha() 
dark_block4=pygame.image.load('Graphics/Block.png').convert_alpha()
dark_block5=pygame.image.load('Graphics/Block.png').convert_alpha()


game_font = pygame.font.Font(None ,25) #bale font !!!!!!!!
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #animation timer
#main game

main_game = MAIN()

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()#kleinei to game
           sys.exit()
       if event.type == SCREEN_UPDATE:
            main_game.update()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               if main_game.snake.direction.y !=1:   
                    main_game.snake.direction = Vector2(0,-1)
           if event.key == pygame.K_DOWN:
               if main_game.snake.direction.y !=-1:
                    main_game.snake.direction = Vector2(0,1)
           if event.key == pygame.K_RIGHT:
               if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(1,0)
           if event.key == pygame.K_LEFT:
               if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1,0)
               

    screen.fill((175,215,70))
    main_game.draw_elements()
    #edw pane ta graphic elements
    pygame.display.update()
    clock.tick(60)#framerate --> 60fps locked :)

