import ast
from sklearn.cluster import KMeans
import numpy as np

def loadClusters():
	clusters=[]
	fo = open('actionRecognition/Clusters.txt', 'a+')
	data = fo.readlines()
	for cluster in data:
		cluster.strip()
		clusters.append(ast.literal_eval(cluster))
	fo.close()
	return clusters

def createPostureLabel(clusters, Posturefeature):
	try:
		X = np.array(clusters)
		kmeans = KMeans(n_clusters=len(clusters), random_state=0).fit(X)
		Posturefeature2D = np.array([ Posturefeature ])
		nsamples, nx, ny = Posturefeature2D.shape
		Posturefeature2D = Posturefeature2D.reshape((nsamples, nx*ny)).tolist()[0]	
		postureLabel = kmeans.predict([Posturefeature2D]).tolist()[0]
	except:
		postureLabel=-1
	# print("labels")
	# print(kmeans.labels_.tolist())
	return postureLabel

def createActivitySequence(activitySequence, postureLabel):
	print 'activitySequence: ', activitySequence
	if postureLabel !=-1:
		if len(activitySequence)==0:
			sequence =[formatLabel(postureLabel)]
		elif len(activitySequence)<5 and formatLabel(postureLabel)!=activitySequence[len(activitySequence)-1]:
			sequence = activitySequence + [formatLabel(postureLabel)]
		elif len(activitySequence)==5:
			sequence=[]
		else:
			sequence = activitySequence
	else:
		sequence = activitySequence
	return sequence

def createWordForActivity(activitySequence):
	return ''.join(activitySequence)

def saveWords(wordForActivity, activity):
	fo = open('actionRecognition/ActivitiesWords.txt', 'a+')
	d = { wordForActivity:activity }
	print 'Activity word to save',d
	fo.write(str(d)+'\n')
	fo.close()

def formatLabel(postureLabel):
	return str(unichr(postureLabel+97))
