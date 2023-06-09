from gym.envs.registration import register

register(
    id='maze',
    entry_point='your_custom_env_package:maze',
)
