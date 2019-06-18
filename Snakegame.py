
#snake using pygame
#By HappySword
import pygame
import time
import random
import tkinter as tk
from tkinter import messagebox

class block(object):
    
   def __init__(self, position,dirx = 0, diry= 1, color = (0,200,255) ):
       self.color = color
       self.position = position
       self.dirx = dirx
       self.diry = diry
       
   def move(self, dirx, diry):
       self.dirx = dirx
       self.diry = diry
       self.position=(self.position[0] + self.dirx, self.position[1] + self.diry)
       
   def draw(self, window, eyes , width, shape = 1):
       #change it later to a circle
       self.width = width
       i = self.position[0]
       j = self.position[1]
       if shape == 0 :
           pygame.draw.circle(window, self.color, (i*width, j*width), width // 2 , 0)
       elif shape == 1:
           pygame.draw.rect(window, self.color, (i*width+1, j*width+1, width-1, width-1))
       #add eyes later

class snake(object):
    body = []
    turns = {}
    
    def __init__(self, color, position, window):
        self.color = color
        self.head = block(position)
        self.body.append(self.head)
        self.window = window
        self.dirx = 0
        self.diry = 1     #change them to be random later
        
    def reset(self,position):
        self.body = []
        self.turns = {}
        self.head = block(position)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1 
        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            Keys = pygame.key.get_pressed()
            for key in Keys:
                if Keys[pygame.K_UP] == 1:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.position[:]] = [self.dirx,self.diry]
                    
                elif Keys[pygame.K_DOWN] == 1:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.position[:]] = [self.dirx,self.diry]
                    
                elif Keys[pygame.K_LEFT] == 1:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.position[:]] = [self.dirx,self.diry]
                    
                elif Keys[pygame.K_RIGHT] == 1:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.position[:]] = [self.dirx,self.diry]
                    
        for i, c in enumerate (self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirx == 1 and c.position[0] >= rowandcol-1 : c.position = (0, c.position[1])
                elif c.dirx == -1 and c.position[0] <= 0 : c.position = (rowandcol-1, c.position[1])    
                elif c.diry == 1 and c.position[1] >= rowandcol : c.position = (c.position[0], 0)
                elif c.diry == -1 and c.position[1] <= 0 : c.position= (c.position[0], rowandcol-1)
                else: c.move(c.dirx ,c.diry)
                
                
    def draw(self, width):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(self.window,True, width)
            else: 
                c.draw(self.window,False, width)
    
    def addCube(self):
        tail = self.body[-1]
        dx = tail.dirx
        dy = tail.diry
        
        if dx == 1 and dy == 0:
            self.body.append(block((tail.position[0]-1,tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(block((tail.position[0]+1,tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(block((tail.position[0],tail.position[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(block((tail.position[0],tail.position[1]+1)))
    
        self.body[-1].dirx = dx
        self.body[-1].diry = dy
        
    
def createGrid(dimension,rowandcol,surface):
    # change it so it would be circles instead of squares
    distance= dimension // rowandcol
    x = distance
    y = distance 
    for i in range (rowandcol):
        pygame.draw.line(surface, (20,20,20), (x,0), (x,dimension) )
        pygame.draw.line(surface, (20,20,20), (0,y), (dimension,y) )
        x+=distance
        y+=distance

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def drawCircleGrid(dimension, rowandcol, window):
    distance= dimension // rowandcol
    for i in range (1,rowandcol):
        for j in range(1,rowandcol):
            pygame.draw.circle(window, (200,200,200),(i*distance,j*distance)  , distance // 2 , 1)
           
    
    
def reDrawWindow(dimension, rowandcol, surface, snake, snack):
    surface.fill((50,50,50))
    #drawCircleGrid(dimension, rowandcol, surface)
    createGrid(dimension, rowandcol, surface)
    snake.draw(dimension // rowandcol)
    snack.draw(surface, False, dimension // rowandcol)
    pygame.display.update()
   
def randomSnack(snake):
    while True:
        x = random.randrange(rowandcol-1)
        y = random.randrange(rowandcol-1)
        flag = False
        for block in snake.body:
            if block.position[0] == x and block.position [1] == y:
                flag = True
        if not flag:
            break
    return (x,y)
        
        
        
def main():
    pygame.init()
    length = 500
    global rowandcol
    rowandcol = 20
    window = pygame.display.set_mode((length,length))
    s = snake((0,200,255), (rowandcol//2,rowandcol//2), window)
    snack = block(randomSnack(s),0,1,(0,255,0))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 80)
    font1 = pygame.font.SysFont("Verdana", 40)
    gName = font.render("Snake", True, (0,200,255))
    message = font1.render("Press Space to Play...", True, (0,200,255))
    window.fill((50,50,50))
    window.blit(gName, (120,100))
    window.blit(message, (40,250))
    pygame.display.update()
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    while True:
        pygame.time.delay(70)
        clock.tick(12)
        s.move()
        if s.body[0].position == snack.position:
            s.addCube()
            snack = block(randomSnack(s),0,0,(0,255,0))
        for b in s.body:
            if b != s.head and b.position == s.head.position:
                message_box("You Lost!", "Play Again \n Your Score Was : "+str(len(s.body)))
                s.reset((rowandcol//2,rowandcol//2))
        reDrawWindow(length, rowandcol, window, s, snack)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    pass
    
main()