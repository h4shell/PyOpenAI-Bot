from pyai import ai
import requests
from creds import *


lock = True
mxid = []


def send_to_telegram(to, message):
    if to == False:
        to = conf['chat_id']
    else:
        pass
    message = str(message)
    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "content-type": "application/json"
    }

    payload = {'chat_id': to,
               'parse_mode': 'Markdown',
               'text': message,
               "disable_web_page_preview": True,
               }
    apiURL = f'https://api.telegram.org/bot{conf["token_id"]}/sendMessage'
    response = requests.post(apiURL, json=payload, headers=headers).json()

    return response


def inbox():
    url = f'https://api.telegram.org/bot{conf["token_id"]}/getUpdates'
    payload = {
        "offset": -1,
        "limit": 100,
        "timeout": 10
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(
        url, json=payload, headers=headers).json()["result"]

    try:

        for i in response:
            if str(i['message']['message_id']) in mxid:
                pass
            else:
                mxid.append(str(i['message']['message_id']))

                inbox = {'FROM': i['message']['from']['username'],
                         'ID_FROM': i['message']['from']['id'],
                         'TEXT': i['message']['text']
                         }
                print(i['message']['from']['username'])
                if i['message']['from']['username'] != conf["username"]:
                    pass
                else:
                    return inbox

                # print("" + str(i['message']['message_id']))
                # response = []
                # mxid.append(str(i['message']['message_id']))
                # print(mxid)
    except:
        pass


if __name__ == '__main__':

    while True:
        try:
            ris = inbox()
            if ris == None:
                pass
            else:
                print(ris)
            if ris == None:
                pass
            else:
                if lock == True:
                    lock = False
                    pass
                else:
                    x = ai(ris['TEXT'])
                    print(x)
                    send_to_telegram(ris['ID_FROM'], str(x))
        except:
            pass
