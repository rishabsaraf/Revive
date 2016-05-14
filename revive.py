import os
import sys
import re
from os.path import isfile, join

FILE_NAME_PATTERN = "S%SE%E"

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


def update_name_pattern(namePattern):
	"""
	Sets the name pattern to the default pattern if it is empty.
	@param namePattern: the file name pattern
	@return namePattern: the updated file name pattern
	"""
	if not namePattern:
		namePattern = FILE_NAME_PATTERN
	return namePattern


def get_new_name(filename, namePattern):
	"""
	Gets the new name for a filename based on a pattern.
	@param filename: the current file name.
	@param namePattern: the name pattern according to which the new file name is to be returned.
	@return newFilename: new name for the file.
	"""
	(baseName, extension) = os.path.splitext(filename)
	(season, episode) = get_season_and_episode_number(filename)
	if not season or not episode:
		newFilename = baseName
	else:
		newFilename = get_filename_from_pattern(namePattern, season, episode)
	newFilename = newFilename + extension
	return newFilename


def get_filename_from_pattern(namePattern, season, episode):
	"""
	Gets the filename from the name pattern by replacing the pattern with season and episode at relevant places.
	@param season: the season number as string
	@param episode: the episode number as string
	@return filename: the name generated from the pattern, season and episode
	"""
	name = namePattern.replace("%s", season)
	name = name.replace("%S", season)
	name = name.replace("%e", episode)
	name = name.replace("%E", episode)
	return name


def update_filenames(directory, filesList, namePattern):
	"""
	Updates all the file names present in the filesList according to the namePattern.
	@param directory: the directory path of all the files present in the filesList
	@param filesList: the list of files whose names are to be updated.
	@param namePattern: the namePattern according to which the new filenames are to be generated.
	"""
	for filename in filesList:
		newFilename = get_new_name(filename, namePattern)
		os.rename(os.path.join(directory,filename),os.path.join(directory,newFilename))


if __name__ == '__main__':
	directory = raw_input("Enter the directory: ")
	filesList = get_filenames(directory)
	filesList = remove_sysfiles(filesList)
	namePattern = raw_input("Enter the file name pattern: ")
	update_filenames(directory, filesList, namePattern)
