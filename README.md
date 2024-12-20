# gym-cartlataccel

RL learns to drive a (very simple) car in <1s!

CartLatAccel is a simple 1D controls environment with added realistic noise and trajectory following. This task is a very simple, vectorized cart dynamics environment for testing RL [driving controls](https://blog.comma.ai/rlcontrols/). Think CartPole but without the pole!

The only inputs are x, v, and x_target, and the action is the steering force/accel.

## Installation

`pip install --user git+https://github.com/ellenjxu/gym-cartlataccel`

## Dependencies

`pip install -r requirements.txt`

## Usage

```python
import gymnasium as gym
import gym_cartlataccel

env = gym.make("CartLatAccel-v1")
```

set noise_mode in env.py.

custom PPO solves in <1s running ~1M steps, using a batch size of 1k: `python ppo.py`. Runs in 0.6s on single A2000 GPU (on my laptop 3050 it takes 1s).

```
Runtimes: rollout 0.014, gae 0.002, buffer 0.000, update 0.004
eps 31000.00, reward -0.053, t 0.93
Total time: 0.9299213886260986
rolling out best model
reward [-0.35961219]
```

![cartlataccel](https://github.com/user-attachments/assets/7c9e5570-bb28-4276-9bda-c1ff84ce7448)

---

Version 1.1 (2024-11-12): fixed normalization for reward, action space so now (-1,1) per timestep. Added action clipping to -1,1
