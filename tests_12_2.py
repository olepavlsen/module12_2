import unittest

import runner_and_tournament


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.hus = runner_and_tournament.Runner('Усейн', 10)
        self.andr = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_run_1(self):
        run_1 = runner_and_tournament.Tournament(90, self.hus, self.nick)
        result_1 = runner_and_tournament.Tournament.start(run_1)  # finishers
        self.assertTrue(result_1[max(result_1)] == self.nick)
        for place, runner in result_1.items():
            self.all_results[place] = runner.name
            # for i in range(len(result_1)):
        #     self.all_results[i + 1] = result_1[i + 1].name



    def test_run_2(self):
        run_2 = runner_and_tournament.Tournament(90, self.andr, self.nick)
        result_2 = runner_and_tournament.Tournament.start(run_2)  # finishers
        self.assertTrue(result_2[max(result_2)] == self.nick)
        for place, runner in result_2.items():
            self.all_results[place] = runner.name
            # for i in range(len(result_2)):
        #     self.all_results[i + 1] = result_2[i + 1].name

    # def tearDown(self):
    #     print(self.all_results)

    def test_run_3(self):
        run_3 = runner_and_tournament.Tournament(90, self.hus, self.andr, self.nick)
        result_3 = runner_and_tournament.Tournament.start(run_3)  # finishers
        self.assertTrue(result_3[max(result_3)] == self.nick)
        for place, runner in result_3.items():
            self.all_results[place] = runner.name
            # for i in range(len(result_3)):
        #     self.all_results[i + 1] = result_3[i + 1].name

    def tearDown(self):
        print(self.all_results)
    # @classmethod
    # def tearDownClass(cls):
    #     print(cls.all_results)
        # print(cls.test_run_2)
        # print(cls.test_run_3)


if __name__ == "__main__":
    unittest.main()
