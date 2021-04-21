'''
Chicken
    - State: 
        - hunger(value 1-10)
        - alive (T/F)
        - breed
    -What is does:
        - eat/peck
        - lay eggs
        - make sound(chirp)
'''

class Chicken:

    def __init__(self, breed):
        self.breed = breed
        self.hunger = 10
        self.alive = True

    def heartbeat(self):
        self.hunger-=1
        if self.hunger < 0 or self.hunger > 10:
            self.alive = False
            print(f'{self.breed} ded')

    def eat(self):
        if self.alive:
            self.heartbeat
            self.hunger+=2


    def sonify(self):
        if self.alive:
            print("chicken sounds")
            self.heartbeat()


def main():
    d = Chicken('dorking')
    h = Chicken('hamburg')
    for i in range(11):
        d.eat()
        d.sonify()
        h.sonify()
        
main()

