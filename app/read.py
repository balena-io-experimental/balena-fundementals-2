# python imports
import psutil
import os 
import time
# import sqlchemy
from init import db, Reading

# read environment variables + set defaults
interval = os.getenv('INTERVAL', '20');

def log():
	cpu = psutil.cpu_percent()
	newLog = Reading(value=cpu)
	db.session.add(newLog)
	db.session.commit()
	print "CPU: " + str(cpu)
	print str(count_logs()) + " readings have been recorded"

def count_logs():
	return db.session.query(Reading).count()
	
while True:
    log()
    time.sleep(int(interval))
