class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


print("Blu is a {}".format(blu.__class__.species))
blu = Parrot("Blu", 10)
blu.name = "mike"
print("cool", blu.name)






