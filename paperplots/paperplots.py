import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation as scaledtf
import numpy as np
import csv
import pickle
import datetime
import socket
import os


# https://sashamaps.net/docs/tools/20-colors/
Colours = (
    '#800000',  # Maroon (99.99%)
    '#4363d8',  # Blue (99.99%)
    '#ffe119',  # Yellow (99.99%)
    '#e6beff',  # Lavender (99.99%)
    '#f58231',  # Orange (99.99%)
    '#3cb44b',  # Green (99%)
    '#000075',  # Navy (99.99%)
    '#e6194b',  # Red (99%)
    '#46f0f0',  # Cyan (99%)
    '#f032e6',  # Magenta (99%)
    '#9a6324',  # Brown (99%)
    '#008080',  # Teal (99%)
    '#911eb4',  # Purple (95%*)
    '#aaffc3',  # Mint (99%)
    '#ffd8b1',  # Apiroct (95%)
    '#bcf60c',  # Lime (95%)
    '#fabed4',  # Pink (99%)
    '#808000',  # Olive (95%)
    '#fffac8',  # Beige (99%)
    #'#a9a9a9',
    #'#ffffff',
    #'#000000'
)



def make_plot(data, colours=None):

	fig, ax = plt.subplots(figsize=(6, 4))
	ax.plot(data[1], data[0], label=data[4], color=colours[0], linewidth=2)

	ax.legend()
	# Adding labels and title
	ax.set_xlabel(data[3])
	ax.set_title(data[2])

	# Setting white background
	ax.set_facecolor('white')
	ax.grid()

	# Show the plot
	plt.show()


class Writer():
	"""
	Writes scalars as a pickle file within the given directory

	Args:
		logdir (str): name of the logging directory. Default: "runs/"
	"""
	def __init__(self, logdir=f'runs/{datetime.datetime.now()}_{socket.gethostname()}', run_name=None):
		self.chunk_size = 1000
		self.logdir = logdir
		if run_name != None:
			self.run_name = run_name
		else:
			self.run_name = 'recorded_data'

		# dicts with key as tag and value as a list of y,x entries
		# self.full_data has all the data in a numpy array while self.data only holds self.chunk_size samples
		self.full_data = {}
		self.data = {}

	def add_scalar(self, tag, scalar_value, global_step=None, ylabel=None, xlabel=None, name=None):
		""" Add a scalar value of a given tag, scalar value, and time series step """
		if not tag in list(self.data.keys()):
			self.data[tag] = [[], [], ylabel, xlabel]
			self.full_data[tag] = [np.array([]), np.array([]), ylabel, xlabel, name]

		self.data[tag][0].append(scalar_value)
		self.data[tag][1].append(global_step)

		self.update_full_data(tag)

	def update_full_data(self, tag):
		""" Update the full data dict with the currently stored chunk """
		if len(self.data[tag][0]) > self.chunk_size:
			# Add current chunk to full data
			self.full_data[tag][0] = np.concatenate((self.full_data[tag][0], np.array(self.data[tag][0])), axis=0)
			self.full_data[tag][1] = np.concatenate((self.full_data[tag][1], np.array(self.data[tag][1])), axis=0)

			self.data[tag] = [[], [], self.data[tag][2], self.data[tag][3], self.data[tag][4]]

	def close(self):
		""" Save the data stored in self.full_data as a pkl file """
		for tag in list(self.full_data.keys()):
			self.full_data[tag][0] = np.concatenate((self.full_data[tag][0], np.array(self.data[tag][0])), axis=0)
			self.full_data[tag][1] = np.concatenate((self.full_data[tag][1], np.array(self.data[tag][1])), axis=0)

		filepath = f'./{self.logdir}/{self.run_name}.pkl'
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		with open(filepath, 'wb') as handle:
			pickle.dump(self.full_data, handle, protocol=pickle.HIGHEST_PROTOCOL)



class Plotter():
	"""
	Writer class
	"""
	def __init__(self, logdir=f'runs/'):
		self.logdir = logdir
		self.colours = Colours


	def plot_run(self, run_name=None, run_path=None, tags=None):
		""" Plot a run either with the logdir/run_name or plot a run with the direct run path """
		assert (run_name==None and run_path!=None) or (run_name!=None and run_path==None), "Please provide either a run name or a run path. Not both!"

		if run_name != None:
			filepath = f'{self.logdir}/{run_name}.pkl'
		elif run_path != None:
			filepath = run_path
	
		with open(filepath, 'rb') as handle:
			data = pickle.load(handle)

		# If no tags are given, plot all the data
		if tags == None:
			tags = list(data.keys())

		for tag in tags:
			make_plot(data[tag], colours=self.colours)



	# def plot_experiment(self):

	# def compare_experiments(self):

