# gym-cartlataccel

RL learns to drive a (very simple) car in ~0.6s!

This task is a very simple, vectorized cart dynamics environment for testing RL driving controls. Think CartPole, but for cars (it's literally just CartPole without the pole, with added realistic noise and trajectory following).

The only inputs are x, v, and x_target, and the action is the steering force/accel.

## Installation

`pip install --user git+https://github.com/ellenjxu/gym-cartlataccel`

## Dependencies

`pip install -r requirements.txt`

## Usage

```python
import gymnasium as gym
import gym_cartlataccel

env = gym.make("CartLatAccel-v0")
```

set noise_mode in env.py.

custom PPO solves in <1s running ~1M steps, using a batch size of 1k: `python ppo.py`


![cartlataccel](https://github.com/user-attachments/assets/7c9e5570-bb28-4276-9bda-c1ff84ce7448)
