# flyweight method - structural design pattern
#   minimize the number of objects at run-time -> create an immutable flyweight
#   object which is shared by multiple contexts while being indistinguishable
#   from a "normal" object that is not shared


# create base class
class BulletContext:
    def __init__(self, x, y, z, velocity):
        self.x = x
        self.y = y
        self.z = z
        self.velocity = velocity
        

# create flyweight class
# - helps in improving the Data Caching
# - save a lot of space in RAM
# - ultimately leads to improve in performance because we are using less number
#   of heavy objects
class BulletFlyweight:
    def __init__(self):
        self.asset = '■■►'
        self.bullets = []
        
    def bullet_factory(self, x: float, y: float, z: float, velocity: float) \
        -> BulletContext:
            bull = [b for b in self.bullets if b.x==x and b.y==y and b.z==z and b.velocity==velocity]
            if not bull:
                bull = BulletContext(x,y,z,velocity)
                self.bullets.append(bull)
            else:
                bull = bull[0]
                
            return bull
        
    def print_bullets(self):
        print('Bullets:')
        for bullet in self.bullets:
            print(f'{bullet.x} {bullet.y} {bullet.z} {bullet.velocity}')


# run method
if __name__ == '__main__':
    bf = BulletFlyweight()

    # adding bullets
    bf.bullet_factory(1,1,1,1)
    bf.bullet_factory(1,2,5,1)

    bf.print_bullets()