import pykinect
from pykinect import nui
from pykinect.nui import JointId
from TorsoCalcutatorModule import calculateTorso
import settings
import PostureFeatureExtration
import PostureSelection
import ActivityFeatureComputation
import Classification

skeleton_to_depth_image = nui.SkeletonEngine.skeleton_to_depth_image

training = settings.training
creatingClusters = settings.creatingClusters
creatingActivitySequence = settings.creatingActivitySequence
numberOfClubsters = settings.numberOfClubsters
activityFile = settings.activityFile
activity = settings.activity

activitySequence =[]

#LOAD CLOSTERS
if training and creatingActivitySequence:
	clusters = ActivityFeatureComputation.loadClusters()
	print 'clusters: \n', clusters



# ActivityFeatureComputation.createPostureLabel(clusters, [[-0.009005660612280015, -1.8705235122661397], [-0.04563693655945724, -0.998958092224828], [1.1430441925446853, 0.6327943850946958], [-1.2159814718985813, 0.4932803845028426], [1.2924588710434584, 1.5129025026361729], [-1.0244124795520126, 1.222698061324344], [0.5990121106562336, 3.593948226694114], [-0.5377174131316365, 3.6293186299806006], [0.6880202229902418, 4.9371415710844095], [-0.6293457509324764, 5.002503521509857]] )

def actionRecognition(skeletons, dispInfo):
	skeleton = skeletons[0]
	#ARRAY OF JOINTS COORDINATES
	s = PostureFeatureExtration.jointsDetection(skeleton, dispInfo)
	#ARRAY OF JOINTS NORMALIZED. POSTURE VECTOR
	f = PostureFeatureExtration.jointsNormalization(s)
	# print 'Joints normalized: \n', f
	if training and not creatingClusters and not creatingActivitySequence: #SAVE TRAINING DATA

		if len(f)>0:
			PostureFeatureExtration.saveTrainingData(f, activityFile)
	#CREATE ACTIVITY SEQUENCE
	elif training and creatingActivitySequence:
		postureLabel = ActivityFeatureComputation.createPostureLabel(clusters, f)
		global activitySequence
		activitySequence = ActivityFeatureComputation.createActivitySequence(activitySequence,postureLabel,numberOfClubsters)
		if len(activitySequence)==numberOfClubsters:
			# print 'Activity Sequence', activitySequence
			wordForActivity = ActivityFeatureComputation.createWordForActivity(activitySequence)
			print 'Word for activity: ',wordForActivity
			ActivityFeatureComputation.saveWords(wordForActivity, activity)
	# DETECT ACTIVITY. FINAL FASE
	elif not training:
		postureLabel = ActivityFeatureComputation.createPostureLabel(clusters, f)
		global activitySequence
		activitySequence = ActivityFeatureComputation.createActivitySequence(activitySequence,postureLabel,numberOfClubsters)
		if len(activitySequence)==numberOfClubsters:
			wordForActivity = ActivityFeatureComputation.createWordForActivity(activitySequence)
			print 'Word for activity: ', wordForActivity
			words = Classification.loadWords()
			activityDetected = Classification.getActivity(words, wordForActivity)
			print 'ACTIVITY DETECTED: ', activityDetected



#CREATE CLUSTERS OF AN ACTIVITY
if training and creatingClusters:
	activityVector = PostureSelection.loadTrainingData(activityFile)
	PostureSelection.createClusters(activityVector, numberOfClubsters)