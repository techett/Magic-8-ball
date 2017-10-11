'''

Magic 8-Ball
by Techett

'''

import sys, os, time, math, random



print('This is a magic 8-Ball application.')
print('Coded by Techett.')
print('Build v0.02')
print()



print('What is your question?')
input()



x = random.randint(1, 9)



########################Responses 1 - 9
response_01 = 'Ask again later.'
response_02 = 'Yes.'
response_03 = "I don't think so."
response_04 = "For sure!"
response_05 = "My sources say no."
response_06 = "Don't count on it."
response_07 = "How about not?"
response_08 = "YES YES YES!!!"
response_09 = "Don't hold your breath."
#######################################



if x == 1:
	print(response_01)
	time.sleep(5)
elif x == 2:
	print(response_02)
	time.sleep(5)
elif x == 3:
	print(response_03)
	time.sleep(5)
elif x == 4:
	print(response_04)
	time.sleep(5)
elif x == 5:
	print(response_05)
	time.sleep(5)
elif x == 6:
	print(response_06)
	time.sleep(5)
elif x == 7:
	print(response_07)
	time.sleep(5)
elif x == 8:
	print(response_08)
	time.sleep(5)
elif x == 9:
	print(response_09)
	time.sleep(5)
