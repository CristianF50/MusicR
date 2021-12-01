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

class test_recomendaciones(unittest.TestCase):

    def test_recomendaciones(self):
        mock_recomendaciones_patcher = patch('musicrpy.sp.recommendations')
        res = {'tracks': [{'album': {'album_type': 'SINGLE', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3ccVtqcqedranb7y8eywJ5'}, 'href': 'https://api.spotify.com/v1/artists/3ccVtqcqedranb7y8eywJ5', 'id': '3ccVtqcqedranb7y8eywJ5', 'name': 'Blanco White', 'type': 'artist', 'uri': 'spotify:artist:3ccVtqcqedranb7y8eywJ5'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'external_urls': {'spotify': 'https://open.spotify.com/album/5OxtmtnqvwogIYMdo2h4eQ'}, 'href': 'https://api.spotify.com/v1/albums/5OxtmtnqvwogIYMdo2h4eQ', 'id': '5OxtmtnqvwogIYMdo2h4eQ', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02f1e82d635519bf864c452a65', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851f1e82d635519bf864c452a65', 'width': 64}], 'name': 'Colder Heavens EP', 'release_date': '2017-03-31', 'release_date_precision': 'day', 'total_tracks': 4, 'type': 'album', 'uri': 'spotify:album:5OxtmtnqvwogIYMdo2h4eQ'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3ccVtqcqedranb7y8eywJ5'}, 'href': 'https://api.spotify.com/v1/artists/3ccVtqcqedranb7y8eywJ5', 'id': '3ccVtqcqedranb7y8eywJ5', 'name': 'Blanco White', 'type': 'artist', 'uri': 'spotify:artist:3ccVtqcqedranb7y8eywJ5'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'disc_number': 1, 'duration_ms': 284400, 'explicit': False, 'external_ids': {'isrc': 'UK4GH1700003'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/7BYQUH8RD2mPoXjZEawyjy'}, 'href': 'https://api.spotify.com/v1/tracks/7BYQUH8RD2mPoXjZEawyjy', 'id': '7BYQUH8RD2mPoXjZEawyjy', 'is_local': False, 'name': 'Outsider', 'popularity': 44, 'preview_url': 'https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a', 'track_number': 3, 'type': 'track', 'uri': 'spotify:track:7BYQUH8RD2mPoXjZEawyjy'}], 'seeds': [{'initialPoolSize': 249, 'afterFilteringSize': 249, 'afterRelinkingSize': 249, 'id': '2Gsare6GuBE2Ph3zJanNKl', 'type': 'TRACK', 'href': 'https://api.spotify.com/v1/tracks/2Gsare6GuBE2Ph3zJanNKl'}, {'initialPoolSize': 249, 'afterFilteringSize': 249, 'afterRelinkingSize': 249, 'id': '63cgeMV2nSl851R7jy4lxw', 'type': 'TRACK', 'href': 'https://api.spotify.com/v1/tracks/63cgeMV2nSl851R7jy4lxw'}, {'initialPoolSize': 249, 'afterFilteringSize': 249, 'afterRelinkingSize': 249, 'id': '7sTcNcxIIRpEdSu3W6k8Ky', 'type': 'TRACK', 'href': 'https://api.spotify.com/v1/tracks/7sTcNcxIIRpEdSu3W6k8Ky'}, {'initialPoolSize': 249, 'afterFilteringSize': 249, 'afterRelinkingSize': 249, 'id': '6Wz9rIfo9tOBcVCd1Mo7F7', 'type': 'TRACK', 'href': 'https://api.spotify.com/v1/tracks/6Wz9rIfo9tOBcVCd1Mo7F7'}, {'initialPoolSize': 249, 'afterFilteringSize': 249, 'afterRelinkingSize': 249, 'id': '4CjGrRGLysTkB2sECV570E', 'type': 'TRACK', 'href': 'https://api.spotify.com/v1/tracks/4CjGrRGLysTkB2sECV570E'}]}

        mock_recomendaciones= mock_recomendaciones_patcher.start()
        mock_recomendaciones.return_value = res

        response = getRecomendaciones('')

        mock_recomendaciones_patcher.stop()

        aux=[cancion('7BYQUH8RD2mPoXjZEawyjy','Outsider','Blanco White','https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65%27','https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a')]

        self.assertIs(response[0].id, aux[0].id)

class test_Library(unittest.TestCase):

    def test_Library(self):

        mock_Library_patcher = patch('musicrpy.sp.current_user_saved_tracks')
        res = {'href': '', 'items': [{'added_at': '', 'track': {'album': {'album_type': '', 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': 'artist', 'uri': ''}], 'available_markets': [], 'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'images': [{'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}], 'name': '', 'release_date': '', 'release_date_precision': '', 'total_tracks': '', 'type': '', 'uri': ''}, 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': '', 'uri': ''}], 'available_markets': [], 'disc_number': '', 'duration_ms': '', 'explicit': '', 'external_ids': {'isrc': ''}, 'external_urls': {'spotify': ''}, 'href': '', 'id': '2Gsare6GuBE2Ph3zJanNKl', 'is_local': '', 'name': '', 'popularity': '', 'preview_url': '', 'track_number': '', 'type': '', 'uri': ''}}], 'limit': '', 'next': '', 'offset': '', 'previous': '', 'total': ''}

        mock_Library= mock_Library_patcher.start()
        mock_Library.return_value = res

        response = addToLibrary('2Gsare6GuBE2Ph3zJanNKl')
        mock_Add_patcher = patch('musicrpy.sp.current_user_saved_tracks_add')
        res = None
        mock_Add= mock_Add_patcher.start()
        mock_Add.return_value = res

        mock_Library_patcher.stop()

        self.assertEqual(response, ('true'))

        mock_Add= mock_Add_patcher.stop()

class test_Library_Fail(unittest.TestCase):

    def test_Library_Fail(self):

        mock_Library_patcher = patch('musicrpy.sp.current_user_saved_tracks')
        res = {'href': '', 'items': [{'added_at': '', 'track': {'album': {'album_type': '', 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': 'artist', 'uri': ''}], 'available_markets': [], 'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'images': [{'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}, {'height': '', 'url': '', 'width': ''}], 'name': '', 'release_date': '', 'release_date_precision': '', 'total_tracks': '', 'type': '', 'uri': ''}, 'artists': [{'external_urls': {'spotify': ''}, 'href': '', 'id': '', 'name': '', 'type': '', 'uri': ''}], 'available_markets': [], 'disc_number': '', 'duration_ms': '', 'explicit': '', 'external_ids': {'isrc': ''}, 'external_urls': {'spotify': ''}, 'href': '', 'id': 'esto es una pueba debe de fallar', 'is_local': '', 'name': '', 'popularity': '', 'preview_url': '', 'track_number': '', 'type': '', 'uri': ''}}], 'limit': '', 'next': '', 'offset': '', 'previous': '', 'total': ''}

        mock_Library= mock_Library_patcher.start()
        mock_Library.return_value = res

        mock_Add_patcher = patch('musicrpy.sp.current_user_saved_tracks_add')
        res = None
        mock_Add= mock_Add_patcher.start()
        mock_Add.return_value = res

        sp.current_user_saved_tracks_add

        response = addToLibrary('debe de fallar')

        mock_Library_patcher.stop()

        self.assertEqual(response, ('false'))

        mock_Add= mock_Add_patcher.stop()

class test_Music(unittest.TestCase):
    @patch('builtins.input', return_value="S")

    def test_Music(self,mock_input):
        mock_getSemillas_patcher = patch('musicrpy.getSemillas')
        res = ['2Gsare6GuBE2Ph3zJanNKl']
        mock_getSemillas= mock_getSemillas_patcher.start()
        mock_getSemillas.return_value = res

        mock_getReco_patcher = patch('musicrpy.getRecomendaciones')
        res2 = [cancion('7BYQUH8RD2mPoXjZEawyjy','Outsider','Blanco White','https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65%27','https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a')]
        mock_getReco= mock_getReco_patcher.start()
        mock_getReco.return_value = res2

        mock_addLib_patcher = patch('musicrpy.addToLibrary')
        res3 = 'true'
        mock_addLib= mock_addLib_patcher.start()
        mock_addLib.return_value = res3

        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        
        mock_getSemillas= mock_getSemillas_patcher.stop()
        mock_getReco= mock_getReco_patcher.stop()
        mock_addLib= mock_addLib_patcher.stop()

class test_Music_N(unittest.TestCase):
    @patch('builtins.input', return_value="N")

    def test_Music(self,mock_input):
        mock_getSemillas_patcher = patch('musicrpy.getSemillas')
        res = ['2Gsare6GuBE2Ph3zJanNKl']
        mock_getSemillas= mock_getSemillas_patcher.start()
        mock_getSemillas.return_value = res

        mock_getReco_patcher = patch('musicrpy.getRecomendaciones')
        res2 = [cancion('7BYQUH8RD2mPoXjZEawyjy','Outsider','Blanco White','https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65%27','https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a')]
        mock_getReco= mock_getReco_patcher.start()
        mock_getReco.return_value = res2

        mock_addLib_patcher = patch('musicrpy.addToLibrary')
        res3 = 'true'
        mock_addLib= mock_addLib_patcher.start()
        mock_addLib.return_value = res3

        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        
        mock_getSemillas= mock_getSemillas_patcher.stop()
        mock_getReco= mock_getReco_patcher.stop()
        mock_addLib= mock_addLib_patcher.stop()

class test_Music_E(unittest.TestCase):
    @patch('builtins.input', return_value="E")

    def test_Music(self,mock_input):
        mock_getSemillas_patcher = patch('musicrpy.getSemillas')
        res = ['2Gsare6GuBE2Ph3zJanNKl']
        mock_getSemillas= mock_getSemillas_patcher.start()
        mock_getSemillas.return_value = res

        mock_getReco_patcher = patch('musicrpy.getRecomendaciones')
        res2 = [cancion('7BYQUH8RD2mPoXjZEawyjy','Outsider','Blanco White','https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65%27','https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a')]
        mock_getReco= mock_getReco_patcher.start()
        mock_getReco.return_value = res2

        mock_addLib_patcher = patch('musicrpy.addToLibrary')
        res3 = 'true'
        mock_addLib= mock_addLib_patcher.start()
        mock_addLib.return_value = res3

        self.assertRaises(musicr())
        
        mock_getSemillas= mock_getSemillas_patcher.stop()
        mock_getReco= mock_getReco_patcher.stop()
        mock_addLib= mock_addLib_patcher.stop()




if __name__ == "__main__":
    unittest.main()