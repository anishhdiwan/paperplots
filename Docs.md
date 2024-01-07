# Documentation

## Writer
```
class Writer(logdir, run_name):
	"""Writes scalars as a pickle file within the given directory

	Args:
		logdir (str): name of the logging directory that houses runs. Default: "runs/recorded_data"
		run_name (str): Name of the run

	"""

function add_scalar(tag, scalar_value, global_step=None, ylabel=None, xlabel=None, name=None):
	""" Record a scalar value (could be loss, reward, accuracy, etc)
	Args:
		tag (str): a tag for this scalar. Metrics that need to be compared must have the same tag. 
		Ex: accuracies of algo1 and algo2 must have the same tag "accuracy" if they need to be compared 

		scalar_value (float): the value to be recorded
		global_step (float): the x-axis corresponding to the scalar value
		ylabel (str): y axis label for this data (ideally keep the same across runs)
		xlabel (str): x axis label for this data (ideally keep the same across runs)
		name (str): name of the data line in the plot. Example: "algorithm_1" or "Q-learning"

	"""

function close(self):
	""" Necessary to actually save the recorded data 
	"""
```

## Plotter
```
class Plotter():
	"""Plots runs or experiments

	Args:
		logdir (str): name of the logging directory that houses experiments. Default: "runs/"
		Note that unlike Writer(), logdir here houses all experiments not runs. 

	"""

function plot_run(self, run_name, tags=None, rolling_avg=False, window_size=None):
	""" Plot a run or compare multiple runs

	Args:
		run_name (str OR list(str)): name of the run to plot or a list of run names to plot. 
		Example: "algo1/run1" OR ["algo1/run1", "algo2/run4"]

		tags (list(str)): list of tags to plot. Default: None
		If not given, plot all tags

		rolling_avg (bool): whether or not to apply a rolling average

		window_size (int): rolling average window size. Default: 10% of run length

	"""

function plot_experiment(self, exp_name, tags=None, rolling_avg=False, window_size=None, plot_error=True):
	""" Plot the average scalar values in an experiment or compare multiple experiments 

	Args:
		exp_name (str OR list(str)): name of the experiment folder containing runs or a list of experiment folder names.  
		Example: "algo1" OR ["algo1", "algo2"]

		tags (list(str)): list of tags to plot. Default: None
		If not given, plot all tags

		rolling_avg (bool): whether or not to apply a rolling average
		window_size (int): rolling average window size. Default: 10% of run length
		plot_error (bool): whether or not to plot shaded error regions

	"""
```
