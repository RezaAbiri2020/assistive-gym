import gym, sys, argparse
import numpy as np
import assistive_gym

if sys.version_info < (3, 0):
    print('Please use Python 3')
    exit()

parser = argparse.ArgumentParser(description='Assistive Gym Environment Viewer')
parser.add_argument('--env', default='ScratchItchJaco-v0',
                    help='Environment to test (default: ScratchItchJaco-v0)')
args = parser.parse_args()

env = gym.make(args.env)

episode = 0
while episode <1:
    episode = episode +1
    done = False
    env.render()
    observation = env.reset()
    
    action = env.action_space.sample()
    print('Observation size:', np.shape(observation), 'Action size:', np.shape(action))
    print('next episoddddddddddddddddddddddddddddddddddddddddddddddddddddddddde')
    while not done:
        env.render()
        #action = env.action_space.sample()
        #print(action)
        action=np.array([-100, -100, -100, -100, -100, -100, -100])
        observation, reward, done, info = env.step(action)
        #print(observation)
        #print(reward)
        #print('next sampleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee point')
        #print(done)
        #print(info)
