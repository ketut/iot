import time

f = open("trigger.txt","w")
seconds = 1545925769.9618232
f.write(time.ctime(seconds))
f.close()
