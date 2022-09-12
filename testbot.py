import requests as req

a = req.get('https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe')

token = "5541908250:AAF4jdKBL4lQ2i-2uOGvxLdCd8JGkRJoGcA"
root_url = "https://api.telegram.org/bot"

ok_codes = 200, 201, 202, 203, 204

def get_updates(token):
	url = f"{root_url}{token}/getUpdates"
	res = requests.get(url)
	if res.status_code in ok_codes:
		updates = res.json()
		#result = {"error": None, "data": updates}
		return updates


updates = get_updates(token)

if len(updates["result"]) > 0:
	last_message = updates["result"][-1]
	last_message_text = last_message["message"]["text"]
	chat_id = last_message["message"]["chat"]["id"]
	print(last_message_text)
else:
	print("No messages")


url = f"{root_url}{token}/sendMessage"
r = requests.post(url, data={'chat_id': chat_id, "text": last_message_text})
print(r)
