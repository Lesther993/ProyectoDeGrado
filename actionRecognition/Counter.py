import ast


def ActivityCounter(activity, activitySequence, postureLabel, _counter):
	counter = _counter
	print "counter:", counter
	if postureLabel !=-1 and formatLabel(postureLabel)==postureToDetect(activity):
		if len(activitySequence)==0:
			counter+=1
		elif formatLabel(postureLabel)!=activitySequence[len(activitySequence)-1]:
			counter+=1
	return counter


def saveActivityCounterData(counter,activity):
	fo = open('actionRecognition/' + activity.title().replace(" ","") +'ActivityHistory.txt', 'r')
	data = fo.readlines()
	_activityHistory = data[0]
	_activityHistory.strip()
	activityHistory = ast.literal_eval(_activityHistory)
	activityHistory['repetitions'].append(counter)
	if len(activityHistory['days'])==0:
		activityHistory['days'].append(1)
	else:
		activityHistory['days'].append( activityHistory['days'][len(activityHistory['days'])-1]+1 )
	print activityHistory
	fo.close()

	fo = open('actionRecognition/' + activity.title().replace(" ","") + 'ActivityHistory.txt', 'w+')
	fo.write(str(activityHistory)+'\n')
	fo.close()


# saveActivityCounterData(34,"Jumping")



def formatLabel(postureLabel):
	return str(unichr(postureLabel+97))

def postureToDetect(activity):
	switcher ={
		"Waving Right Hand":"g",
		"Waving Left Hand":"a"
		# "Jumping":"m",
		# "Jumping Jax":"b",
		# "Squats":"g"
	}
	return switcher.get(activity,"Unknown")

# print postureToDetect("Jumping Jax")