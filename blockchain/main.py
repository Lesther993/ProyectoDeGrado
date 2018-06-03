import uploadToBlockchain
import environment
import ast

environment.address_from = input("Address: ")
environment.privateKey = input("Private key: ")

saveClusters = ast.literal_eval(input("Save Clusters on Blockchain?: "))

if saveClusters:
	uploadToBlockchain.saveClusters()
else:
	saveWords = ast.literal_eval(input("Save Words for Activities on Blockchain?: "))

if saveWords:
	uploadToBlockchain.saveWords()


# import requests
# import json

# r = requests.post("http://localhost:4200/action-recognition/loadWords")

# y =json.loads(r.content)[u'data'].values()[0]
# word = {}
# for _word in y:
# 	word[str(_word[u'word'])] = str(_word[u'name'])
# print word

