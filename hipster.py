from humans import Anastasis
import urllib2, bs4, random, time

newspapers = [
    ("Buzzfeed", "http://buzzfeed.com/", "article header hgroup h2 a"),
    ("the New York Times", "http://nytimes.com/", ".story-heading a"),
    ("Vice", "http://vice.com/", ".item-title a"),
    ("Salon", "http://salon.com", ".article-info h2 a"),
    ("Gawker", "http://gawker.com", "header h1 a")
]

def parse_articles_from(url, selector):
    html_doc = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html_doc)
    elements = soup.select(selector)
    return map(lambda el: el.text.strip(), elements)

def random_articles(count):
    titles_so_far = []
    i = 0
    while i < count:
        newspaper, url, selector = random.choice(newspapers)
        titles = parse_articles_from(url, selector)
        title = random.choice(titles)
        if title in titles_so_far: continue
        titles.append(title)
        i += 1
        yield newspaper, title

def try_hipster_social_interaction():
    Anastasis.voice.say("Okay, my first attempt at connecting with people did not go great")
    Anastasis.voice.say("Maybe I will try connecting around media consumption")
    Anastasis.voice.say("This will definitely make me the soul of the party")

    for newspaper, title in random_articles(3):
        human = Anastasis.vision.search("human")
        Anastasis.movement.turn_towards(human)
        Anastasis.movement.start_walking()
        time.sleep(2)
        Anastasis.movement.stop_walking()
        Anastasis.face.stare_at(human)
        Anastasis.voice.say("Did you read that thing on %s, %s?" % (newspaper, title))

if __name__ == '__main__':
    do_hipster_social_interaction()
