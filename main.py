from pysc2.env import sc2_env, run_loop
from pysc2.lib import actions, features
from simple_agent import SimpleAgent
from absl import app


def main(_):
    agent = SimpleAgent()
    try:
        while True:
            with sc2_env.SC2Env(
                map_name="Simple64",
                players=[sc2_env.Agent(sc2_env.Race.zerg),
                    sc2_env.Bot(sc2_env.Race.random,
                    sc2_env.Difficulty.very_easy)],
                agent_interface_format=features.AgentInterfaceFormat(
                    action_space=actions.ActionSpace.RAW,
                    use_raw_units=True,
                    raw_resolution=64,
                ),
            ) as env:
                run_loop.run_loop([agent], env)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    app.run(main)

