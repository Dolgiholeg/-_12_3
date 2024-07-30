import unittest
import test_Runner
import test_12_2

runST = unittest.TestSuite()
# suiteTest.addTest(unittest.makeSuite(test_Runner.RunnerTest))
runST.addTests(unittest.TestLoader().loadTestsFromTestCase(test_Runner.RunnerTest))
runST.addTests(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)