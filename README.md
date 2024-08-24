# gym-cartlataccel

A simple, vectorized cart environment for testing RL controls on OpenAI Gym.

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

custom PPO solves in <1s running ~1M steps, using a batch size of 1k: `python ppo.py`


![cartlataccel](https://github.com/user-attachments/assets/7c9e5570-bb28-4276-9bda-c1ff84ce7448)
