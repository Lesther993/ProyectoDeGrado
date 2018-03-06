import pykinect
from pykinect import nui
from pykinect.nui import JointId
from TorsoCalcutatorModule import calculateTorso
from PostureFeatureExtration import jointsDetection, jointsNormalization

skeleton_to_depth_image = nui.SkeletonEngine.skeleton_to_depth_image


training = True

def actionRecognition(skeletons, dispInfo):
	skeleton = skeletons[0]
		
	joints = jointsDetection(skeleton, dispInfo)

	jointsNormalized = jointsNormalization(joints)
	print 'Joints normalized'
	print jointsNormalized

	if training:
		pass