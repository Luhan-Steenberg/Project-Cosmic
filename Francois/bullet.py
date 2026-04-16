import math, stddraw
# Francois Cooper
class bullet:
    def __init__(self, x, y, angle, velocity):
        # Francois Cooper | initialises bullet position, angle and velocity
        self.active = True
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = velocity
        
    def move(self):
        # Francois Cooper | bullet trajectory and draw
        self.x += self.velocity * math.cos(self.angle)
        self.y += self.velocity * math.sin(self.angle)
        if self.x >= 1 or self.x <= 0 or self.y >= 1 or self.y <= 0:
            self.active = False
        self.draw()

    def draw(self): 
        # Francois Cooper | draw bullet method
        if self.active:
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledCircle(self.x, self.y, 0.01)

class bullet_manager:
    def __init__(self):
        # Francois Cooper | initialises bullet array
        self.bullet_array = []

    def shoot(self, x, y, angle, velocity): 
        # Francois Cooper | creates new bullet and appends to bullet_array
        new_bullet = bullet(x, y, angle, velocity)
        self.bullet_array.append(new_bullet)

    def update(self): 
        # Francois Cooper | updates bullets each frame 
        for i in self.bullet_array:
            i.move()
        self.remove()

    def remove(self): 
        # Francois Cooper | Removes inactive bullets from bullet_array
        new_array = []
        for i in self.bullet_array:
            if i.active:
                new_array.append(i)
        self.bullet_array = new_array

    def check_collision(self, enemy_array, explosion_manager):
        # Francois Cooper | checks for collision and removes bullet and enemy from their respective lists and creates a new explosion
        for i in self.bullet_array:
            for j in enemy_array:
                distance = math.sqrt((i.x - j.x)**2 + (i.y - j.y)**2)
                if distance <= 0.05:
                    i.active = False
                    j.active = False
                    explosion_manager.new_explosion(i.x, i.y)

class explosion:
    def __init__(self, x, y):
        # Francois Cooper | Initialises explosion
        self.active = True
        self.x = x
        self.y = y
        self.frames = 15
        self.radius = 0.01

    def boom(self):
        # Francois Cooper | Draws explosion
        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.filledCircle(self.x, self.y, self.radius * 2)
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledCircle(self.x, self.y, self.radius * 1.5)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledCircle(self.x, self.y, self.radius)

    def tick_tick(self):
        # Francois Cooper | Counts down frames and increases explosion size each frame
        self.boom()
        self.frames -= 1
        self.radius += 0.005
        if self.frames <= 0:
            self.active = False
        
class explosion_manager:
    def __init__(self):
        # Francois Cooper | Initialises explosion array
        self.explosion_array = []

    def new_explosion(self, x, y): 
        # Francois Cooper | creates new explosion and appends to explosion_array
        new = explosion(x, y)
        self.explosion_array.append(new)

    def update(self): 
        # Francois Cooper | updates explosions each frame 
        for i in self.explosion_array:
            i.tick_tick()
        self.remove()

    def remove(self): 
        # Francois Cooper | Removes inactive explosions from explosion_array
        new_array = []
        for i in self.explosion_array:
            if i.active:
                new_array.append(i)
        self.explosion_array = new_array



        


                    





        

