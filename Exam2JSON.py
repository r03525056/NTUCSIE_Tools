#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
fileContent = []

for line in open(sys.argv[1], 'r'):
	fileContent.append(line)

optionNum = 0
print '{'
print '\t\"problem\":['
continueCount = 0
isMock = 0
for i in xrange(len(fileContent)):
	if fileContent[i].find('公 務 人 員 特 種 考 試 司 法 官 考 試') != -1:
		optionNum = 0
		continueCount = 2
		isMock = 0
	elif fileContent[i].find('全真模擬') != -1:
		optionNum = 0
		continueCount = 6
		isMock = 1
	elif fileContent[i].find('單一選擇題') != -1:
		optionNum = 4
		if isMock:
			continueCount = 4
		else:	
			continueCount = 3
	elif fileContent[i].find('複選題') != -1:
		optionNum = 5
		continueCount = 3
	if continueCount > 0:
		continueCount = continueCount - 1
		continue
	
	print '\t\t{'
	print '\t\t\t\"problemNum\":\"%s\",' %(fileContent[i][0:fileContent[i].find(' ')])
	print '\t\t\t\"problemText\":\"%s\",' %(fileContent[i][fileContent[i].find(' ')+1:len(fileContent[i])-2])
	if optionNum == 4:
		print '\t\t\t\"AnswerNum\":\"one\",'
	else:
		print '\t\t\t\"AnswerNum\":\"more\",'
	print '\t\t\t\"A\":\"%s\",' %(fileContent[i+1][3:len(fileContent[i+1])-1])
	print '\t\t\t\"B\":\"%s\",' %(fileContent[i+2][3:len(fileContent[i+2])-1])
	print '\t\t\t\"C\":\"%s\",' %(fileContent[i+3][3:len(fileContent[i+3])-1])
	if optionNum == 4:
		print '\t\t\t\"D\":\"%s\"' %(fileContent[i+4][3:len(fileContent[i+4])-1])
	else:
		print '\t\t\t\"D\":\"%s\",' %(fileContent[i+4][3:len(fileContent[i+4])-1])
		print '\t\t\t\"E\":\"%s\"' %(fileContent[i+5][3:len(fileContent[i+5])-1])

	continueCount = optionNum + 1
	if (i + continueCount) < len(fileContent):
		print '\t\t},'
	else:
		print '\t\t}'
print '\t]'
print '}'