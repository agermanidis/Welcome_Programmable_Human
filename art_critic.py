from humans import Anastasis
import urllib2, bs4, subprocess, random, time

# concepts borrowed from artybollocks.com
concepts = [
    "postmodern discourse",
    "unwanted gifts",
    "Critical theory",
    "copycat violence",
    "Pre-raphaelite tenets",
    "daytime TV",
    "multiculturalism",
    "midlife subcultures",
    "consumerist fetishism",
    "the Military-Industrial Complex",
    "the tyranny of ageing",
    "counter-terrorism",
    "gender politics",
    "new class identities",
    "recycling culture",
    "vegetarian ethics",
    "emotional memories",
    "emerging sexualities",
    "UFO sightings",
    "consumerist fetishism",
    "football chants",
    "acquired synesthesia",
    "life as performance",
    "urban spaces",
    "romance tourism"
]

def generate_art_critique():
    concept1, concept2 = random.sample(concepts, 2)
    return "This piece is about the relationship between %s and %s" % (concept1, concept2)

def give_art_critiques():
    for i in range(5):
        art_piece = Anastasis.vision.search("art piece")
        Anastasis.movement.turn_towards(art_piece)
        Anastasis.movement.start_walking()
        time.sleep(5)
        Anastasis.movement.stop_walking()
        critique = generate_art_critique()
        Anastasis.voice.say(critique)

if __name__ == '__main__':
    give_art_critiques()

