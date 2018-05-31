


def count(activity, activitySequence, postureLabel, _counter):
	counter = _counter
	if postureLabel !=-1:
		if len(activitySequence)==0 and formatLabel(postureLabel)==postureToDetect(activity):
			counter+=1
		elif formatLabel(postureLabel)!=activitySequence[len(activitySequence)-1] and formatLabel(postureLabel)==postureToDetect(activity):
			counter+=1
	return counter






def formatLabel(postureLabel):
	return str(unichr(postureLabel+97))

def postureToDetect(activity):
	switcher ={
		"Jumping":"m",
		"Jumping Jax":"b",
		"Squats":"g"
	}
	return switcher.get(activity,"Unknown")