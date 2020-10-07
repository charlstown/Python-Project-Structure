
class Modules:
    """
    Class description: Explain what is this class for.
    Name the public methods from this class:
    - method_one
    - method_two
    """
    def __init__(self, config):
        """
        Class constructor: explain the constructor of the class.
        :param config: Explain the config parameter
        """
        # Declaring global variables from config
        self.config = config
        self.local_dir = config['local_dir']

    def __private_method(self):
        """
        Explain what is this private method for.
        :return:
        """
        # Declaring local variables from config
        test = self.config['bool']
        print(f"Modules: This is a private method with local variable {test}")

    def method_one(self):
        """
        Explain what is this public method for.
        :return:
        """
        # Declaring local variables from config
        user = self.config['user']
        print(f"Modules: This is the method one. With local variable {user}")

    def method_two(self, variable=False):
        """
        :param variable: Explain the param variable.
        :return:
        """
        print(f"Modules: This is the method two. With global variable {self.local_dir}")
        # Calling the private method
        if variable:
            self.__private_method()
