import unittest

# This is the class we want to test. So, we need to import it
import lab2_15
import filecmp

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    def create_users(self):
        users = []
        users.append(lab2_15.User("Juan Stenner", "Paseos del Sol", "33-33-33-33-33", "juan.stenner@oracle.com"))
        users.append(lab2_15.User("Esther Rivas", "Zapopan", "44-44-44-44-44", "esther.rivas@hotmail.com"))
        users.append(lab2_15.User("Francisco Corral", "Ciudad del Sol", "11-11-11-11-11", "francisco.corral@hotmail.com"))
        users.append(lab2_15.User("Guido Python", "Guido Address", "22-22-22-22-22", "guido.python@yahoo.com"))
        return users

    def test_create_record(self):
        directory_obj = lab2_15.Directory([])
        len_before = len(directory_obj.records)
        directory_obj.create_record(Test.create_users(self)[0])
        len_after = len(directory_obj.records)
        self.assertTrue(len_after > len_before)

    def test_save_to_file_same_info(self):
        f1 = "test1.txt"
        f2 = "test2.txt"
        # populate directory
        directory_obj = lab2_15.Directory(Test.create_users(self))
        directory_obj.save_records_to_file(f1)
        directory_obj.save_records_to_file(f2)
        self.assertTrue(filecmp.cmp(f1, f2))

    def test_save_to_file_diff_info(self):
        f1 = "test1.txt"
        f2 = "test2.txt"
        users = Test.create_users(self)
        directory_obj = lab2_15.Directory(users[0:3])
        directory_obj.save_records_to_file(f1)
        directory_obj.create_record(users[3])
        directory_obj.save_records_to_file(f2)
        self.assertFalse(filecmp.cmp(f1, f2))

    def test_search_record_mult_types(self):
        params = ["32", 25, 32, True, None, "esther.rivas@hotmail.com", "Juan Stenner"]
        directory_obj = lab2_15.Directory(Test.create_users(self))
        for to_search in params:
            match = directory_obj.search_record(to_search)
            if match not in [None]:
                self.assertIn(to_search, [getattr(match, "name"), getattr(match, "email")])
            else:
                self.assertTrue(match == None)

    def test_load_records_from_file(self):
        f1 = 'records_to_load.txt'
        directory_obj = lab2_15.Directory(Test.create_users(self))
        directory_obj.save_records_to_file(f1)
        str_from_file = directory_obj.load_records_from_file(f1)
        self.assertNotEqual(None, str_from_file)

    def test_load_records_from_not_found_file(self):
        directory_obj = lab2_15.Directory(Test.create_users(self))
        str_from_file = directory_obj.load_records_from_file('hi')
        self.assertEqual(None, str_from_file)
