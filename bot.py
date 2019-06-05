from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests, parser

def get_url(): 
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']    
	return url

def bop(bot, update):   
	url = get_url()    
	chat_id = update.message.chat_id    
	bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('889963111:AAHXMTO5nxtakWAh_14IqdPQnlGxCuVHKdc')    
    dp = updater.dispatcher    
    dp.add_handler(CommandHandler('bop',bop))    
    updater.start_polling()    
    updater.idle()

if __name__ == '__main__':    
	main()

