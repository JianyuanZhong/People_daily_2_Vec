# -*- coding: utf-8 -*-
import os
import subprocess

def print_stars(str):
	buff = "*********************************************************************************************************"
	
	print(buff)

	print("* {}".format(str))

	
	print(buff)


def replace(arr, line):	
	new_line = ''
	replace = False

	for word in line:
		for token in arr:
			if ord(word) == ord(token):
				replace = True
		if not replace:
			new_line += word
		replace = False

	new_line.replace('  ', ' ')

	return new_line




f_in  = open('segment_test.txt', 'r+')
f_out = open('data_text.txt', 'w+')

line = ''



while 1:
#for i in range(20):
	print_stars("Preparing data......")
	line = f_in.readline()
	line = replace(['，', ',', '[', ']', '（', '）', '、', '“', '”', '：', '《', '》', '《', '》', '/' , '【', '】', '(', ')', '>', '／'], line)
	print(line)
	f_out.write(line)

	if len(line) == 0:
		print_stars("Complete!")
		break


# for file in lsdir:
# 	print_stars("Tonkenizing %s" % file)
# 	cmd = "bash stanford-segmenter-2017-06-09/segment.sh pku {} utf-8 0 >> segment_test.txt".format(file)
# 	print(cmd)
# 	#os.popen(cmd)
# 	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	

# 	print_stars("Finished")


