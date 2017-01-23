#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,json
from structs import typing_message,text_message

def recive_message(event,token):
	sender_id = event['sender']['id']
	recipient_id = event['recipient']['id']
	time_message = event['timestamp']
	message = event['message']
	text = message['text'] 
	print text

	typing = typing_message(sender_id)
	call_send_API(typing,token)

	user = call_userAPI(sender_id, token)
	firt_name = user['first_name']
	message = "Hola {}, como estas ?".format(firt_name)

	message = text_message(sender_id,message)
	call_send_API(message,token)


def call_send_API(data,token):
	res = requests.post('https://graph.facebook.com/v2.6/me/messages',
			params = {'access_token':token},
			data = json.dumps(data),
			headers={'Content-type':'application/json'}
		)
	if res.status_code ==200:
		print "El mensaje fue enviado exitosamente!!"

def call_userAPI(user_id,token):
	res = requests.get('https://graph.facebook.com/v2.6/' + user_id,
			params = {'access_token':token})
	data = json.loads(res.text)
	return data


