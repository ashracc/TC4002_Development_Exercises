import unittest
import os
import lab5
from datetime import datetime


class TestLab5(unittest.TestCase):
    def test_bubble_sort_correctness(self):
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_bubble_sort(unordered_list), sorted(unordered_list))

    def test_merge_sort_correctness(self):
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_merge_sort(unordered_list), sorted(unordered_list))

    def test_heap_sort_correctness(self):
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_heap_sort(unordered_list), sorted(unordered_list))

    def test_quick_sort_correctness(self):
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_heap_sort(unordered_list), sorted(unordered_list))

    def test_performance(self):
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for algorithm in ['bubble',
                          'merge',
                          'heap',
                          'quick']:
            function_name = eval('sort_obj.execute_' + algorithm + '_sort')
            sort_obj.list_len = len(u_lists[19])
            sort_obj.start_time = datetime.now()
            sort_obj.ordered.append(function_name(u_lists[19]))
            sort_obj.end_time = datetime.now()
            sort_obj.algorithm = algorithm + " Sort"
            stats = sort_obj.get_performance_data(sort_obj.list_len, sort_obj.start_time, sort_obj.end_time,
                                                  sort_obj.algorithm)
            sort_obj.print_stats(stats)

    def test_try_to_break(self):
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for x in u_lists[0:len(u_lists) - 2]:
            for algorithm in ['bubble',
                              'merge',
                              'heap',
                              'quick']:
                function_name = eval('sort_obj.execute_' + algorithm + '_sort')
                sort_obj.ordered.append(function_name(x))

    def test_able_to_write(self):
        sort_obj = lab5.Sort()
        in_File = "input.csv"
        out_file = "output.csv"
        u_lists = sort_obj.set_input_data(in_File)
        for unordered_list in u_lists:
            sort_obj.ordered.append(sort_obj.execute_bubble_sort(unordered_list))
        sort_obj.set_output_data(out_file)
        self.assertTrue(os.path.isfile(out_file))
        os.startfile(out_file)

    def test_opened_file(self):
        file_path = "output.csv"
        sort_obj = lab5.Sort()
        self.assertRaises(PermissionError, sort_obj.set_output_data, file_path)

    def test_file_not_found(self):
        file_path = "file.csv"
        sort_obj = lab5.Sort()
        self.assertRaises(ValueError, sort_obj.set_input_data, file_path)