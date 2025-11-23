from bob import Bob
from spring import Spring

def setup():
    global bob, spring
    size(600, 600)
    bob = Bob(width/2, height/2 - 100, 50)
    spring = Spring(width/2, 10, height/2-10)
    
                    
def draw():
    global bob, spring
    
    background(125)
    
    gravity = PVector(0, 1)
    bob.applyForce(gravity)

    
    spring.connect(bob)
    
    bob.update()
    bob.display()
    
    spring.display()
    spring.displayLine(bob)
