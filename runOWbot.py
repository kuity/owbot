import telepot
from pprint import pprint

bot = telepot.Bot('245618972:AAFfmcyfxHsrVC9aj4TUturkefkhP7Vz6zc')
#response = bot.getUpdates()

def handle(msg):
	pprint(msg)

bot.message_loop(handle)

