import sys
sys.path.append('/home/struan/python/karelia/')

import requests
import time
import karelia

bot = karelia.newBot('0 Words', 'xkcd')
bot.stockResponses['shortHelp'] = "Pouncy's wordcount!"
bot.stockResponses['longHelp'] = "I display Pouncy's wordcount as they progress through NaNoWriMo, a challenge where they attempt to write a fifty-thousand word novel in thirty days! This year, they're writing Upon Ephemeral Winds, a story about friendship, adversity, and the way relationships change to mirror the people in them.\n\nI get information from the NaNoWriMo API, and update every minute. I respond to the usual commands."
bot.connect()

won = False
lastTime = time.time()

while True:
    try:
        bot.parse()

        response = requests.get(
            "http://nanowrimo.org/wordcount_api/wc/struan_dw")
        response = response.text.split('<user_wordcount>')[1]
        response = response.split('</user_wordcount>')[0]

        bot.changeNick("{} Words".format(response))

        if int(response) >= 50000 and not won:
            bot.send(
                ":tada::balloon:@PouncySilverkitten:black_nib::scroll: has made it to 50,000 words!")
            won = True
    except:
        bot.connect()
