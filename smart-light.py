'''
This script tests out a simple on-line learning technique for 
finding the threshold in a linear range for binary classification.
The goal is to have the output varible activate for inputs greater 
than the real threshold and vis-versa.
'''

import random

# real threshold (human trigger)
realThresh = 250
# learnt threshold
sysThresh = 0
# output
on = False
wrongs= 0

for i in range(100):
	curr = random.randint(1, 1000)
	on = curr > sysThresh
	print curr,on
	if (not on and curr > realThresh) or (on and curr < realThresh):
		# when the system fails to activate after passing the real threshold
		# OR when the system activates before passing the real threshold
		print sysThresh,'->',curr
		sysThresh = curr
		wrongs += 1

print 'System threshold:',sysThresh,'| adjusted system threshold',wrongs,'times'