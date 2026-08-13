# Unit tests for admin name matching (Python 2.7 / unittest)
import unittest

from nameauth import (
    strip_clan_tag,
    normalize_admin_name,
    normalize_admin_list,
    get_admin_level_by_name,
)


class TestStripClanTag(unittest.TestCase):

    def test_strips_bracket_tag(self):
        self.assertEqual(strip_clan_tag('[KKCK] Chaziz'), 'Chaziz')

    def test_strips_tag_with_symbols(self):
        self.assertEqual(strip_clan_tag('[LP!] MarceloGallardo'), 'MarceloGallardo')

    def test_no_tag_unchanged(self):
        self.assertEqual(strip_clan_tag('axelpro'), 'axelpro')

    def test_unclosed_bracket_unchanged(self):
        self.assertEqual(strip_clan_tag('[broken Chaziz'), '[broken Chaziz')

    def test_empty(self):
        self.assertEqual(strip_clan_tag(''), '')


class TestNormalize(unittest.TestCase):

    def test_case_and_tag(self):
        self.assertEqual(normalize_admin_name('  [KKCK] Chaziz  '), 'chaziz')

    def test_toml_entry_with_accidental_tag(self):
        self.assertEqual(normalize_admin_name('[KKCK] Chaziz'), 'chaziz')


class TestNormalizeList(unittest.TestCase):

    def test_drops_empty_and_normalizes(self):
        result = normalize_admin_list(['Chaziz', '', '  ', '[X] Bob'])
        self.assertEqual(result, frozenset(['chaziz', 'bob']))


class TestGetLevel(unittest.TestCase):

    def setUp(self):
        self.high = frozenset(['chaziz'])
        self.mid = frozenset(['bob'])
        self.low = frozenset(['carl'])

    def test_high_wins(self):
        high = frozenset(['shared'])
        mid = frozenset(['shared'])
        self.assertEqual(
            get_admin_level_by_name('[T] Shared', high, mid, self.low),
            'high',
        )

    def test_mid(self):
        self.assertEqual(
            get_admin_level_by_name('Bob', self.high, self.mid, self.low),
            'mid',
        )

    def test_low(self):
        self.assertEqual(
            get_admin_level_by_name('carl', self.high, self.mid, self.low),
            'low',
        )

    def test_none(self):
        self.assertIsNone(
            get_admin_level_by_name('nobody', self.high, self.mid, self.low)
        )

    def test_hash_like_string_does_not_match_name_list(self):
        # Old hash values must not grant admin when lists hold names
        self.assertIsNone(
            get_admin_level_by_name(
                '4a64aa3317f2bc80a2c7b8cbbb5c6908',
                self.high,
                self.mid,
                self.low,
            )
        )


if __name__ == '__main__':
    unittest.main()
