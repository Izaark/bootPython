def typing_message(recipient_id):
	message_data ={
		'recipient':{'id':recipient_id},
		'sender_action':'typing_on'
	}
	return message_data

def text_message(recipient_id,message_text):
	message_data = {
	'recipient':{'id':recipient_id},
	'message':{'text':message_text}
	}
	return message_data
