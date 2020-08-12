from pysc2.env import sc2_env, run_loop
from pysc2.lib import actions, features
from zomp_agent import ZompAgent
from brians_excellant_agent import BrianAgent
from absl import app


def main(_):
    agent_chris = ZompAgent()
    agent_brian = BrianAgent()
    with sc2_env.SC2Env(
        map_name="Simple64",
        players=[sc2_env.Agent(sc2_env.Race.zerg), sc2_env.Agent(sc2_env.Race.terran)],
        agent_interface_format=features.AgentInterfaceFormat(
            action_space=actions.ActionSpace.RAW,
            use_raw_units=True,
            raw_resolution=64,
        ),
    ) as env:
        run_loop.run_loop([agent_chris, agent_brian], env)


if __name__ == "__main__":
    app.run(main)

