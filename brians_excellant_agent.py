from pysc2.agents import base_agent
from pysc2.lib import actions


class BrianAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(BrianAgent, self).step(obs)

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])