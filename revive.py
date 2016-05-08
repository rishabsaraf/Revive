import os
import sys
import re
from os.path import isfile, join

def get_filenames(directory=None):
	"""
	Gets the list of filenames present in the directory.
	@param directory: the directory whose files are to be found.
	                  If none is specified, it will look into the current working directory.
	@return filenames: list of all the filenames in the directory.
	"""
	filenames = []
	if not directory:
		print('No directory specified.')
		directory = os.getcwd()
		print('Using ' + directory + ' as the working directory.')

	if not os.path.exists(directory):
		print('The path does not exist.')
	else:
		filenames = [name for name in os.listdir(directory) if isfile(join(directory, name))]

	return filenames

def remove_sysfiles(filesList):
	"""
	Removes the system files from a lists for files.
	@param filesList: list of files
	@return newFilesList: list of files with system files removed.
	"""
	newFilesList = []
	for filename in filesList:
		if filename[0] != '.':
			newFilesList.append(filename)
	return newFilesList

def clean_string(string):
	"""
	Removes all the non alphanumeric characters from the file name.
	@param string: the string to be cleaned
	@return cleanedString: string containing only alphanumeric characters.
	"""
	return re.sub('[^0-9a-zA-z]+','',string)

def get_season_and_episode_number(filename):
	"""
	Gets the season and episode number from the filename.
	@param filename: the name of the file
	@return (season,episode): a tuple of season and episode number
	"""
	match = re.search('(s|S)(\d+)(e|E)(\d+)',filename)
	season = ''
	episode = ''
	if match:
		season = match.group(2)
		episode = match.group(4)


	return (season,episode)

if __name__ == '__main__':
	directory = raw_input("Enter the directory: ")
	a = get_filenames(directory)
	a = remove_sysfiles(a)
	print(a)
