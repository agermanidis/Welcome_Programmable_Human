import random, time
from humans import Anastasis

def stare_at_people():
    Anastasis.voice.say("Now I just want to connect with everyone!")
    Anastasis.voice.say("Okay, I'll give social interaction a try")

    for i in range(3):
        human = Anastasis.vision.search("human")
        Anastasis.movement.turn_towards(human)
        Anastasis.movement.start_walking()
        time.sleep(1)
        Anastasis.movement.stop_walking()
        Anastasis.face.stare_at(human)
        time.sleep(2)

if __name__ == '__main__':
    stare_at_people()

