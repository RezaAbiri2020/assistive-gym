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

# finding the boundaries of spaces
print('action space information:')
print(env.action_space)
print('high:')
print(env.action_space.high)
print('low:')
print(env.action_space.low)

print(' observation space information:')
print(env.observation_space)
print('high:')
print(env.observation_space.high)
print('low:')
print(env.observation_space.low)

for episode in range(1): # it seems each episode defined as 200 samples 
    env.render()
    observation = env.reset()

    for dt in range(70):
        #print(dt)
        env.render()
        #action = env.action_space.sample()
        #print(action)
        #action=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
        action=np.array([1, 0, 0, 0, 0, 0, 0])
        observation, reward, done, info = env.step(action)
        #print(observation)
        #print(reward)
        #print('next sampleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee point')
        #print(done)
        #print(info)
        if done:
            print("EEEEEEEEEEEpisode finished after {} timesteps".format(dt+1))
            break
env.close()

