import requests
from .models import TeleSettings

token = '6448285772:AAE97hJYCGYpBuGQTa1MSGBVQxeRetvZXns'
chat_id = '-989205590'
text = 'Test_2'

def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        if text.find('{') and text.find('{') and text.rfind('{') and text.rfind('}'):
            part1 = text[0:text.find('{')]
            part2 = text[text.find('}')+1:text.rfind('{')]
            part3 = text[text.rfind('}'):-1]

            text_slise = part1 + tg_name + part2 + tg_phone + part3
        else:
            text_slise = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
            })
        except:
            pass

        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:\
                print('Ошибка 500')
            else:
                print("Сообщение отправлено!")
    else:
        pass