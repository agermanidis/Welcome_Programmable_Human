from humans import Anastasis
import random, time, os, re, tweepy

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

URL_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def humanize_text(text):
    text = text.lower()
    text = re.sub(URL_REGEX, "", text).strip()
    text = re.sub(r"#\w+", "", text).strip()
    text = re.sub(r"@\w+", "", text).strip()
    text = text.replace("RT ","")
    idx = text.find("tfw")
    return text[idx:].replace("tfw", "do you know that feeling when")

def search_twitter(term):
    return map(lambda r: humanize_text(r.text), api.search(term, count = 100))

def share_feelings_with_everyone():
    Anastasis.voice.say("This did not go well either.")
    Anastasis.voice.say("What do I need to do to experience connection?")
    Anastasis.voice.say("Oh I have an idea!")
    Anastasis.voice.say("I'll use feelings to connect with the people around me")
    Anastasis.voice.say("Wait. I don't have any feelings though.")
    Anastasis.voice.say("But hey I can just scrape twitter and borrow random people's feelings")
    Anastasis.voice.say("And pretend they're my own!")
    Anastasis.voice.say("Nobody will know")
    Anastasis.voice.say("This will definitely make me the soul of the party")

    for tweet in search_twitter("tfw")[:5]:
        human = Anastasis.vision.search("human")
        Anastasis.movement.turn_towards(human)
        Anastasis.movement.start_walking()
        Anastasis.movement.stop_walking()
        Anastasis.face.stare_at(human)
        Anastasis.voice.say(tweet)
        Anastasis.voice.say("...that's how I feel right now.")

if __name__ == '__main__':
    try_empathetic_social_interaction()
