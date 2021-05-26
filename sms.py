import requests

number = input('Enter phone number: ')
message = input('Enter Message: ')

payload = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/text", data=payload)
if r.json()['success']:
    print('Success!')
else:
    print('Error!')