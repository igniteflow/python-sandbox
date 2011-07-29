from dog import Dog
from non_generic_implementation import Person, DogAdapter

def exercise_system():
    person = Person("Bob")
    canine = DogAdapter(Dog("Fido"))

    for critter in (person, canine):

        print critter.name, "says", critter.make_noise()

if __name__ == "__main__":
    exercise_system()