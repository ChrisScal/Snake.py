import pygame as pygame
import sys,random
from pygame.math import Vector2
#test
class Snake:
    #To fydi
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)    
        self.new_block = False 

    def draw_snake(self):
        for block in self.body:
            #create rect
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            block_rect = pygame.Rect(x_pos, y_pos ,cell_size ,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
            #draw the rectangle
            
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


class Fruit :
    def __init__(self) :
        #x,y position
        self.randomize() #oti briskotan sth methodo randmize htan edw alla gia oikonomia xwroi aplws thn kaloume

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size ,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
        #draw rect

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)#disdiastatos pinakas syntetagmenwn (bloebei anti gia lista argotera)
        

class MAIN :
    
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        pygame.mixer.music.set_volume(0.1)
        #self.play_background_sound()

 #se sxolio ki auto cause perimenw to menu gia gameover
    ''' def play_game_over_sound(self):
        self.sound_gameover = pygame.mixer.Sound("Game_over.mp3") 
        self.sound_gameover.play()''' 

    #giam giam noises, poly satisfying 
    def play_crunch_sound(self):
        pygame.mixer.music.load("Apple-bite.mp3") 
        pygame.mixer.music.play()
        

    def open_crunch_sd(self):
        self.play_crunch_sound()
        pygame.mixer.music.set_volume(0.5)

    def mute_crunch_sound(self):
        self.play_crunch_sound()
        pygame.mixer.music.set_volume(0) 
        
    #gia strofes
    def play_turn_sd(self):
        pygame.mixer.music.load("turn_2.wav") 
        pygame.mixer.music.play()

    def open_turn(self):
        self.play_turn_sd()
        pygame.mixer.music.set_volume(0.5)
    
    def mute_turn_sound(self):
        self.play_turn_sd()
        pygame.mixer.music.set_volume(0)
    
    #to perifhmo pillarmen theme, to exw ws sxolio gia na to energopoihsw otan ftia3ete to menu
    '''def play_background_sound(self):
        pygame.mixer.music.load("Pillar_men.mp3.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(100)'''
    
    def update(self):
       self.snake.move_snake() 
       self.check_collision()
       self.check_fail()
    
    def mute_sound(self):
        self.mute_crunch_sound()
        self.mute_turn_sound()
    
    def play_sound(self):
        self.play_crunch_sound()
        self.play_turn_sd
    
    def open_sd(self):
        self.open_crunch_sd()
        self.open_turn()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.play_crunch_sound()
            self.fruit.randomize()
            #reposition to mhlo
            self.snake.addblock()
            #+1 block sto snecko
            
    def check_fail(self):
        #check an snake ektos screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0<= self.snake.body[0].y < cell_number:
            #self.play_game_over_sound()
            self.game_over()
            
        #check kanibalismos
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                #self.play_game_over_sound()
                self.game_over()         

    def game_over(self):
        pygame.quit()
        sys.exit()
        #gia thn wra


pygame.init()#kanei initialize to module (einai aparaitito)
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))#window
clock = pygame.time.Clock()
pygame.display.set_caption('Snake Game')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #animation timer

sound = False #peiramatiko stadio

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
                    main_game.play_turn_sd()
           if event.key == pygame.K_DOWN:
               if main_game.snake.direction.y !=-1:
                    main_game.snake.direction = Vector2(0,1)
                    main_game.play_turn_sd()
           if event.key == pygame.K_RIGHT:
               if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(1,0)
                    main_game.play_turn_sd()
           if event.key == pygame.K_LEFT:
               if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1,0)
                    main_game.play_turn_sd()
            #sorry xrhsto alla eprepe         
           if event.key == pygame.K_w:
               if main_game.snake.direction.y !=1:   
                    main_game.snake.direction = Vector2(0,-1)
                    main_game.play_turn_sd()
           if event.key == pygame.K_s:
               if main_game.snake.direction.y !=-1:
                    main_game.snake.direction = Vector2(0,1)
                    main_game.play_turn_sd()
           if event.key == pygame.K_d:
               if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(1,0)
                    main_game.play_turn_sd()
           if event.key == pygame.K_a:
               if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1,0)
                    main_game.play_turn_sd()
           #gia mute ton hxo         
           if event.key == pygame.K_m:
               sound= not sound
               if sound == False:
                   main_game.mute_sound()
               else:
                   main_game.open_sd()
               
               
    
    
               

    screen.fill((175,215,70))
    main_game.draw_elements()
    #edw pane ta graphic elements
    pygame.display.update()
    clock.tick(60)#framerate --> 60fps locked :)
    
