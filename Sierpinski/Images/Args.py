import sys


class ArgError(LookupError):
    def __init__(self):
        super(ArgError, self).__init__('expected more arguments in program call')


class Args(dict):
    def __init__(self, parameters={}, h=''):
        try:
            assert all(map(lambda x: isinstance(x, str), parameters.keys()))
            super(Args, self).__init__(parameters)
            if '-h' in sys.argv:
                print(h)
                sys.exit()
            self.__init()
        except AssertionError:
            raise TypeError('the keys should be an instance of str') from None

    def __init(self):
        keys = self.keys()
        for i in range(1, len(sys.argv)):
            key = sys.argv[i][1:]
            if key in keys:
                try:
                    self[key] = type(self[key])(sys.argv[i + 1])
                except IndexError:
                    raise ArgError() from None
