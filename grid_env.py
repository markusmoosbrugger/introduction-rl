from gym import Env, spaces
import random


class GridEnv(Env):
    """ OpenAI Gym Grid Environment

     Attributes
    ----------
    action_space: gym.spaces.Discrete
        The Space object corresponding to valid actions
    observation_space: gym.spaces.Tuple
        The Space object corresponding to valid observations
    reward_range:
        A tuple corresponding to the min and max possible rewards


    Methods
    -------
    step(action)
        The agent takes a step in the environment
    reset()
        Resets the state of the environment and returns an initial observation
    render()
        Renders/displays the environment

    """

    metadata = {'render.modes': ['console']}
    reward_range = (int(-100), int(100))

    def __init__(self, bomb_positions=None):
        super(GridEnv, self).__init__()

        self.height = 8
        self.width = 8
        self.pos = None

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple(
            (spaces.Discrete(self.height), spaces.Discrete(self.width)))

        self.moves = {0: (0, -1),   # move down
                      1: (1, 0),    # move right
                      2: (0, 1),    # move up
                      3: (-1, 0),   # move left
                      }

        self.action_names = ['down', 'right', 'up', 'left']

        self.start_pos = (0, 0)
        self.end_pos = (7, 7)

        if bomb_positions:
            self.bomb_positions = bomb_positions
        else:
            self.bomb_positions = self.create_bomb_positions()

        self.reset()

    def step(self, action):
        """
        Performs one timestep and moves the current position by one step to the given direction.
        When end of episode is reached, you are responsible for calling `reset()`
        to reset this environment's state.

        Accepts an action and returns a tuple (observation, reward, done, info).

        :param action: an action provided by the agent
        :return:
            observation (object): the current position in the grid
            reward (float) : amount of reward returned after previous action
            done (bool): whether the episode has ended, in which case further step() calls
            will return undefined results
            info (dict): may contain auxiliary diagnostic information (helpful for debugging,
            and sometimes learning); currently not used
        """

        x, y = self.moves[action]
        # update position
        self.pos = self.pos[0] + x, self.pos[1] + y

        # check if position is outside of field
        self.pos = max(0, self.pos[0]), max(0, self.pos[1])
        self.pos = min(self.pos[0], self.width - 1), min(self.pos[1], self.height - 1)

        if self.pos == self.end_pos:
            # goal reached, return positive reward
            return self.pos, 100, True, {}

        elif self.pos in self.bomb_positions:
            # bomb at current position, return negative reward
            return self.pos, -100, False, {}

        # usual reward is -1
        return self.pos, -1, False, {}

    def reset(self):
        """ Resets the starting position and returns an initial observation.

        :return: the initial position
        """
        self.pos = self.start_pos
        return self.pos

    def render(self, mode='console'):
        """
        Renders the environment.
        """

        if mode != 'console':
            raise NotImplementedError()
        print("|\t" + "___\t" * self.width + "|")
        for i in reversed(range(self.height)):
            print("|\t", end="")
            for j in range(self.width):
                printed = False
                if self.pos == (j, i):
                    print("x", end="")
                    printed = True
                if (j, i) == self.start_pos:
                    print("A", end="")
                    printed = True
                if (j, i) == self.end_pos:
                    print("B", end="")
                    printed = True
                if (j, i) in self.bomb_positions:
                    print("!!", end="")
                    printed = True

                if not printed:
                    print(".", end="")

                print("\t", end="")

            print("|")
        print("|\t" + "___\t" * self.width + "|")

    def create_bomb_positions(self, num_bombs=5):
        """
        Sets a random seed and creates the bombs at random positions.

        :param num_bombs: the number of bombs to be created
        :return: the positions of the created bombs
        """
        bomb_positions = []
        # set random seed to facilitate reproducibility
        random.seed(100)
        for _ in range(num_bombs):
            x = random.randrange(self.height)
            y = random.randrange(self.height)
            bomb_positions.append((x, y))

        return bomb_positions

    def get_minimum_number_of_steps(self):
        """
        Get the minimum number of steps required to move from the start position to
        the end position.

        :return: The number of steps required.
        """
        steps_x = abs(self.start_pos[0] - self.end_pos[0])
        steps_y = abs(self.start_pos[1] - self.end_pos[1])

        return steps_x + steps_y

    def get_action_index(self, action_name):
        """
        Get the index of the action specified by the given action name.

        :param action_name: The name of the action
        :return: The index of the action
        """
        return self.action_names.index(action_name)

    def get_action_name(self, action_index):
        """
        Get the name of the action specified by the given action index.

        :param action_index: The index of the action.
        :return: The name of the action.
        """
        return self.action_names[action_index]
