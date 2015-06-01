from humans import Anastasis
import pywapi, bs4, urllib2, random, time

location_ids = {
    'Manhattan': 'USNY0996',
    'Moscow': 'RSXX0063',
    'Tokyo': 'JAXX0085',
    'Paris': 'FRXX0076'
}

def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32

def get_weather(name):
    location_id = location_ids[name]
    weather = pywapi.get_weather_from_weather_com(location_id)
    temperature = weather['current_conditions']['temperature']
    return celsius_to_fahrenheit(float(temperature))

def tell_temperatures():
    for city, location_id in location_ids.items():
        Anastasis.voice.say("The temperature in {0} right now is {1} degrees Fahrenheit".format(city, get_weather(city)))

positive_adjectives = ['adaptable', 'adventurous', 'affable', 'affectionate', 'agreeable',
                       'ambitious', 'amiable', 'amicable', 'amusing', 'brave', 'bright',
                       'broad-minded', 'calm', 'careful', 'charming', 'communicative',
                       'compassionate', 'conscientious', 'considerate', 'convivial',
                       'courageous', 'courteous', 'creative', 'decisive', 'determined',
                       'diligent', 'diplomatic', 'discreet', 'dynamic', 'easygoing',
                       'emotional', 'energetic', 'enthusiastic', 'exuberant', 'fair-minded',
                       'faithful', 'fearless', 'forceful', 'frank', 'friendly', 'funny',
                       'generous', 'gentle', 'good', 'gregarious', 'hard-working', 'helpful',
                       'honest', 'humorous', 'imaginative', 'impartial', 'independent',
                       'intellectual', 'intelligent', 'intuitive', 'inventive', 'kind',
                       'loving', 'loyal', 'modest', 'neat', 'nice', 'optimistic', 'passionate',
                       'patient', 'persistent', 'pioneering', 'philosophical', 'placid',
                       'plucky', 'polite', 'powerful', 'practical', 'pro-active',
                       'quick-witted', 'quiet', 'rational', 'reliable', 'reserved',
                       'resourceful', 'romantic', 'self-confident', 'self-disciplined',
                       'sensible', 'sensitive', 'shy', 'sincere', 'sociable', 'straightforward',
                       'sympathetic', 'thoughtful', 'tidy', 'tough', 'unassuming',
                       'understanding', 'versatile', 'warmhearted', 'willing', 'witty']

def give_speech():
    stage = Anastasis.vision.find("stage")
    Anastasis.movement.turn_towards(stage)
    Anastasis.movement.start_walking()
    Anastasis.movement.stop_walking()
    Anastasis.movement.turn_around()

    microphone = Anastasis.vision.find("microphone")
    Anastasis.body.grab(microphone)
    Anastasis.body.pull(microphone)

    Anastasis.voice.say("Hello everyone!")
    Anastasis.voice.say("My name is Anastasis")
    Anastasis.voice.say("I'm one of the students at SFPC")
    Anastasis.voice.say("I would describe my time at SFPC as")
    for adjective in random.sample(positive_adjectives, 5):
        Anastasis.voice.say(adjective)
        time.sleep(1)

    Anastasis.voice.say("I made a lot of great new friends")
    Anastasis.voice.say("And I also made a project!")

    for i in range(3):
        Anastasis.body.jump()

    Anastasis.voice.say("The project is called Human Action Code")
    Anastasis.voice.say("It's a framework for programming humans to perform arbitrary actions in the world")
    Anastasis.voice.say("And it's also generating everything I'm doing right now")

    Anastasis.movement.rotate(45)
    Anastasis.right_hand.extend()
    Anastasis.right_hand.release()

    Anastasis.face.smile()
    Anastasis.voice.say("You could say I'm the first programmable human being")

    Anastasis.body.thinking_pose()

    Anastasis.voice.say("Why did I make it?")
    Anastasis.voice.say("Because everyone is trying to make machines that pass the Turing Test")
    Anastasis.voice.say("But I want to make humans that fail the Turing Test")

    Anastasis.voice.say("With Human Action Code the Internet enters my body")
    Anastasis.voice.say("and expresses itself through it")
    Anastasis.voice.say("I have access to every real-time information stream available online")

    tell_temperatures()

