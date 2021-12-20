# -------------------------
# Project:Double Deep Q-Learning on Flappy Bird
# Author: DSTRC-W.&G.
# Date: 2021.12.20
# -------------------------

import cv2
import sys
sys.path.append("game/")
import game.wrapped_flappy_bird as game
from BrainDDQN import BrainDQN
import numpy as np
import matplotlib.pyplot as plt

# preprocess raw image to 80*80 gray image
def preprocess(observation):
	observation = cv2.cvtColor(cv2.resize(observation, (80, 80)), cv2.COLOR_BGR2GRAY)
	ret, observation = cv2.threshold(observation,1,255,cv2.THRESH_BINARY)
	return np.reshape(observation,(80,80,1))

def playFlappyBird():
	# Step 1: init BrainDQN
	actions = 2
	brain = BrainDQN(actions)
	# Step 2: init Flappy Bird Game
	flappyBird = game.GameState()
	# Step 3: play game
	# Step 3.1: obtain init state
	action0 = np.array([1,0])  # do nothing
	observation0, reward0, terminal = flappyBird.frame_step(action0)
	observation0 = cv2.cvtColor(cv2.resize(observation0, (80, 80)), cv2.COLOR_BGR2GRAY)
	ret, observation0 = cv2.threshold(observation0,1,255,cv2.THRESH_BINARY)
	brain.setInitState(observation0)

	t = 1600
	col = np.zeros(20*t)
	i = 0
	rtg = 0
	# Step 3.2: run the game
	while 1!= 0:
		action = brain.getAction()
		nextObservation,reward,terminal = flappyBird.frame_step(action)
		rtg = rtg + reward
		if terminal:
			col[i] = rtg
			i = i + 1
			rtg = 0
			#draw a reward-figure every t steps
			if i % t==0:
				x = np.arange(0, i)
				plt.plot(x, col[0:i], 'r--')
				plt.ylabel('reward')
				plt.xlabel('times')
				plt.show()
		nextObservation = preprocess(nextObservation)
		brain.setPerception(nextObservation,action,reward,terminal)

def main():
	playFlappyBird()

if __name__ == '__main__':
	main()