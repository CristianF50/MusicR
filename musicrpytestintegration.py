from musicrpy import *
import unittest 
from unittest import result, TestCase, mock
from unittest.mock import patch 

class test_Music_integracion(unittest.TestCase):
    @patch('builtins.input', return_value="S")
    def test_Music1(self):
        
        mock_getReco_patcher = patch('musicrpy.getRecomendaciones')
        res2 = [cancion('7BYQUH8RD2mPoXjZEawyjy','Outsider','Blanco White','https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65%27','https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a')]
        mock_getReco= mock_getReco_patcher.start()
        mock_getReco.return_value = res2

        mock_addLib_patcher = patch('musicrpy.addToLibrary')
        res3 = 'true'
        mock_addLib= mock_addLib_patcher.start()
        mock_addLib.return_value = res3


        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        
        mock_getReco= mock_getReco_patcher.stop()
        mock_addLib= mock_addLib_patcher.stop()
    
    def test_Music2(self):
        mock_getSemillas_patcher = patch('musicrpy.getSemillas')
        res = ['2Gsare6GuBE2Ph3zJanNKl']
        mock_getSemillas= mock_getSemillas_patcher.start()
        mock_getSemillas.return_value = res


        mock_addLib_patcher = patch('musicrpy.addToLibrary')
        res3 = 'true'
        mock_addLib= mock_addLib_patcher.start()
        mock_addLib.return_value = res3


        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        
        mock_getSemillas= mock_getSemillas_patcher.stop()

        mock_addLib= mock_addLib_patcher.stop()
    
    def test_Music3(self):
        mock_getSemillas_patcher = patch('musicrpy.getSemillas')
        res = ['2Gsare6GuBE2Ph3zJanNKl']
        mock_getSemillas= mock_getSemillas_patcher.start()
        mock_getSemillas.return_value = res

        mock_getReco_patcher = patch('musicrpy.getRecomendaciones')
        res2 = [cancion('7BYQUH8RD2mPoXjZEawyjy','Outsider','Blanco White','https://i.scdn.co/image/ab67616d0000b273f1e82d635519bf864c452a65%27','https://p.scdn.co/mp3-preview/78530e35146097b2ab3a9f723373fcffe2472669?cid=c176bd9d61984d3f8c4804b03245467a')]
        mock_getReco= mock_getReco_patcher.start()
        mock_getReco.return_value = res2


        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        
        mock_getSemillas= mock_getSemillas_patcher.stop()
        mock_getReco= mock_getReco_patcher.stop()
    
    def test_Music4(self):
        mock_getSemillas_patcher = patch('musicrpy.getSemillas')
        res = ['2Gsare6GuBE2Ph3zJanNKl']
        mock_getSemillas= mock_getSemillas_patcher.start()
        mock_getSemillas.return_value = res


        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        
        mock_getSemillas= mock_getSemillas_patcher.stop()

    def test_Music5(self):

        mock_addLib_patcher = patch('musicrpy.addToLibrary')
        res3 = 'true'
        mock_addLib= mock_addLib_patcher.start()
        mock_addLib.return_value = res3

        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))
        

        mock_addLib= mock_addLib_patcher.stop()
    
    def test_Music6(self):
        self.assertEqual(musicr(),("La cancion que te recomendamos es: ", 'Outsider', " by ",'Blanco White'))


if __name__ == "__main__":
    unittest.main()