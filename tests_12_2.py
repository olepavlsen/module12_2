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
        self.res = {}
        run_1 = runner_and_tournament.Tournament(90, self.hus, self.nick)
        result_1 = runner_and_tournament.Tournament.start(run_1)  # finishers
        self.assertTrue(result_1[max(result_1)] == self.nick)
        for place, runner in result_1.items():
            self.res[place] = runner.name
        self.all_results[1] = self.res

    def test_run_2(self):
        self.res = {}
        run_2 = runner_and_tournament.Tournament(90, self.andr, self.nick)
        result_2 = runner_and_tournament.Tournament.start(run_2)  # finishers
        self.assertTrue(result_2[max(result_2)] == self.nick)
        for place, runner in result_2.items():
            self.res[place] = runner.name
        self.all_results[2] = self.res

    def test_run_3(self):
        self.res = {}
        run_3 = runner_and_tournament.Tournament(90, self.hus, self.andr, self.nick)
        result_3 = runner_and_tournament.Tournament.start(run_3)  # finishers
        self.assertTrue(result_3[max(result_3)] == self.nick)
        for place, runner in result_3.items():
            self.res[place] = runner.name
        self.all_results[3] = self.res

    @classmethod
    def tearDownClass(cls):
        print(f'{cls.all_results[1]} \n{cls.all_results[2]} \n{cls.all_results[3]}')


if __name__ == "__main__":
    unittest.main()
