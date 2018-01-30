#
# Made by analogorange for Bakery Pool
#
# Visit my project - Check you Garlicoin balance from anywhere: garli.top
#
# Donations: GemPKNS9zP4K9d7Qbc2HjTTDHYubnfMSKi
#
# Attribution 4.0 International (CC BY 4.0)
#
from urllib.request import urlopen, Request
import json, time, requests, codecs

botjson = Request('https://api.telegram.org/ TELEGRAMBOTKEY /getUpdates',headers={'User-Agent': 'Mozilla/5.0'})
readbotjson = urlopen(botjson).read()
botinfo = json.loads(readbotjson.decode('utf-8'))
chatid = botinfo["result"][0]["message"]["chat"]["id"]

def checkhashrate():
    reader = codecs.getreader("utf-8")

    req = Request('https://api.grlc-bakery.fun/v1/stats',
    headers={'User-Agent': 'Mozilla/5.0'})
    jsonurl = urlopen(req).read()
    obj = json.loads(jsonurl.decode('utf-8'))
    hashrate = int(obj["data"]["workers"]["ENTERYOURWALLET"]["hashrate"])
    return hashrate;

mails = 0 #don't touch

def run():
    global mails
    myhash = checkhashrate() #don't touch
    minhash = 70000 #Set minimum hashrate. To check notifications set to 999999999999

    while True:
        if myhash > minhash:
            myhash = checkhashrate()
            print(str(myhash/1000) + " kH/s")
            time.sleep(15) #Timer in seconds
            print('\033[H\033[J') #Comment this if you want to see your hashrate history
            mails = 0
            print('Press ctrl+z or cmd+z to stop. Your chat id: %s' % chatid)
        elif myhash < minhash:
            if mails == 1:
                run()
            else:
                mails += 1
                requests.get('https://api.telegram.org/ TELEGRAMBOTKEY /sendMessage?chat_id= YOURCHATID &text=YOURWANINGMESSAGE')
                run()


def sendhashrate():
    while True:
        rawkhs = checkhashrate()
        khs = str(myhash/1000) + " kH/s"
        sendkhs = 'https://api.telegram.org/ TELEGRAMBOTKEY /sendMessage?chat_id= YOURCHATID &text=%s' % khs
        requests.get(sendkhs)
        time.sleep(600) #Send your hashrate to you each 10 minutes
                
run()
sendhashrate() #comment this if you dont want to get notifications about your hashrate
