import os

# without docker
from dotenv import load_dotenv

# without docker
load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admins = [
    941953049
]

ip = os.getenv('IP')

aiogram_redis = {
    'host': ip
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
