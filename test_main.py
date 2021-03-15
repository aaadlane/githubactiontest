import unittest
import os

class Test_file(unittest.TestCase):
     

    #Test que le fichier exist
    def test_check_file_exist_main.py(self):
        directory_path = './main.py' # somepath
        self.assertTrue(os.path.exists(directory_path)) 
    
    

if __name__ == '__main__':
    #Verbosity indique le nombre d'info que va retourner l'execution
    #de mes tests
    unittest.main(verbosity=2)