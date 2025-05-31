'''
program: bernoulli_streak.py
simulates number of Bernoulli trials needed to get a target streak of successes and visualizes results.
author: lauren chapa
date: 2025-05-31
'''

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# function to run a bernoulli trial
def bernoulli_trial(p, streak_target, number_runs):
    '''
    simulates the number of Bernoulli trials needed to get streak_target
    consecutive 1s, repeated number_runs times.

    returns empirical mean and variance of total trials required
    '''
    
    # empty list to store samples
    samples_taken = []
    
    for x in range(number_runs):
        consecutive = 0
        total = 0
        
        while consecutive < streak_target:
            sample = np.random.binomial(1, p)
            total += 1
            
            consecutive = consecutive + 1 if sample == 1 else 0
                
        samples_taken.append(total)
        
    return np.mean(samples_taken), np.var(samples_taken), samples_taken

# parameters
p = 0.6
streak_target = 3
number_runs = 1000  

# running Bernoulli trial simulation
emp_mean, emp_var, samples_taken = bernoulli_trial(p, streak_target, number_runs)

# printing empirical statistics
print(f"{'empirical mean:':<25}{emp_mean:>5.3f}")
print(f"{'empirical variance:':<25}{emp_var:>5.3f}")

# plot histogram of samples
plt.hist(samples_taken, 
         bins=range(min(samples_taken), max(samples_taken)+1), 
         color='#90caf9', 
         edgecolor='white', 
         alpha=0.5)
# plot mean line
plt.axvline(emp_mean, color='gray', linestyle='dashed', linewidth=1.5, label=f"Mean = {emp_mean:.3f}")

plt.title(f"Distribution of Trials until {streak_target} Consecutive Successes (p={p})")
plt.xlabel('Number of Trials')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()