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

def createActivitySequence(clusters, Posturefeature):
	try:
		X = np.array(clusters)
		kmeans = KMeans(n_clusters=len(clusters), random_state=0).fit(X)
		Posturefeature2D = np.array([ Posturefeature ])
		print 'Posturefeature2D 1:\n',Posturefeature2D
		nsamples, nx, ny = Posturefeature2D.shape
		Posturefeature2D = Posturefeature2D.reshape((nsamples, nx*ny)).tolist()[0]	
		postureLabel = kmeans.predict([Posturefeature2D]).tolist()[0]
	except:
		postureLabel=-1
	# print("labels")
	# print(kmeans.labels_.tolist())
	# print("centers")
	# print(kmeans.cluster_centers_.tolist())
	# print("verification of center labels")
	# print(kmeans.predict(kmeans.cluster_centers_).tolist())
	return postureLabel


# createActivitySequence(loadClusters(), [[-0.009005660612280015, -1.8705235122661397], [-0.04563693655945724, -0.998958092224828], [1.1430441925446853, 0.6327943850946958], [-1.2159814718985813, 0.4932803845028426], [1.2924588710434584, 1.5129025026361729], [-1.0244124795520126, 1.222698061324344], [0.5990121106562336, 3.593948226694114], [-0.5377174131316365, 3.6293186299806006], [0.6880202229902418, 4.9371415710844095], [-0.6293457509324764, 5.002503521509857]] )