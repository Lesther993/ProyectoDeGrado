from TorsoCalcutatorModule import calculateTorso
import settings
import PostureFeatureExtration
import PostureSelection
import ActivityFeatureComputation
import Classification
import pygame

training = settings.training
creatingClusters = settings.creatingClusters
creatingActivitySequence = settings.creatingActivitySequence
numberOfClubsters = settings.numberOfClubsters
activity = settings.activity
activityFile = settings.activity.title().replace(" ","")





#CREATE CLUSTERS OF AN ACTIVITY
if training and creatingClusters:
	activityVector = PostureSelection.loadTrainingData(activityFile)
	PostureSelection.createClusters(activityVector, numberOfClubsters)


activitySequence =[]
#LOAD CLOSTERS
if (not training) or (training and creatingActivitySequence):
	clusters = ActivityFeatureComputation.loadClusters()
	# print 'clusters: \n', clusters


def actionRecognition(skeletons, dispInfo):
	skeleton = skeletons[0]
	#ARRAY OF JOINTS COORDINATES
	s = PostureFeatureExtration.jointsDetection(skeleton, dispInfo)
	#ARRAY OF JOINTS NORMALIZED. POSTURE VECTOR
	f = PostureFeatureExtration.jointsNormalization(s)
	# print 'Joints normalized: \n', f
	global activitySequence
	if training and not creatingClusters and not creatingActivitySequence: #SAVE TRAINING DATA

		if len(f)>0:
			PostureFeatureExtration.saveTrainingData(f, activityFile)
	#CREATE ACTIVITY SEQUENCE
	elif training and creatingActivitySequence:
		postureLabel = ActivityFeatureComputation.createPostureLabel(clusters, f)
		activitySequence = ActivityFeatureComputation.createActivitySequence(activitySequence, postureLabel, numberOfClubsters)
		if len(activitySequence)==numberOfClubsters:
			# print 'Activity Sequence', activitySequence
			wordForActivity = ActivityFeatureComputation.createWordForActivity(activitySequence)
			print 'Word for activity to save: ', wordForActivity
			ActivityFeatureComputation.saveWords(wordForActivity, activity)
	# DETECT ACTIVITY. FINAL FASE
	elif not training:
		postureLabel = ActivityFeatureComputation.createPostureLabel(clusters, f)
		activitySequence = ActivityFeatureComputation.createActivitySequence(activitySequence, postureLabel, numberOfClubsters)
		if len(activitySequence)==numberOfClubsters:
			wordForActivity = ActivityFeatureComputation.createWordForActivity(activitySequence)
			print 'Word for activity to compare: ', wordForActivity
			words = Classification.loadWords()
			global activityDetected
			activityDetected = Classification.getActivity(words, wordForActivity)
			settings.activityDetected = activityDetected