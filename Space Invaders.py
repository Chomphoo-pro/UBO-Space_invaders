#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import tkinter as tk
from tkinter import *
from time import *
import tkinter as tk



class SpaceInvaders(object):
    '''
    Main Game class
    '''
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Space Invaders")
        self.frame = tk.Frame(self.root)
        self.frame.pack(side="top", fill="both")
        self.game = Game(self.frame)
       
        
        
    def play(self):
        self.game.start_animation()
        self.root.mainloop()

        
        
class Game(object):
    def __init__(self, frame):
        self.frame = frame
        self.fleet = Fleet()
        self.defender = Defender()
        self.height = 800
        self.width = self.fleet.get_width()
        self.canvas = tk.Canvas(self.frame, width = 420, height = 320, bg = 'black')
        self.canvas.pack()
        self.defender.install_in(self.canvas)
        self.fleet.install_in(self.canvas)
        
    def animation(self):
        return 0
    
    def start_animation(self):
        pass
        
    
    def move_bullets(self):
        return 0
    
    def move_aliens_fleet(self):
        return 0
    
       
        

        


#Création du defender
class Defender(object):
    def __init__(self):
        self.width = 20
        self.height = 20
        self.move_delta = 20
        self.x = 230
        self.y = 300
        self.id = None
        self.max_fired_bullets = 8
        self.fired_bullets = []
        
        
    def get_x(self):
        return self.x
    
    def set_x(self, v):
        self.x = v
        
        
    def get_y(self):
        return self.y
    
    def set_y(self, v):
        self.y = v
        
        
    def get_id(self):
        return self.id
    
    def set_id(self, v):
        self.id = v
        
        
        
    def get_width(self):
        return self.width
    
    def set_width(self, v):
        self.width = v
        
        
        
    def get_height(self):
        return self.height
    
    def set_height(self, v):
        self.height = v

        
    
    def install_in(self, canvas):
        a = Alien()
        a.install_in(canvas, 100, 100, "alien.gif", "alienTag") #test barbare de creation d'alien
        x = self.get_x()
        y = self.get_y()
        L = self.get_width()
        H = self.get_height()
        canvas.focus_set()
        
        def events(event): #Action du defender Partie CONTROL
            if (event.keysym == "Left"):
                dx = -1 #modifie le delta x
                self.move_in(canvas, dx) #déplace le carré en soustration la position initial avec dx

            elif (event.keysym == "Right"):
                dx = 1
                self.move_in(canvas, dx)

            elif (event.keysym == "space"): #méthode de lancement de la bulette
                self.fire(canvas)
            else:
                print(event.keysym)
            

        self.set_id(canvas.create_rectangle(x, y, x+L, y+H, fill='white')) #créer le defender
        canvas.bind("<Key>",events) #detecte les touches

        
    

            
    def move_in(self, canvas, dx):
        L = 480 #longueur de la fenetre
        w = self.get_width() #longueur du defender
        x = self.get_x() #position du defender
        movex = self.move_delta * dx #calcul du deplacement de pixel
        
        if (-w <= x+movex and x+movex <= L):
            self.x += movex
            canvas.move(self.id, movex, 0)
        #else:
            #print("x: "+str(x)+"/"+str(self.x)+" - dx: "+str(dx)+" - L: "+str(L)+" - l: "+str(l))

            
    
    def fire(self, canvas):#Tire une bullette
        lesBullets = self.fired_bullets
        nbrBullets = len(lesBullets)
        maxBullets = self.max_fired_bullets
        if (nbrBullets < maxBullets):
            bullet = Bullet(self)
            lesBullets.append(bullet)
            bullet.install_in(canvas)

                
 
            
        
        
        
    
    
#Création d'une boule 
class Bullet(object):
    def __init__(self, shooter):
        self.radius = 10
        self.color = "red"
        self.speed = 4
        self.id = None
        self.shooter = shooter
    
    def install_in(self, canvas):
        self.y = self.shooter.y
        x = self.shooter.x
        y = self.y
        
        color = self.color
        r = self.radius
        self.test = 0
        self.id = canvas.create_oval(x, y + 5, x+r, y + 5 +r, fill=color)
        #supprime 1 boulette
        self.move_in(canvas)
        

    def move_in(self, canvas):
        self.y -= self.speed
        r = self.radius
        if (self.y > 0 - r*2): #deplace en haut
            canvas.move(self.id, 0, -self.speed)
            canvas.after(19, lambda: self.move_in(canvas))
        else: # supprimer quand il arrive en haut
            canvas.delete(self.id)
            self.shooter.fired_bullets.pop()
        
        

        
        
#Création d'un alien
class Alien(object):
    def __init__(self):
        self.id = None
        self.alive = True
        #self.move_delta = 5
        


    def touched_by(self, canvas, projectile):
        return 0
    
    def install_in(self, canvas, x, y, image, tag):
        self.pim = PhotoImage(file=image)
        canvas.create_image(100, 100, image=self.pim, tags=tag)
        

    def move_in(self, canvas, dx, dy):
        movex = self.move_delta * dx
        movey = self.move_delta * dy
        canvas.move(self.id, movex, movey)
        
        
        
        
#création d'un groupe d'aliens
class Fleet(object):
    def __init__(self):
        self.aliens_lines = 5
        self.aliens_columns = 10
        self.aliens_inner_gap = 20
        self.alien_x_delta = 5
        self.alien_y_delta = 15
        fleet_size = self.aliens_lines * self.aliens_columns
        self.aliens_fleet = [None] * fleet_size
        
    def get_width(self):
        return -1
        
        
        
    def install_in(self, canvas):
        unAlien = Alien()
        unAlien.install_in(Canvas, 100, 100, "alien.gif", "tag")
        
    def move_in(self, canvas):
        return 0
        
    def manage_touched_aliens_by(self, canvas, defender):
        return 0
    
    
        
    
    
spaceInvaders = SpaceInvaders()
spaceInvaders.play()


# In[ ]:





# In[32]:





# In[ ]:





# In[1]:


from tkinter import *



class Example2:
    def __init__(self):
        x=0
        
    def install_in(self,canvas):
        self.pim = PhotoImage(file="alien.gif")
        
        canvas.create_image(100, 100, image=self.pim)
        canvas.create_line(15, 25, 200, 25)
    

        

class Example:
    def __init__(self):
        self.root = Tk()
        self.canvas_width = 1000
        self.canvas_height = 400
        
        self.canvas = Canvas(self.root, width=self.canvas_width, height = self.canvas_height)
        self.canvas.pack()

    def install(self):
        ex =Example2()
        ex.install_in(self.canvas)
        

    def start(self):
        self.root.mainloop()
        
ex = Example()
ex.install()
ex.start()


# In[ ]:




