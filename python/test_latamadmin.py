# Unit tests for latamadmin AutoBalance (no BF2 required)
import unittest

import latamadmin


class TestParseAb(unittest.TestCase):

    def test_need_arg(self):
        self.assertEqual(latamadmin.parse_ab_command('!ab'), 'need_arg')
        self.assertEqual(latamadmin.parse_ab_command('!AB'), 'need_arg')
        self.assertEqual(latamadmin.parse_ab_command('HUD_TEXT_CHAT_TEAM !ab'), 'need_arg')
        self.assertEqual(latamadmin.parse_ab_command('!ab foo'), 'need_arg')

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


class TestSetNext(unittest.TestCase):

    def setUp(self):
        self.catalog = [
            {'name': 'ramelle', 'mode': 'gpm_cq', 'layer': '16', 'index': 0},
            {'name': 'ramelle', 'mode': 'gpm_cq', 'layer': '32', 'index': 1},
            {'name': 'battle_of_keren', 'mode': 'gpm_cq', 'layer': '16', 'index': 2},
            {'name': 'hurtgen_forest', 'mode': 'gpm_cq', 'layer': '64', 'index': 3},
            {'name': 'alam_halfa', 'mode': 'gpm_cq', 'layer': '16', 'index': None},
        ]

    def test_parse_empty_and_id(self):
        self.assertEqual(latamadmin.parse_setnext_args([]).get('kind'), 'empty')
        self.assertEqual(latamadmin.parse_setnext_args(['7']).get('map_id'), 7)

    def test_parse_map_layer(self):
        parsed = latamadmin.parse_setnext_args(['ramelle', '16'])
        self.assertEqual(parsed['kind'], 'search')
        self.assertEqual(parsed['query'], 'ramelle')
        self.assertEqual(parsed['layer'], '16')
        self.assertIsNone(parsed['mode'])

    def test_parse_spaces_and_pr_layer(self):
        parsed = latamadmin.parse_setnext_args(['hurtgen', 'forest', 'std'])
        self.assertEqual(parsed['query'], 'hurtgen forest')
        self.assertEqual(parsed['layer'], '64')
        parsed2 = latamadmin.parse_setnext_args(['keren', 'cq', 'inf'])
        self.assertEqual(parsed2['mode'], 'gpm_cq')
        self.assertEqual(parsed2['layer'], '16')

    def test_resolve_unique(self):
        parsed = latamadmin.parse_setnext_args(['ramelle', '16'])
        status, item, extra = latamadmin.resolve_setnext_target(self.catalog, parsed)
        self.assertEqual(status, 'ok')
        self.assertEqual(item['index'], 0)

    def test_resolve_keren_substring(self):
        parsed = latamadmin.parse_setnext_args(['keren', '16'])
        status, item, extra = latamadmin.resolve_setnext_target(self.catalog, parsed)
        self.assertEqual(status, 'ok')
        self.assertEqual(item['name'], 'battle_of_keren')

    def test_resolve_hurtgen_spaces(self):
        parsed = latamadmin.parse_setnext_args(['hurtgen', 'forest', '64'])
        status, item, extra = latamadmin.resolve_setnext_target(self.catalog, parsed)
        self.assertEqual(status, 'ok')
        self.assertEqual(item['name'], 'hurtgen_forest')

    def test_resolve_many_without_layer(self):
        parsed = latamadmin.parse_setnext_args(['ramelle'])
        status, item, extra = latamadmin.resolve_setnext_target(self.catalog, parsed)
        self.assertEqual(status, 'many')
        self.assertEqual(len(extra), 2)

    def test_resolve_id(self):
        parsed = latamadmin.parse_setnext_args(['3'])
        status, item, extra = latamadmin.resolve_setnext_target(self.catalog, parsed)
        self.assertEqual(status, 'ok')
        self.assertEqual(item['name'], 'hurtgen_forest')

    def test_map_name_matches(self):
        self.assertTrue(latamadmin.map_name_matches('battle_of_keren', 'keren'))
        self.assertTrue(latamadmin.map_name_matches('hurtgen_forest', 'hurtgen forest'))
        self.assertFalse(latamadmin.map_name_matches('ramelle', 'keren'))


class TestCommandLevels(unittest.TestCase):

    def test_aliases(self):
        self.assertEqual(latamadmin.resolve_command_name('sn'), 'setnext')
        self.assertEqual(latamadmin.resolve_command_name('SN'), 'setnext')
        self.assertEqual(latamadmin.resolve_command_name('info'), 'info')

    def test_chat_commands(self):
        self.assertTrue(latamadmin.is_chat_command('ab'))
        self.assertTrue(latamadmin.is_chat_command('info'))
        self.assertTrue(latamadmin.is_chat_command('setnext'))
        self.assertTrue(latamadmin.is_chat_command('sn'))
        self.assertFalse(latamadmin.is_chat_command('stats'))

    def test_admin_tag_to_power(self):
        self.assertEqual(latamadmin.admin_tag_to_power('high'), 0)
        self.assertEqual(latamadmin.admin_tag_to_power('mid'), 1)
        self.assertEqual(latamadmin.admin_tag_to_power('low'), 2)
        self.assertEqual(latamadmin.admin_tag_to_power(None), 777)

    def test_defaults_mod_can_ab_info_setnext(self):
        self.assertTrue(latamadmin.can_use_command('ab', 2))
        self.assertTrue(latamadmin.can_use_command('ab', 0))
        self.assertFalse(latamadmin.can_use_command('ab', 777))
        self.assertTrue(latamadmin.can_use_command('info', 2))
        self.assertTrue(latamadmin.can_use_command('setnext', 2))
        self.assertTrue(latamadmin.can_use_command('sn', 1))
        self.assertFalse(latamadmin.can_use_command('info', 777))
        self.assertFalse(latamadmin.can_use_command('setnext', 777))
        self.assertFalse(latamadmin.can_use_command('ab_toggle', 2))

    def test_high_only_if_level_zero(self):
        old = dict(latamadmin.COMMAND_LEVELS)
        try:
            latamadmin.COMMAND_LEVELS['setnext'] = latamadmin.LEVEL_HIGH
            self.assertTrue(latamadmin.can_use_command('setnext', 0))
            self.assertFalse(latamadmin.can_use_command('setnext', 1))
            self.assertFalse(latamadmin.can_use_command('setnext', 2))
        finally:
            latamadmin.COMMAND_LEVELS.clear()
            latamadmin.COMMAND_LEVELS.update(old)


if __name__ == '__main__':
    unittest.main()
