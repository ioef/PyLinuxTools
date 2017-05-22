#!/usr/bin/env python

#find all activities related to usb devices in the system
with open("/var/log/messages", "r") as f:	
	for line in f:
		if "usb" in line:
			print line.strip()
