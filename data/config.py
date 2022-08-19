import os

# without docker
from dotenv import load_dotenv
# without docker
load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admins = []

ip = os.getenv('IP')

aiogramRedis = {
    'host': ip
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}