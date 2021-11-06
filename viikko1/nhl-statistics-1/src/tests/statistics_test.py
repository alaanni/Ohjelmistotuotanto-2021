import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics (unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_setUp_toimii(self):
        self.assertEqual(0,0)
    
    def test_palauttaa_oikean_pelaajan(self):
        pelaaja = self.statistics.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")
        self.assertEqual(pelaaja.team, "EDM")
        self.assertEqual(pelaaja.goals, 4)
        self.assertEqual(pelaaja.assists, 12)
        self.assertEqual(pelaaja.points, 16)
        self.assertEqual(pelaaja.__str__(), "Semenko EDM 4 + 12 = 16")
    
    def test_none_jos_pelaajaa_ei_ole(self):
        pelaaja = self.statistics.search("Semenka")
        self.assertEqual(pelaaja, None)

    def test_palauttaa_listan(self):
        list = self.statistics.team("PIT")
        self.assertEqual(len(list), 1)

    def test_top_scorers_toimii(self):
        topPlayer = self.statistics.top_scorers(1)
        self.assertEqual(topPlayer[0].name, "Gretzky")
