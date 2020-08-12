from pysc2.agents import base_agent
from pysc2.lib import actions

class Operation():
    pass

class Task():
    pass

class ZompAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(ZompAgent, self).step(obs)

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])