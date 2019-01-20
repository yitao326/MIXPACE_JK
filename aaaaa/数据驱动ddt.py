from ddt import ddt, data
import unittest

data = [
    {"user":"111", "psw":"111"},
    {"user":"222", "psw":"222"},
    {"user":"333", "psw":"333"},
    {"user":"444", "psw":"444"},
]

@ddt
class Test(unittest.TestCase):

    @data(*data)
    def test_login(self, a):
        print(a)
        print(a["user"], a["psw"])

if __name__ == '__main__':
    unittest.main()
