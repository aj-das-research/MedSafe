import unittest
import zipfile
from src.analyzer import MedSafeAnalyzer
import tempfile
import os

class TestMedSafeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = MedSafeAnalyzer()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        self.analyzer.cleanup()
        os.rmdir(self.temp_dir)

    def test_load_from_zip(self):
        # Create a sample zip file
        zip_path = os.path.join(self.temp_dir, 'test.zip')
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            zip_file.writestr('test.py', 'print("Hello, World!")')

        self.analyzer.load_from_zip(zip_path)
        self.assertTrue(os.path.exists('temp_codebase/test.py'))

    def test_analyze(self):
        # Create a sample file with a compliance issue
        os.makedirs('temp_codebase', exist_ok=True)
        with open('temp_codebase/test.py', 'w') as f:
            f.write('import pickle\n')

        self.analyzer.codebase = 'temp_codebase'
        report = self.analyzer.analyze()

        self.assertIn("Use of prohibited module: pickle", report)

if __name__ == '__main__':
    unittest.main()