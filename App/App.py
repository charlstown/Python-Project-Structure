import argparse
import json

from Modules import Modules


class App:
    """
    Class description: Explain the main class.
    Name the public methods from this class:
    - run
    """

    def __init__(self, dir_config):
        """
        Class constructor: Here you should read the config file, generate
        the instances from modules and declare global variables.
        :param dir_config: Explain the dir_config parameter.
        """
        # Reading the config json file
        with open(dir_config) as f:
            config = json.load(f)

        # Variables
        self.config = config

        # Instance
        self.modules = Modules(self.config)

    def run(self):
        """
        This method runs the whole app and manage all calls.
        :return:
        """
        print("APP: Initializing the app")
        # Run first module method
        self.modules.method_one()

        # Run second module method
        self.modules.method_two(variable=True)


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", default="Data/config.json",
                        help="Add the config file path after this flag")
    parser.add_argument("--test", "-t", default=False, action='store_true',
                        help="This argument is a switcher, by default is false")
    args = parser.parse_args()

    # Argument variables
    arg_config = args.config
    arg_test = args.test
    print("Initial args:")
    print(f"- Config: {arg_config}")
    print(f"- Test: {arg_test}", '\n')

    # App execution
    my_app = App(dir_config=arg_config)
    my_app.run()
