# Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

# This constant data of an object is usually called the intrinsic state. It lives within the object; other objects can only read it, not change it. The rest of the object’s state, often altered “from the outside” by other objects, is called the extrinsic state.

# Use the Flyweight pattern only when your program must support a huge number of objects which barely fit into available RAM.


class Flyweight:
    def __init__(self, name, color, size):
        self._intrinsic_state = (name, color, size)

    def operation(self, extrinsic_state):
        # Perform some operation using both intrinsic and extrinsic state
        print(f"Intrinsic State: {self._intrinsic_state}, Extrinsic State: {extrinsic_state}")

class FlyweightFactory:
    _list_flyweights = {}
    def __init__(self,elements):
        for ele in elements:
            self._list_flyweights[ele[0]] = Flyweight(*ele)

    def get_flyweight(self, name):
        key = name
        return self._list_flyweights[key]

def add_particles_to_canvas(particle_name,speed, direction):
    flyweight = factory.get_flyweight(particle_name)
    flyweight.operation((particle_name, speed, direction))

if __name__ == "__main__":
    # Example usage
    elements = [
        ("bullet", "golden", "Small"),
        ("gun", "grey", "Medium"),
        ("missile", "green", "Large"),
    ]

    factory = FlyweightFactory(elements)

    # Simulating adding particles to a canvas
    add_particles_to_canvas("bullet", 10, "North")
    add_particles_to_canvas("gun", 15, "East")
    add_particles_to_canvas("missile", 20, "South")
    add_particles_to_canvas("bullet", 12, "West")  # Reusing existing flyweight
