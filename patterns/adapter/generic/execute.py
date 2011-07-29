from dog import Dog
from cat import Cat
from generic_implementation import Person, CreatureAdapter

def exercise_system():
    person = Person("Bob")
    fido = Dog("Fido")
    canine = CreatureAdapter(fido, fido.bark)
    whiskers = Cat("Whiskers")
    feline = CreatureAdapter(whiskers, whiskers.meow)

    for critter in (person, canine, feline):
        print critter.name, "says", critter.make_noise()
        
exercise_system()