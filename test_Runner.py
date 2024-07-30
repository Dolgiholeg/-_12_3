import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
    def walk(self):
        self.distance += 5
    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Alex')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Max')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
            runner = Runner('Fred')
            runner1 = Runner('Ilia')
            for i in range(10):
                runner.run()
                runner1.walk()
            self.assertNotEqual(runner.distance, runner1.distance)

if __name__ == "__main__":
    unittest.main()

