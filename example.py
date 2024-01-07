"""
Examples

Let's compare two algorithms (say DQN and DQfD)
-----------------------------------------------
1. We run one experiment with DQN and another with DQfD
2. Each experiment has 5 runs
3. Each run has 50 episodes

What we plan to record and plot
-------------------------------
While we can record this data and visualise it with TORCH.UTILS.TENSORBOARD (https://pytorch.org/docs/stable/tensorboard.html) 
it does not allow us to make pretty plots right away. This is where paperplots comes in

1. We plan to record the episode return and loss curves across all runs
2. Just to check how things look, we want to plot the losses from one of the runs of DQN
3. We also want to plot the average return vs num episodes and compare both algorithms


# NOTE: A run is a single run of an algorithm. An experiment is a set of runs usually with the same parameters
"""
# Importing random to get the values
import random
random.seed(0)
num_episodes = 50
num_runs = 5



from paperplots import Writer, Plotter

############################ WRITING DATA ############################

for algo in ["DQN", "DQfD"]:

	# Running an experiment and saving data
	for i_run in range(num_runs):
		
		# Instantiating the writer object similar to the writer from tensorboard
		# A writer is instantiated for every run to keep separate logs
		writer = Writer(logdir=f'runs/{algo}', run_name=f'run{i_run}')

		for i_episode in range(num_episodes):
			# We get some loss and episode return (here I've defined it based on the episode number to make it look nice)
			# Let's bias the results towards DQfD :)
			scaling = 1.0
			if algo == "DQfD":
				scaling = 1.5
			loss = num_episodes - i_episode + random.uniform(-0.1*i_episode, 0.1*i_episode)
			reward = scaling*(i_episode + random.uniform(-5.,5.))

			# Writing to the runs/ folder
			# add_scalar(tag="str tag", scalar_value="y axis value", global_step="x axis step", ylabel="something", xlabel="something")
			writer.add_scalar(f"return", reward, i_episode, ylabel="episode return", xlabel="num episodes", name=f"{algo}")
			writer.add_scalar(f"loss", loss, i_episode, ylabel="loss", xlabel="num episodes", name=f"{algo}")

		# write.close() is necessary to save your data!!
		writer.close()


############################ PLOTTING DATA ############################



# Instantiating the plotter object.
plotter = Plotter(logdir='runs')

# Plotting the first run by itself
# plotter.plot_run(run_name="DQN/run0", rolling_avg=True, window_size=2, tags=["return"])

# Plot an average over all runs in the experiment
plotter.plot_experiment(exp_name="DQfD", rolling_avg=True, window_size=None, tags=["return", "loss"])
	
	
