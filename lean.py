
from chat_downloader import ChatDownloader
import json

res = []
url = f'https://www.youtube.com/watch?v=KpSLiHAYe7k'
try:
    chats = ChatDownloader().get_chat(url)
except:
    chats = []

for chat in chats:
    author = chat['author']['name']
    
    obj = {
        'author': author,
        'message': chat['message'],
        'chat_timestamp': chat['time_in_seconds']
    }
    res.append(obj)
print('success')
with open('heartchallenger_chats.json', 'w') as f:
    json.dump(res, f, indent=4)






# Mori Calliope Ch. hololive-EN