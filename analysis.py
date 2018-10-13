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
	
def main():
	filename = "redaali.json"
	db = parse(filename)
	analysis(db)

	
main()
