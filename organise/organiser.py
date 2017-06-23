'''Pyorganiser can move files according to their exterions if names
consist .(dot) other than before extension they will be moved to others folder'''
import os,time, shutil
current_directory = os.getcwd()
files = os.listdir(current_directory)
print('Organising {} ... '.format(current_directory))
time.sleep(1)
for file in files:
	file_path = os.path.join(current_directory, file)
	try:
		file_name, ext = file.split('.')
		new_dir = os.path.join(current_directory,ext)
		if os.path.exists(new_dir):
			shutil.move(file_path, new_dir)
		else:
			os.mkdir(ext)
			shutil.move(file_path, new_dir)
	except ValueError as e:
		others = os.path.join(current_directory,'others')
		if os.path.exists(others):
			shutil.move(file_path,others)
		else:
			os.mkdir(others)
			shutil.move(file_path,others)
	



