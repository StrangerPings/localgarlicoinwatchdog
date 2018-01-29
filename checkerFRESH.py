#
# Adapted by analogorange for freshgarlicblocks.net
#
# Visit my project - Check you Garlicoin balance from anywhere: http://35.196.19.10/ or https://35.196.19.10/
#
# Donations: GemPKNS9zP4K9d7Qbc2HjTTDHYubnfMSKi
#
# Attribution 4.0 International (CC BY 4.0)
#
from urllib.request import urlopen, Request
import json
import codecs
import time
import emails # 'pip install emails' before using

message = emails.html(html="TEXT",
                       subject="ALERT",
                       mail_from=('NAME', 'me@gmail.com'))

def checkhashrate():
    reader = codecs.getreader("utf-8")

    req = Request('https://www.freshgarlicblocks.net/api/workerinfo/YOURWALLET',
    headers={'User-Agent': 'Mozilla/5.0'})
    jsonurl = urlopen(req).read()
    obj = json.loads(jsonurl.decode('utf-8'))
    hashrate = float(obj["hashrate"])
    return hashrate;

def run():
    myhash = checkhashrate() #don't touch
    mails = 0 #don't touch
    minhash = 70000 #Set minimum hashrate
    print(str(myhash/1000) + " kH/s")

    while True:
        if myhash > minhash:
            myhash = checkhashrate()
            print(str(myhash/1000) + " kH/s")
            time.sleep(15) #Timer in seconds
            print('\033[H\033[J') #Comment this if you want to see your hashrate history
            mails = 0
            print('Press ctrl+z or cmd+z to stop')
        elif myhash < minhash:
            if mails == 1:
                return True
            else:
                mails += 1
                r = message.send(to='me@gmail.com', smtp={'host': 'aspmx.l.google.com', 'timeout': 5})
                print(r.status_code)
                return True


run()
