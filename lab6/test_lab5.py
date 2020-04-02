"""!@brief Course: TC4002 Analysis, Design and Construction of Software Systems

Enrollment: A00354823

Author: Juan Francisco Corral Stenner
"""
import unittest
import os
import lab5
from datetime import datetime


class TestLab5(unittest.TestCase):
    """!@brief A Class that will implement different tests to the lab5 module.
    """
    def test_bubble_sort_correctness(self):
        """!@brief Test bubble sort algorithm correctness

        Obtains a list of lists retrieved from "input.csv" file. Then, for each list, it runs an assertEqual test
        between the result of execute_bubble_sort() function and built-in sorted() function.
        @param self The object pointer.
        """
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_bubble_sort(unordered_list), sorted(unordered_list))

    def test_merge_sort_correctness(self):
        """!@brief Test merge sort algorithm correctness

        Obtains a list of lists retrieved from "input.csv" file. Then, for each list, it runs an assertEqual test
        between the result of execute_merge_sort() function and built-in sorted() function.
        @param self The object pointer.
        """
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_merge_sort(unordered_list), sorted(unordered_list))

    def test_heap_sort_correctness(self):
        """!@brief Test heap sort algorithm correctness

        Obtains a list of lists retrieved from "input.csv" file. Then, for each list, it runs an assertEqual test
        between the result of execute_heap_sort() function and built-in sorted() function.
        @param self The object pointer.
        """
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_heap_sort(unordered_list), sorted(unordered_list))

    def test_quick_sort_correctness(self):
        """!@brief Test quick sort algorithm correctness

        Obtains a list of lists retrieved from "input.csv" file. Then, for each list, it runs an assertEqual test
        between the result of execute_quick_sort() function and built-in sorted() function.
        @param self The object pointer.
        """
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            self.assertEqual(sort_obj.execute_heap_sort(unordered_list), sorted(unordered_list))

    def test_performance(self):
        """!@brief Test the performance of various sort algorithms

        Obtains a list of lists retrieved from "input.csv" file. Then, for each list, it executes four different
        sorting algorithms (bubble sort, merge sort, heap sort, quick sort), calls get_performance_data and stores the
        results in "stats". Finally this data is printed out to console using the "print_stats" function.
        @param self The object pointer.
        """
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
        """!@brief Test the the correctness of various sort algorithms

        Obtains a list of lists retrieved from "input.csv" file. Then, for each list, it executes four different
        sorting algorithms (bubble sort, merge sort, heap sort, quick sort). Using an assertEqual test it compares the
        obtained result vs the built in sorted() function.
        @param self The object pointer.
        """
        sort_obj = lab5.Sort()
        u_lists = sort_obj.set_input_data("input.csv")
        for unordered_list in u_lists:
            for algorithm in ['bubble',
                              'merge',
                              'heap',
                              'quick']:
                function_name = eval('sort_obj.execute_' + algorithm + '_sort')
                self.assertEqual(function_name(unordered_list), sorted(unordered_list))

    def test_able_to_write(self):
        """!@brief Test if its able to write a file

        Obtains a list of lists retrieved from "input.csv" file. For each list, it runs execute_bubble_sort()
        function and store its result in the "ordered" attribute of the class Sort. Then it writes the contents of
        "ordered" into "output.csv". With and assertTrue test, checks if "output.csv" exists and finally, at OS level
        it opens "output.csv".
        @param self The object pointer.
        """
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
        """!@brief Test if the output file is open

        Using an assertRaises test, check if the file "output.csv" is opened and unable to be written.
        @param self The object pointer.
        """
        file_path = "output.csv"
        sort_obj = lab5.Sort()
        self.assertRaises(PermissionError, sort_obj.set_output_data, file_path)

    def test_file_not_found(self):
        """!@brief Test the existences of a file

        Tries to open a file named: "file.csv" if it doesn't exist will raise a ValuerError error. This will be
        checked using an assertRaises test.
        @param self The object pointer.
        """
        file_path = "file.csv"
        sort_obj = lab5.Sort()
        self.assertRaises(ValueError, sort_obj.set_input_data, file_path)