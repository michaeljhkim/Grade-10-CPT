#global
def s():
    global t
    print(t)
    t = "poo"
    print(t)

t = "butt"
s()
