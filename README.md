# gym-cartlataccel

A simple, vectorized cart environment for testing RL controls on OpenAI Gym.

Custom PPO implement solves in <1s running ~1M steps, using a batch size of 1k.

## Installation

`pip install --user git+https://github.com/ellenjxu/gym-cartlataccel`

## Dependencies

`pip install -r requirements.txt`

## Usage

```
import gymnasium as gym
import gym_cartlataccel

env = gym.make("CartLatAccel-v0")
```

`python ppo.py`
