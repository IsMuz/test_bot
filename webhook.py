from pprint import pprint
import requests

bot_token = '889963111:AAHXMTO5nxtakWAh_14IqdPQnlGxCuVHKdc'
test_url = "79c7eaf2.ngrok.io/{}".format(bot_token)

def get_url(method):
	return "https://api.telegram.org/bot{}/{}".format(bot_token, method)

r = requests.get(get_url("setWebhook"), data = {"url": test_url})
r = requests.get(get_url("getWebhookinfo"))
pprint(r.status_code)
pprint(r.json())