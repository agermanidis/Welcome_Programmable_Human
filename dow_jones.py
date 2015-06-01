from humans import Anastasis
import csv, datetime

def visualize_dow_jones():
    Anastasis.voice.say("Human Action Code is also useful in corporate settings")
    Anastasis.voice.say("It can be used, for example, for doing data visualization for Fortune 500 companies")
    Anastasis.voice.say("Here I'll show you, I'll visualize the Dow Jones Industrial Average for this week!")

    with open('data/DJIA.csv', 'rb') as csvfile:
        dow_reader = csv.reader(csvfile)
        prev_market_average = None

        for index, row in enumerate(dow_reader):
            if index == 0: continue

            year, month, day = map(float, row[0].split("-"))
            market_average = float(row[1])

            dt = datetime.datetime(year=int(year), month=int(month), day=int(day))
            day_of_week = dt.strftime("%A")
            Anastasis.voice.say("Last %s the stock market was like" % day_of_week)

            if market_average > prev_market_average:
                Anastasis.face.smile()
                Anastasis.body.jump()

            else:
                Anastasis.face.frown()
                Anastasis.body.lie_down_fetal_position()

            prev_market_average = market_average

if __name__ == '__main__':
    visualize_dow_jones()
