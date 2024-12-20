import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_player_none(self):
        player = self.stats.search("Asdfgh")
        self.assertIsNone(player)

    def test_team(self):
        team = self.stats.team("EDM")
        player_names = [player.name for player in team]
        self.assertEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_not_defined(self):
        top_players = self.stats.top(3)
        expected_names = ["Gretzky", "Lemieux", "Yzerman"]
        self.assertEqual([player.name for player in top_players], expected_names)

    def test_top_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        expected_names = ["Gretzky", "Lemieux", "Yzerman"]
        self.assertEqual([player.name for player in top_players], expected_names)

    def test_top_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        expected_names = ["Lemieux", "Yzerman", "Kurri"]
        self.assertEqual([player.name for player in top_players], expected_names)

    def test_top_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        expected_names = ["Gretzky", "Yzerman", "Lemieux"]
        self.assertEqual([player.name for player in top_players], expected_names)
