import pytest
from chatbot.keyword_matcher import KeywordMatcher
from automata.events import Event


class TestKeywordMatcher:
    def setup_method(self) -> None:
        self.matcher = KeywordMatcher()

    def test_match_diagnosa(self) -> None:
        inputs = ["diagnosa", "motor saya rusak", "kendaraan mogok", "masalah mesin", "rusak"]
        for text in inputs:
            assert self.matcher.match(text) == Event.DIAGNOSA, f"Failed on: {text}"

    def test_match_servis(self) -> None:
        inputs = ["servis", "perawatan berkala", "jadwal servis"]
        for text in inputs:
            assert self.matcher.match(text) == Event.SERVIS, f"Failed on: {text}"

    def test_match_tips(self) -> None:
        inputs = ["tips", "cara merawat motor", "tips perawatan", "edukasi kendaraan"]
        for text in inputs:
            assert self.matcher.match(text) == Event.TIPS, f"Failed on: {text}"

    def test_match_motor(self) -> None:
        inputs = ["motor", "sepeda motor", "roda dua", "matic"]
        for text in inputs:
            assert self.matcher.match(text) == Event.MOTOR, f"Failed on: {text}"

    def test_match_mobil(self) -> None:
        inputs = ["mobil", "roda empat", "sedan", "mobil pribadi"]
        for text in inputs:
            assert self.matcher.match(text) == Event.MOBIL, f"Failed on: {text}"

    def test_match_mesin(self) -> None:
        inputs = ["mesin", "engine", "busi", "starter"]
        for text in inputs:
            assert self.matcher.match(text) == Event.MESIN, f"Failed on: {text}"

    def test_match_ya(self) -> None:
        inputs = ["ya", "iya", "betul", "tentu", "ok"]
        for text in inputs:
            assert self.matcher.match(text) == Event.YA, f"Failed on: {text}"

    def test_match_tidak(self) -> None:
        inputs = ["tidak", "nggak", "ga", "enggak"]
        for text in inputs:
            assert self.matcher.match(text) == Event.TIDAK, f"Failed on: {text}"

    def test_match_mileage(self) -> None:
        assert self.matcher.match("5000") == Event.MILEAGE_5000
        assert self.matcher.match("10000") == Event.MILEAGE_10000
        assert self.matcher.match("15000") == Event.MILEAGE_15000
        assert self.matcher.match("20000") == Event.MILEAGE_20000
        assert self.matcher.match("25000") == Event.MILEAGE_25000

    def test_match_menu(self) -> None:
        inputs = ["menu", "kembali", "utama"]
        for text in inputs:
            assert self.matcher.match(text) == Event.MENU, f"Failed on: {text}"

    def test_match_selesai(self) -> None:
        inputs = ["selesai", "terima kasih", "makasih", "bye"]
        for text in inputs:
            assert self.matcher.match(text) == Event.SELESAI, f"Failed on: {text}"

    def test_match_unknown(self) -> None:
        inputs = ["apa kabar", "hari ini", "123xyz"]
        for text in inputs:
            assert self.matcher.match(text) == Event.UNKNOWN, f"Failed on: {text}"

    def test_case_insensitive(self) -> None:
        assert self.matcher.match("DIAGNOSA") == Event.DIAGNOSA
        assert self.matcher.match("Servis") == Event.SERVIS
        assert self.matcher.match("Mesin Rusak") == Event.DIAGNOSA

    def test_match_rem(self) -> None:
        assert self.matcher.match("rem") == Event.REM
        assert self.matcher.match("brake") == Event.REM

    def test_match_ban(self) -> None:
        assert self.matcher.match("ban") == Event.BAN
        assert self.matcher.match("roda") == Event.BAN
