import pandas
import matplotlib
import sklearn
import numpy
import json


def parse(filename):
	path = "../Data/" + filename
	with open(path) as f:
		data = json.load(f)
	return data
def analysis(json_data):
	chat_members = []
	json_people = json_data["participants"]
	json_messages = json_data["messages"]
	for p in json_people:
		chat_members.append(p["name"])
	
	json_messages.reverse()
	sender = json_messages[0]['sender_name']
	length_of_message = 0
	total_message =''
	response = ''
	data_justin_to_reda = {'ID':[],'message_length':[],'response':[]}
	ID = 0
	for message in json_messages:
		if 'content' in message:
			if(sender == 'Reda Ali' and "Justin Chen" == message['sender_name']):
				data_justin_to_reda['ID'].append(ID)
				data_justin_to_reda['message_length'].append(length_of_message)
				data_justin_to_reda['response'].append(response)
				ID += 1
				length_of_message = 0
				response = ''
				sender = "Justin Chen"
			if message['sender_name'] == "Reda Ali":
				response += message['content']
				sender = "Reda Ali"	
			if message['sender_name'] == "Justin Chen":
				length_of_message += len(message['content'])


	dataframe = pandas.DataFrame(data = data_justin_to_reda)
	while True:
		justin_input = input("Justin Chen: ")
		for index,message in dataframe.iterrows():
			if(message['message_length'] == len(justin_input)):
				print(message['response'])
				break
		if justin_input == "end":
			break
	
def main():
	filename = "redaali.json"
	db = parse(filename)
	analysis(db)

	
main()
