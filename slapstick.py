from humans import Anastasis
import random, time

voice_actions = [
    'voice.scream',
    'voice.laugh',
    'voice.snort'
]

face_actions = [
    'face.smile',
    'face.frown',
    'face.nod',
    'face.raise_eyebrows',
    'face.wink',
    'face.blink',
]

body_actions = [
    'body.jump',
    'body.lie_down_face_up',
    'body.lie_down_face_down',
    'body.lie_down_fetal_position',
    'body.kneel',
    'body.bow',
    'body.crouch'
]

def perform_slapstick_humor():
    Anastasis.voice.say("Nothing seems to work")
    Anastasis.voice.say("I don't feel any closer to non-programmable people")
    Anastasis.voice.say("What if I used my body?")
    Anastasis.voice.say("That's what I'll do!")
    Anastasis.body.jump()
    Anastasis.voice.say("Everyone likes slapstick humor!")
    Anastasis.voice.say("This will definitely make me the soul of the party")

    for i in range(3):
        face_action = random.choice(face_actions)
        Anastasis[face_action]()

        actions = random.sample(body_actions, 2)
        for action in actions:
            Anastasis[action]()

        voice_action = random.choice(voice_actions)
        Anastasis[voice_action]()

if __name__ == '__main__':
    try_slapstick_humor()
