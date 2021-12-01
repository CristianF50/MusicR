from musicrpy import *
import unittest 
from unittest import result, TestCase, mock
from unittest.mock import patch 

class test_semillas(unittest.TestCase):

    def test_semillas(self):
        mock_semillas_patcher = patch('musicrpy.sp.current_user_saved_tracks')
        res = {'href': '', 'items': [{'added_at': '', 'track': {'album': {'album_type': '', 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': 'artist', 'uri': ''}], 'available_markets': [], 'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'images': [{'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}], 'name': '', 'release_date': '', 'release_date_precision': '', 'total_tracks': '', 'type': '', 'uri': ''}, 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': '', 'uri': ''}], 'available_markets': [], 'disc_number': '', 'duration_ms': '', 'explicit': '', 'external_ids': {'isrc': ''}, 'external_urls': {'spotify': ''}, 'href': '', 'id': '2Gsare6GuBE2Ph3zJanNKl', 'is_local': '', 'name': '', 'popularity': '', 'preview_url': '', 'track_number': '', 'type': '', 'uri': ''}}], 'limit': '', 'next': '', 'offset': '', 'previous': '', 'total': ''}

        mock_semillas = mock_semillas_patcher.start()
        mock_semillas.return_value = res

        response = getSemillas()

        mock_semillas_patcher.stop()

        self.assertEqual(response, ['2Gsare6GuBE2Ph3zJanNKl'])

class test_semillas(unittest.TestCase):

    def test_semillas(self):
        mock_semillas_patcher = patch('musicrpy.sp.current_user_saved_tracks')
        res = {'href': '', 'items': [{'added_at': '', 'track': {'album': {'album_type': '', 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': 'artist', 'uri': ''}], 'available_markets': [], 'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'images': [{'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}], 'name': '', 'release_date': '', 'release_date_precision': '', 'total_tracks': '', 'type': '', 'uri': ''}, 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': '', 'uri': ''}], 'available_markets': [], 'disc_number': '', 'duration_ms': '', 'explicit': '', 'external_ids': {'isrc': ''}, 'external_urls': {'spotify': ''}, 'href': '', 'id': '2Gsare6GuBE2Ph3zJanNKl', 'is_local': '', 'name': '', 'popularity': '', 'preview_url': '', 'track_number': '', 'type': '', 'uri': ''}}], 'limit': '', 'next': '', 'offset': '', 'previous': '', 'total': ''}

        mock_semillas = mock_semillas_patcher.start()
        mock_semillas.return_value = res

        response = getSemillas()

        mock_semillas_patcher.stop()

        self.assertEqual(response, ['2Gsare6GuBE2Ph3zJanNKl'])



if __name__ == "__main__":
    unittest.main()