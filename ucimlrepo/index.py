import unittest
from ucimlrepo import fetch_ucirepo, list_available_datasets

class TestMLRepo(unittest.TestCase):
    """Tests for the main fetch functionality"""
    
    def test_fetch_with_both_id_and_name_raises_error(self):
        """Should raise ValueError when both id and name are provided"""
        with self.assertRaises(ValueError):
            fetch_ucirepo(id=1, name='Abalone')

    def test_fetch_with_no_arguments_raises_error(self):
        """Should raise ValueError when no arguments are provided"""
        with self.assertRaises(ValueError):
            fetch_ucirepo()

    def test_fetch_with_invalid_id_type_raises_error(self):
        """Should raise ValueError when id is not an integer"""
        with self.assertRaises(ValueError):
            fetch_ucirepo(id='Abalone')

    def test_fetch_with_invalid_name_type_raises_error(self):
        """Should raise ValueError when name is not a string"""
        with self.assertRaises(ValueError):
            fetch_ucirepo(name=1)

    def test_fetch_nonexistent_id_raises_error(self):
        """Should raise error when dataset ID doesn't exist"""
        with self.assertRaises(Exception):
            fetch_ucirepo(id=999999)  # Use extremely high ID that likely won't exist

    def test_fetch_by_name_success(self):
        """Test successful fetch using dataset name"""
        abalone = fetch_ucirepo(name='Abalone')
        self.assertEqual(abalone.metadata.uci_id, 1)
        self.assertEqual(abalone.metadata.name, 'Abalone')

class TestListDatasets(unittest.TestCase):
    """Tests for the list_available_datasets function"""
    
    def test_list_by_area(self):
        """Test listing datasets by area"""
        result = list_available_datasets(area='health and medicine')
        self.assertIsInstance(result, list)  # Assuming it returns a list

    def test_list_by_filter(self):
        """Test listing datasets by filter"""
        result = list_available_datasets(filter='python')
        self.assertIsInstance(result, list)

    def test_list_by_search(self):
        """Test listing datasets by search term"""
        result = list_available_datasets(search='nino')
        self.assertIsInstance(result, list)

class TestDatasetStructure(unittest.TestCase):
    """Tests for verifying dataset structure"""
    
    def test_heart_disease_structure(self):
        """Test the structure of the heart disease dataset"""
        heart_disease = fetch_ucirepo(id=45)
        
        # Verify metadata
        self.assertEqual(heart_disease.metadata.uci_id, 45)
        self.assertEqual(heart_disease.metadata.repository_url, 
                        'https://archive.ics.uci.edu/dataset/45/heart+disease')

        # Verify data shapes
        self.assertEqual(heart_disease.data.features.shape, (303, 13))
        self.assertEqual(heart_disease.data.targets.shape, (303, 1))

        # Verify variable names
        self.assertEqual(heart_disease.variables['name'][0], 'age')

if __name__ == '__main__':
    unittest.main()