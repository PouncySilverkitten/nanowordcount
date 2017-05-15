import requests
import time
import karelia

bot = karelia.newBot('0','test')
bot.stockResponses['shortHelp'] = "Pouncy's wordcount!"
bot.stockResponses['longHelp'] = "I display Pouncy's wordcount as they progress through NaNoWriMo, a challenge where they attempt to write a fifty-thousand word novel in thirty days! This year, they're writing a sci-fi novel set on Mars. To make humanity a multi-planet species, two things were needed - private companies to build towns, and civilian to live. Now, one will withdraw, leaving the other stranded...\n\nI get information from the NaNoWriMo API, and update every minute. I respond to the usual commands."
bot.connect()
print("Connected")

won = False
lastTime = time.time()

while True:
    print(bot.parse())
    
    
    if lastTime < time.time()-60:
        lastTime = time.time()
    
        response = requests.get("http://nanowrimo.org/wordcount_api/wc/struan_dw")
        response = response.text.split('<user_wordcount>')[1]
        response = response.split('</user_wordcount>')[0]
        bot.changeNick(response)
        
        if int(response) >= 50000 and not won:
            bot.send(":tada::balloon:Congratulations, @PouncySilverkitten!:black_nib::scroll:")
            won = True
