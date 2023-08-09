import requests

token = '6448285772:AAE97hJYCGYpBuGQTa1MSGBVQxeRetvZXns'
chat_id = '-989205590'
text = 'Test_2'

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })

sendTelegram()