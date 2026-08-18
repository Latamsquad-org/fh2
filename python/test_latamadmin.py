# Unit tests for latamadmin AutoBalance (no BF2 required)
import unittest

import latamadmin


class TestParseAb(unittest.TestCase):

    def test_status(self):
        self.assertEqual(latamadmin.parse_ab_command('!ab'), 'status')
        self.assertEqual(latamadmin.parse_ab_command('!AB'), 'status')
        self.assertEqual(latamadmin.parse_ab_command('HUD_TEXT_CHAT_TEAM !ab'), 'status')

    def test_on_off(self):
        self.assertEqual(latamadmin.parse_ab_command('!ab on'), 'on')
        self.assertEqual(latamadmin.parse_ab_command('!ab ON'), 'on')
        self.assertEqual(latamadmin.parse_ab_command('!ab off'), 'off')
        self.assertEqual(latamadmin.parse_ab_command('!ab enable'), 'on')
        self.assertEqual(latamadmin.parse_ab_command('!ab disable'), 'off')

    def test_not_ab(self):
        self.assertIsNone(latamadmin.parse_ab_command('!stats'))
        self.assertIsNone(latamadmin.parse_ab_command('ab on'))
        self.assertIsNone(latamadmin.parse_ab_command(''))


class TestSwitchAllowed(unittest.TestCase):

    def test_equal_to_plus_one_ok(self):
        # 9 vs 9 -> 10 vs 8 (diff 2) permitido
        self.assertTrue(latamadmin.is_switch_allowed(9, 9, 1, 2))

    def test_diff_two_to_stacked_blocked(self):
        # 10 vs 8, el de 8 se pasa a 10 -> 11 vs 7 (diff 4)
        self.assertFalse(latamadmin.is_switch_allowed(10, 8, 2, 1))

    def test_diff_two_to_weak_ok(self):
        # 10 vs 8, el de 10 se pasa a 8 -> 9 vs 9
        self.assertTrue(latamadmin.is_switch_allowed(10, 8, 1, 2))

    def test_same_team_ok(self):
        self.assertTrue(latamadmin.is_switch_allowed(10, 8, 1, 1))

    def test_improving_still_over_ok(self):
        # 12 vs 8, el de 12 se pasa a 8 -> 11 vs 9 (diff 2)
        self.assertTrue(latamadmin.is_switch_allowed(12, 8, 1, 2))

    def test_worsening_blocked(self):
        self.assertFalse(latamadmin.is_switch_allowed(12, 8, 2, 1))


class TestTargetIfIllegal(unittest.TestCase):

    def test_balanced_no_move(self):
        self.assertIsNone(latamadmin.target_team_if_illegal(10, 8, 1))
        self.assertIsNone(latamadmin.target_team_if_illegal(10, 8, 2))
        self.assertIsNone(latamadmin.target_team_if_illegal(9, 9, 1))

    def test_stacked_joiner_moved(self):
        # Ya conto 11 vs 8 (diff 3); el jugador esta en el 11
        self.assertEqual(latamadmin.target_team_if_illegal(11, 8, 1), 2)

    def test_player_on_weak_not_moved(self):
        self.assertIsNone(latamadmin.target_team_if_illegal(11, 8, 2))

    def test_no_team_goes_to_smaller(self):
        self.assertEqual(latamadmin.target_team_if_illegal(10, 8, 0), 2)
        self.assertEqual(latamadmin.target_team_if_illegal(8, 10, 0), 1)

    def test_no_team_tie_defaults_team1(self):
        self.assertEqual(latamadmin.target_team_if_illegal(5, 5, 0), 1)


class TestHelpers(unittest.TestCase):

    def test_other_team(self):
        self.assertEqual(latamadmin.other_team(1), 2)
        self.assertEqual(latamadmin.other_team(2), 1)
        self.assertEqual(latamadmin.other_team(0), 0)

    def test_smaller_larger(self):
        self.assertEqual(latamadmin.smaller_team(10, 8), 2)
        self.assertEqual(latamadmin.larger_team(10, 8), 1)
        self.assertEqual(latamadmin.smaller_team(4, 4), 0)


class TestInfoHelpers(unittest.TestCase):

    def test_parse_bang(self):
        self.assertEqual(latamadmin.parse_bang_command('!info'), ('info', []))
        self.assertEqual(
            latamadmin.parse_bang_command('HUD_TEXT_CHAT_TEAM !info chaziz last'),
            ('info', ['chaziz', 'last']),
        )
        self.assertIsNone(latamadmin.parse_bang_command('info'))

    def test_parse_info_args(self):
        self.assertEqual(latamadmin.parse_info_args([]), ('round', None, False))
        self.assertEqual(
            latamadmin.parse_info_args(['chaziz']),
            ('player', 'chaziz', False),
        )
        self.assertEqual(
            latamadmin.parse_info_args(['chaziz', 'last']),
            ('player', 'chaziz', True),
        )
        self.assertEqual(
            latamadmin.parse_info_args(['#12']),
            ('player', '#12', False),
        )

    def test_pretty_names(self):
        self.assertEqual(latamadmin.pretty_map_name('hurtgen_forest'), 'Hurtgen Forest')
        self.assertEqual(latamadmin.pretty_gamemode('gpm_cq'), 'Conquest')

    def test_maplist_append(self):
        text = (
            'rem ignore\n'
            'mapList.append ramelle gpm_cq 16\n'
            'mapList.append alam_halfa gpm_cq 32\n'
        )
        entries = latamadmin.parse_maplist_append_text(text)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]['name'], 'ramelle')
        self.assertEqual(
            latamadmin.format_map_entry(entries[0]),
            'Ramelle (Conquest, 16)',
        )

    def test_maplist_list_output(self):
        text = '0: ramelle gpm_cq 16\n1: "levels/alam_halfa" gpm_cq 32\n'
        entries = latamadmin.parse_maplist_list_output(text)
        self.assertEqual(entries[1]['name'], 'alam_halfa')
        self.assertEqual(latamadmin.map_entry_at(entries, 0)['layer'], '16')
        self.assertIsNone(latamadmin.map_entry_at(entries, 9))

    def test_round_info_lines(self):
        lines = latamadmin.format_round_info_lines({
            'server_name': 'LATAMSQUAD FH2',
            'current': 'Ramelle (Conquest, 16)',
            'next': 'Alam Halfa (Conquest, 16)',
            'players': 12,
            'max_players': 100,
            'team1': 6,
            'team2': 6,
            'tickets1': 250,
            'tickets2': 248,
            'team1_name': 'USA',
            'team2_name': 'Germany',
        })
        self.assertEqual(lines[0], 'Servidor: LATAMSQUAD FH2')
        self.assertTrue(lines[1].startswith('Mapa:'))
        self.assertTrue('Tickets: USA 250 | Germany 248' in lines[-1])

    def test_player_name_matches(self):
        self.assertTrue(latamadmin.player_name_matches('[KKCK] Chaziz', 'chaz'))
        self.assertTrue(latamadmin.player_name_matches('[KKCK] Chaziz', 'kkck'))
        self.assertFalse(latamadmin.player_name_matches('Chaziz', 'bob'))

    def test_player_info_lines(self):
        lines = latamadmin.format_player_info_lines({
            'name': 'Chaziz',
            'team': 1,
            'score': 10,
            'kills': 3,
            'deaths': 1,
            'ping': 40,
            'ip': '1.2.3.4',
            'show_last': True,
        })
        self.assertTrue(lines[0].startswith('Chaziz:'))
        self.assertEqual(lines[1], '----->1.2.3.4')
        self.assertTrue('no disponible' in lines[2])


if __name__ == '__main__':
    unittest.main()
