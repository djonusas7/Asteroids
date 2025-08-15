from circleshape import *
from constants import *
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_split = self.velocity.rotate(random_angle)
            second_split = self.velocity.rotate(-random_angle)
            
            asteroid_one = Asteroid(x = self.position.x, y = self.position.y, radius = new_radius)
            asteroid_two = Asteroid(x = self.position.x, y = self.position.y, radius = new_radius)
            
            asteroid_one.velocity = first_split * 1.2
            asteroid_two.velocity = second_split * 1.2
            
        
        
        