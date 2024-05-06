
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities
def printMaxActivities(s, f ):
 n = len(f)
 print ("The following activities are selected")
 # The first activity is always selected
 i = 0
 print (i),
 # Consider rest of the activities
 for j in range(n):
    if s[j] >= f[i]:
        print (j),
        i = j
