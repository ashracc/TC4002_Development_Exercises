import unittest

# This is the class we want to test. So, we need to import it
import lab3_20
import filecmp

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    def create_users(self):
        users = []
        users.append(lab3_20.User("Juan Stenner", "juan.stenner@gmail.com", "32", "MX"))
        users.append(lab3_20.User("Esther Rivas", "esther.rivas@gmail.com", "32", "MX"))
        users.append(lab3_20.User("Javier Ramos", "javier.ramos@gmail.com", "35", "MX"))
        users.append(lab3_20.User("Ivette Rios", "ivette.rios@gmail.com", "36", "MX"))
        return users

    # test case function to check the add_record function
    def test_0_add_record(self):
        print("=== Start add_record test ===")
        directory_obj = lab3_20.Directory([])
        len_before = len(directory_obj.records)
        directory_obj.add_record(Test.create_users(self)[0])
        len_after = len(directory_obj.records)
        print("   Records before: {0}, records now: {1}".format(len_before, len_after))
        self.assertTrue(len_after > len_before)

    def test_1_del_record(self):
        print("=== Start del_record_test ===")
        # Users to populate
        users = Test.create_users(self)
        # populate directory
        directory_obj = lab3_20.Directory(users)
        print("   The directory has {0} users".format(len(directory_obj.records)))
        for idx in range(len(directory_obj.records)):
            len_before = len(directory_obj.records)
            directory_obj.del_record(0)
            len_after = len(directory_obj.records)
            print("   Records before: {0}, records now: {1}".format(len_before, len_after))
            self.assertTrue(len_after < len_before)

    def test_2_del_record_when_empty(self):
        print("=== Start del_record_test ===")
        # empty directory
        directory_obj = lab3_20.Directory([])
        print("   The directory has {0} users".format(len(directory_obj.records)))
        self.assertRaises(IndexError, directory_obj.del_record, 0)

    def test_3_search_record_mult_types(self):
        print("=== Start search_record_test ===")
        # What to search
        params = ["32", 25, 32, True, None, "esther.rivas@gmail.com"]
        # populate directory
        directory_obj = lab3_20.Directory(Test.create_users(self))
        for to_search in params:
            print("   Searching: {0} - type: {1} in age or email".format(to_search, type(to_search)))
            match = directory_obj.search_record(to_search)
            if match not in [None]:
                print("     {0} matched".format(getattr(match, "name")))
                self.assertIn(to_search, [getattr(match, "age"), getattr(match, "email")])
            else:
                print("     No such user")
                self.assertTrue(match == None)

    def test_4_save_to_file_same_info(self):
        print("=== Start save_to_file_same_info test ===")
        f1 = "test1.txt"
        f2 = "test2.txt"
        # populate directory
        print("   Populating records")
        directory_obj = lab3_20.Directory(Test.create_users(self))
        print("   Saving to", f1)
        directory_obj.save_to_file(f1)
        print("   Saving to", f2)
        directory_obj.save_to_file(f2)
        print("   Comparing {0} vs {1}".format(f1, f2))
        self.assertTrue(filecmp.cmp(f1, f2))

    def test_5_save_to_file_diff_info(self):
        print("=== Start save_to_file_diff_info test ===")
        f1 = "test1.txt"
        f2 = "test2.txt"
        users = Test.create_users(self)
        # populate directory
        print("   Populating records")
        directory_obj = lab3_20.Directory(users[0:3])
        print("   Saving to", f1)
        directory_obj.save_to_file(f1)
        print("   Adding {0} to the records.".format(getattr(users[3], "name")))
        directory_obj.add_record(users[3])
        print("   Saving to", f2)
        directory_obj.save_to_file(f2)
        print("   Comparing {0} vs {1}".format(f1, f2))
        self.assertFalse(filecmp.cmp(f1, f2))

    def test_6_cmp_file_vs_temp(self):
        print("=== Start cmp_file_vs_temp test ===")
        f1 = "test1.txt"
        users = Test.create_users(self)
        # populate directory
        print("   Populating records")
        directory_obj = lab3_20.Directory(users[0:3])
        print("   Saving to", f1)
        directory_obj.save_to_file(f1)
        print("   Comparing {0} vs records".format(f1))
        self.assertEqual(directory_obj.load_records_from_file(f1), directory_obj.get_records())
        print("   Adding {0} to the records.".format(getattr(users[3], "name")))
        directory_obj.add_record(users[3])
        print("   Comparing {0} vs records".format(f1))
        self.assertNotEqual(directory_obj.load_records_from_file(f1), directory_obj.get_records())

# if __name__ == '__main__':
#     # begin the unittest.main()
#     unittest.main()