
class Spring(object):
    def __init__(self, x, y, l):

        self.anchor = PVector(x, y)
        self.leng = l
        self.k = 0.1
        
    def connect(self, bob):
        force = PVector.sub(bob.location, self.anchor)
        d = force.mag()
        stretch = d-self.leng
        
        force.normalize()
        force.mult(-1*self.k*stretch)
        
        bob.applyForce(force)
        
    def display(self):
        fill(100)
        rectMode(CENTER)
        rect(self.anchor.x, self.anchor.y, 10, 10)
        
    def displayLine(self, bob):
        stroke(255)
        line(bob.location.x, bob.location.y, self.anchor.x, self.anchor.y)
        
        
        
