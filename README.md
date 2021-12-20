
## Playing Flappy Bird Using Deep Reinforcement Learning (Based on Double Q Learning and DDQN)
![](README_md_files%5Cimage%20%282%29.png?v=1&type=image)
![](README_md_files%5Cimage%20%283%29.png?v=1&type=image)[](README_md_files%5Cimage.png?v=1&type=image)

We rewrite the code from Flood Sun's Framework based on Double Q Learning(but we use a Q-network to replace Q-function) and DDQN with these changes:

 - 1,every t episodes draw a terminal-reward figure

![DDQN](README_md_files%5CReal-1600-change-epsilon0.2-0.1-greedy-algorithm2.png?v=1&type=image)

 - 2,try another epsilon-greedy algorithm to fit this game.

We still have these problems:

 - 1,The agent's behavior is not good enough after training(try   
   policy-based algorithm in the future).
 - 2,How can we achieve to use the less episodes to train the agent.
   
 - 3,It could easily fall into  local  optimum(we try to change the   
   epsilon-greedy algorithm but it improves a little).
 - 4,If the training results satisfy a kind of distribution. The
   training result is so discrete, we are not able to ensure train a
   promising robot in a certain episodes.
 - 5,It seems to have over-fitting problem.

## Result
![输入图片描述](README_md_files%5Cdouble-QN-real-70000%20%2000_00_00-00_00_30.gif?v=1&type=image)

## About the code

As a reinforcement learning problem, we knows we need to obtain observations and output actions, and the 'brain' do the processing work.

Therefore, you can easily understand the BrainDDQN.py code. There are three interfaces:

1. getInitState() for initialization
2. getAction()
3. setPerception(nextObservation,action,reward,terminal)

the game interface just need to be able to feed the action to the game and output observation,reward,terminal


## Disclaimer

> This work is based on the repo:  [floodsung](https://github.com/floodsung) /**[DRL-FlappyBird](https://github.com/floodsung/DRL-FlappyBird)**

