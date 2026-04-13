import math, stddraw
# Francois Cooper
class bullet:
    def __init__(self, x, y, angle, velocity):
        self.active = True
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = velocity
        
    def move(self): # Francois Cooper | bullet trajectory and draw
        self.x += self.velocity * math.cos(self.angle)
        self.y += self.velocity * math.sin(self.angle)
        if self.x >= 1 or self.x <= 0 or self.y >= 1 or self.y <= 0:
            self.active = False
        self.draw()

    def draw(self): # Francois Cooper | draw bullet
        if self.active:
            stddraw.filledCircle(self.x, self.y, 0.01)

class bullet_manager:
    def __init__(self):
        self.bullet_array = []

    def shoot(self, x, y, angle, velocity): # Francois Cooper | creates new bullet and appends to bullet_array
        new_bullet = bullet(x, y, angle, velocity)
        self.bullet_array.append(new_bullet)

    def update(self): # Francois Cooper | updates bullets each frame 
        for i in self.bullet_array:
            i.move()
        self.remove()

    def remove(self): # Francois Cooper | Removes inactive bullets from bullet_array
        new_array = []
        for i in self.bullet_array:
            if i.active:
                new_array.append(i)
        self.bullet_array = new_array



        

