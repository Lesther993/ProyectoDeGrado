import ast
import difflib
# from difflib import get_close_matches


def loadWords():
	dicOfWords={}
	wordsArray=[]
	fo = open('actionRecognition/ActivitiesWords.txt', 'a+')
	data = fo.readlines()
	for word in data:
		word.strip()
		word = ast.literal_eval(word)
		dicOfWords[word.keys()[0]] = word.values()[0]
	return dicOfWords

def getActivity(dicOfWords, word):
	closestWord = difflib.get_close_matches(word, dicOfWords.keys(),1)
	if len(closestWord)>0:
		activity = dicOfWords[closestWord[0]]
	else:
		activity = 'Unknown'
	return activity
