class Bob(object):
    def __init__(self, x, y, mass):
        self.location = PVector(x, y)
        self.velocity = PVector(0,0)
        self.acceleration = PVector(0,0)
        self.mass = mass
        self.damping = 0.99
        
    
    def display(self):
        fill(255)
        stroke(0)
        strokeWeight(5)
        rect(self.location.x, self.location.y+self.mass/2, self.mass, self.mass)
        
        
    def update(self):
        self.velocity+=self.acceleration
        self.velocity*=self.damping
        self.location += self.velocity
        
        self.acceleration.mult(0)
        
        
    def applyForce(self, force):
        self.acceleration += force  
        
                    
