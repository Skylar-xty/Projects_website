# Connect4
Connect4 is a game in which the players choose a color and then take turns dropping colored tokens into a six-row, seven-column vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. It's a zero-sum game, and could be solved by artificial algorithms like minimax with alpha-beta pruning.
## Introduction
I was an undergraduate research assistant in the [CognAc Lab](https://ivrylab.berkeley.edu/) at UC, Berkeley, and assisted the Postdoctoral Fellow in designing cognitive neuroscience experiments, focusing on the social and nonsocial behaviors of patients with cerebellar degeneration.

I
- Implemented several experiments and interactive tasks using JavaScript, PsychoPy, and Firebase, incorporating
Minimax and Search Algorithms to explore decision-making behaviors.
- Conducted data analysis using inverse binomial sampling to fit the parameters using MATLAB and Slurm.
- Built an experient for Goal congruency test.


## Algorithm

I use MiniMax algorithm for the AI agent.


## Results
Because there exists a solved conclusion which is the first-player-win circumstance, so we switched the game to the four-in-a-row game which has bigger action space.

The game contains two parts. First one is human-AI full game and the second one asks the player to choose between two potential moves. Moves of the players will be collected to Firebase.

Please refer to [Game: four-in-a-row](https://test1-2c630.firebaseapp.com/) for more details.

## Parameter Estimation
I modified the inverse binomial sampling methods referred from the work [Unbiased and efficient log-likelihood estimation with inverse binomial sampling](https://pubmed.ncbi.nlm.nih.gov/33362195/) for parameter estimation in our model using Google Cloud and Slurm for calculation.


## Final Pre
Please refer to [Cerebellum and planning depth in gameplay](https://github.com/Skylar-xty/Projects_website/blob/main/RA%40Berkeley/Cerebellum_and_planning_depth_in_gameplay.pdf) for the final presentation.


## Moreover
I also built an experient for Goal congruency test referring [Goal congruency dominates reward value in accounting for behavioral and neural correlates of value-based decision-making](https://www.nature.com/articles/s41467-019-12931-x).

