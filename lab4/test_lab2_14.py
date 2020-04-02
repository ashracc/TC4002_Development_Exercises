import unittest
import lab2_14
import os

class TestLab2_14(unittest.TestCase):
    def test_add_item(self):
        my_power_list_obj = lab2_14.myPowerList([])
        len_before = len(my_power_list_obj.items)
        my_power_list_obj.add_item(1)
        len_after = len(my_power_list_obj.items)
        self.assertTrue(len_after > len_before)

    def test_remove_item(self):
        my_power_list_obj = lab2_14.myPowerList([])
        my_power_list_obj.add_item(1)
        len_before = len(my_power_list_obj.items)
        my_power_list_obj.remove_item(0)
        len_after = len(my_power_list_obj.items)
        self.assertTrue(len_after < len_before)

    def test_remove_item_list_empty(self):
        my_power_list_obj = lab2_14.myPowerList([])
        self.assertRaises(IndexError, my_power_list_obj.remove_item, 0)

    def test_bubble_sort_int(self):
        my_power_list_obj = lab2_14.myPowerList([1, 2, 35, 6, 42, 325, 43, 2, 3])
        res = my_power_list_obj.bubble_sort()
        for x in range(len(res) - 1):
            self.assertTrue(res[x] <= res[x + 1])

    def test_bubble_sort_float(self):
        my_power_list_obj = lab2_14.myPowerList([1.3, 2.2, 3.5, 65.0, 4.2, 3.25, 43.3, 2, 3.0])
        res = my_power_list_obj.bubble_sort()
        for x in range(len(res) - 1):
            self.assertTrue(res[x] <= res[x + 1])

    def test_bubble_sort_string(self):
        my_power_list_obj = lab2_14.myPowerList(['1','2','3', '5', '6', '42'])
        res = my_power_list_obj.bubble_sort()
        for x in range(len(res) - 1):
            self.assertTrue(res[x] <= res[x + 1])

    def test_bubble_sort_bool(self):
        my_power_list_obj = lab2_14.myPowerList([True, False, False, True, True])
        res = my_power_list_obj.bubble_sort()
        for x in range(len(res) - 1):
            self.assertTrue(res[x] <= res[x + 1])

    def test_left_merge(self):
        my_list = ['-','-','-']
        list_to_merge = ['L','L','L']
        my_power_list_obj = lab2_14.myPowerList(my_list)
        left_merged_list = my_power_list_obj.left_merge(list_to_merge)
        self.assertListEqual(left_merged_list, list_to_merge + my_list)

    def test_right_merge(self):
        my_list = ['-','-','-']
        list_to_merge = ['L','L','L']
        my_power_list_obj = lab2_14.myPowerList(my_list)
        left_merged_list = my_power_list_obj.right_merge(list_to_merge)
        self.assertListEqual(left_merged_list, my_list + list_to_merge)

    def test_readFromTextFile(self):
        f1 = 'testing_save_to_file.txt'
        data = ['1','2','3', '5', '6', '42']
        my_power_list_obj = lab2_14.myPowerList(data)
        my_power_list_obj.saveToTextFile(f1)
        str_from_data = '\n'.join(data) + '\n'
        str_from_file = my_power_list_obj.readFromTextFile(f1)
        self.assertEqual(str_from_data, str_from_file)

    def test_read_unexisting_file(self):
        my_power_list_obj = lab2_14.myPowerList([])
        self.assertRaises(FileNotFoundError,my_power_list_obj.readFromTextFile, '---.txt')

    def test_saveToTextFile(self):
        pass