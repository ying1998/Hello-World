from sys import exit
from random import randint

def death():
    quips = [" You died.  You kinda suck at this.","Nice job,you died ...jackass.", "Such a luser."."I have a small puppy that's better at this."]
    print quips[randint(0,len(quips)-1)]
    exit(1)

def central_corridor():
    print "The Gothons of Planet Percal #25 have invaded your ship and destoryed"
    print "your entire crew. You are the last surviving member and your last"
    print "mission is to get the neutron destruct bomb from the Weapons Armory,"
    print "put it in the bridge, and blow the ship up after getting into an"
    print "escape pod."
    print "\n"
    print "You're running down the central corridor to the weapons Armory when"
    print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clow costume"
    print "flowing around his hate filled body.  He's blocking the door to the"
    print "Armory and about to pull a weapon to blast you."

    action = raw_input("> ")

    if action == "shoot!" :
        print "Quick on the draw you yank out your blaster and fire it at the Gothon."
        print "His clown costume is flowing and moving around his body, which throws"
        print "off your aim. Your laser hits his costume but misses him entirely. This"
        print "completely ruins his brand new costume his mother bought him,which"
        print "makes him fly into an insane rage and blast you repeatedly in the face until"
        print "you are dead. Then he eats you."
        return 'death'

    elif action == "dodge!":
        print "like a world class boxer you dodge, weave,slip and slide right"
        print "as the Gothon's blaster cranks a laser past your head."
        print "In the middle of your artful dodge your foot slips and you“
        print "bang your head on the metal wall and pass out."
        print "You wake up shortly after only to die as the Gothon stomps on"
        print "your head and eats you ."
        return 'death'


    elif action == "tell a joke":
        print "Luck for you they made you learn Gothon insults in the academy."
        print "You tell the one Gothon joke you know:"
        print "Lbhe zbgure asfkn gllslgjngklg;lasjfdsf lsjsdlgsfkgns  kgrsngklslgk sgm k."
        print "The Gothon stops , tries not to laugh,then busts out laughing and can't move."
        print "While he's laughing you run up and shoot him square in the head"
        print "putting him down, then jump through the Weapon Armory door."
        return 'laser_weapon_armory'

    else:
        print "DOES NOT COMPUTE! "
        return ' central_corridor'
