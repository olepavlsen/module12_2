import unittest

import runner_and_tournament


class TournamentTest(unittest.TestCase):
    # all_results = {}
    # all_results = None

    # all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.hus = runner_and_tournament.Runner('Усейн', 10)
        self.andr = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)
        # return

    def test_run_1(self):
        run_1 = runner_and_tournament.Tournament(90, self.hus, self.nick)
        all_results = runner_and_tournament.Tournament.start(run_1)  # finishers
        self.assertTrue(all_results[max(all_results)] == self.nick)
        # return all_results

    def test_run_2(self):
        run_2 = runner_and_tournament.Tournament(90, self.andr, self.nick)
        all_results = runner_and_tournament.Tournament.start(run_2)  # finishers
        self.assertTrue(all_results[max(all_results)] == self.nick)
        # return all_results

    def test_run_3(self):
        run_3 = runner_and_tournament.Tournament(90, self.hus, self.andr, self.nick)
        all_results = runner_and_tournament.Tournament.start(run_3)  # finishers
        self.assertTrue(all_results[max(all_results)] == self.nick)
        # return all_results

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        # print(cls.test_run_2)
        # print(cls.test_run_3)


if __name__ == "__main__":
    unittest.main()
