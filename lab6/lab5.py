"""!@brief Course: TC4002 Analysis, Design and Construction of Software Systems

Enrollment: A00354823

Author: Juan Francisco Corral Stenner
"""
import csv
from datetime import datetime
from pathlib import Path


class Sort:
    """!@brief
    A Class that will implement different sorting methods in order to analyze their performance.
    The used sorting algorithms are:
     - Bubble sort
     - Heap sort
     - Merge sort
     - Quick sort
    """
    def __init__(self):
        """!@brief Creates a new Sort object.

        This Sort Object is being used to store the data related to the performance of the sorting algorithm
        @param self The object pointer.
        """
        ## A list to store unsorted items.
        self.unordered = []
        ## A list to store sorted items.
        self.ordered = []
        ## Used to store the number of records to sort.
        self.list_len = ""
        ## datetime object to store the start date.
        self.start_time = datetime.now()
        ## datetime object to store the end date.
        self.end_time = datetime.now()
        ## String to store the name of the used algorithm.
        self.algorithm = ""

    def set_input_data(self, file_path):
        """!@brief Reads the input from a file

        Reads input data from a file and returns the content of it in list format
        @param self The object pointer.
        @param file_path The path of the file to use as input
        @retval unordered a list representing the input data
        """
        file = Path(file_path)
        if not file.is_file():
            raise ValueError("Could not find " + file_path)
        with open(file_path, newline='') as file_obj:
            reader = csv.reader(file_obj, delimiter=',', lineterminator='\n')
            for row in reader:
                row = list(filter(None, row))
                self.unordered.append(row)
        return self.unordered

    def set_output_data(self, file_path):
        """!@brief Writes the data of a list into a file

        Reads the data related to the performance of a sorting algorithm stored in a list and writes its content to a
        file
        @param self The object pointer.
        @param file_path The path of the file to use as output
        """
        try:
            with open(file_path, 'w') as file_obj:
                writer = csv.writer(file_obj, delimiter=',', lineterminator='\n')
                for row in self.ordered:
                    writer.writerow(row)
        except PermissionError:
            raise PermissionError("Could not write " + file_path)

    def execute_bubble_sort(self, the_list):
        """!@brief Sorts a list of elements using the bubble sort algorithm.

        Takes a list of elements (can be any type) and returns the same list ordered in a lexicographically ascending
        form using the bubble sort algorithm.
        @param self The object pointer.
        @param the_list A list of elements to be sorted.
        @retval the_list A lexicographically ascending ordered list.
        @par Example:

            >>> import lab5
            >>> sort_obj = lab5.Sort()
            >>> unsorted_list = [10, 8, 5, 3, 7]
            >>> sorted_list = sort_obj.execute_bubble_sort(unsorted_list)
            >>> sorted_list
            [3, 5, 7, 8, 10]
        """
        flag = True
        while flag:
            flag = False
            for idx in range(len(the_list) - 1):
                if the_list[idx] > the_list[idx + 1]:
                    the_list[idx], the_list[idx + 1] = the_list[idx + 1], the_list[idx]
                    flag = True
        return the_list

    def merge(self, left_list, right_list):
        """!@brief Helper function for execute_merge_sort() function.

        Takes two arrays which it will try to merge recursively. It will divide the lists and order its elements until
        the sub-lists reach the length of an unit
        @param self The object pointer.
        @param left_list A list of elements representing the left side of the list.
        @param right_list A list of elements representing the right side of the list.
        @retval sorted_list A lexicographically ascending ordered list.
        """
        sorted_list = []
        left_list_index = right_list_index = 0
        left_list_length, right_list_length = len(left_list), len(right_list)
        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
        return sorted_list

    def execute_merge_sort(self, the_list):
        """!@brief Sorts a list of elements using the merge sort algorithm.

        Takes a list of elements (can be any type) and returns the result of executing its helper function merge(),
        which actually will be a NEW list ordered in lexicographically ascending form using the merge sort algorithm.
        @param self The object pointer.
        @param the_list A list of elements to be sorted.
        @return The result of executing merge().
        @par Example:

            >>> import lab5
            >>> sort_obj = lab5.Sort()
            >>> unsorted_list = [10, 8, 5, 3, 7]
            >>> sorted_list = sort_obj.execute_merge_sort(unsorted_list)
            >>> sorted_list
            [3, 5, 7, 8, 10]
        """
        if len(the_list) <= 1:
            return the_list
        mid = len(the_list) // 2
        left_list = self.execute_merge_sort(the_list[:mid])
        right_list = self.execute_merge_sort(the_list[mid:])
        return self.merge(left_list, right_list)

    def heapify(self, the_list, heap_size, root_index):
        """!@brief Helper function for the execute_heap_sort() function.

        It will call it self recursively turning the list to a binary tree (heap).
        @param self The object pointer.
        @param the_list A list of elements to be sorted.
        @param heap_size The size of the heap
        @param root_index The root index
        """
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        if left_child < heap_size and the_list[left_child] > the_list[largest]:
            largest = left_child
        if right_child < heap_size and the_list[right_child] > the_list[largest]:
            largest = right_child
        if largest != root_index:
            the_list[root_index], the_list[largest] = the_list[largest], the_list[root_index]
            self.heapify(the_list, heap_size, largest)

    def execute_heap_sort(self, the_list):
        """!@brief Sorts a list of elements using the heap sort algorithm.

        Takes a list of elements (can be any type) and returns the same list ordered in a lexicographically ascending
        form using the heap sort algorithm.
        @param self The object pointer.
        @param the_list A list of elements to be sorted.
        @retval the_list A lexicographically ascending ordered list.
        @par Example:

            >>> import lab5
            >>> sort_obj = lab5.Sort()
            >>> unsorted_list = [10, 8, 5, 3, 7]
            >>> sorted_list = sort_obj.execute_heap_sort(unsorted_list)
            >>> sorted_list
            [3, 5, 7, 8, 10]
        """
        n = len(the_list)
        for i in range(n, -1, -1):
            self.heapify(the_list, n, i)
        for i in range(n - 1, 0, -1):
            the_list[i], the_list[0] = the_list[0], the_list[i]
            self.heapify(the_list, i, 0)
        return the_list

    def partition(self, the_list, low, high):
        """!@brief Helper function for the execute_quick_sort() function.

        Creates a pivot and swaps the elements at the right and at the left of it leaving the ones with great value at
        the right and the ones with lower value to the left of the pivot
        @param self The object pointer.
        @param the_list A list of elements to sorted.
        @param low helper variable to determine the pivot
        @param high helper variable to determine the pivot
        """
        pivot = the_list[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while the_list[i] < pivot:
                i += 1
            j -= 1
            while the_list[j] > pivot:
                j -= 1
            if i >= j:
                return j
            the_list[i], the_list[j] = the_list[j], the_list[i]

    def execute_quick_sort(self, the_list):
        """!@brief Sorts a list of elements using the quick sort algorithm.

        Takes a list of elements (can be any type) and returns the same list ordered in lexicographically ascending
        form using the quick sort algorithm.
        @param self The object pointer.
        @param the_list A list of elements to be sorted.
        @retval the_list A lexicographically ascending ordered list.
        @par Example

            >>> import lab5
            >>> sort_obj = lab5.Sort()
            >>> unsorted_list = [10, 8, 5, 3, 7]
            >>> sorted_list = sort_obj.execute_quick_sort(unsorted_list)
            >>> sorted_list
            [3, 5, 7, 8, 10]
        """
        def quick_sort(items, low, high):
            if low < high:
                split_index = self.partition(items, low, high)
                quick_sort(items, low, split_index)
                quick_sort(items, split_index + 1, high)
        quick_sort(the_list, 0, len(the_list) - 1)
        return the_list

    def get_performance_data(self, list_len, ini, end, algorithm):
        """!@brief Generates a list containing data related to the performance of an sorting algorithm

        Takes the start time and end time, computes the consumed time, then returns a list containing:
        [algorithm, number_of_records, time_consumed, start_time, end_time]
        @param self The object pointer.
        @param list_len number of records to be sorted
        @param ini datetime object representing the start date
        @param end datetime object representing the end date
        @param algorithm the name of the sorting algoritmh used
        @retval stats A list containing [algorithm, number_of_records, time_consumed, start_time, end_time]
        """
        stats = [algorithm,
                 str(list_len),
                 str(end - ini),
                 ini.strftime('%d/%b/%Y %H:%M:%S'),
                 end.strftime('%d/%b/%Y %H:%M:%S'),
                 ]
        return stats

    def print_stats(self, stats):
        """!@brief Prints out data regarding the performance of a certain sorting algorithm.

        Takes the a list of strings representing the data associated to a sorting execution of a certain algorithm and
        prints it to console
        @param self The object pointer.
        @param stats A list containing [algorithm, number_of_records, time_consumed, start_time, end_time]
        @par Example:

            >>> sort_obj.print_stats(stats)
            =============quick Sort=============
            Num of records: 5036
            Consumed time:  0:00:00.057844
            Start time:     25/Mar/2020 21:07:22
            End time:       25/Mar/2020 21:07:22
      """
        output = ("{0:=^36}\n{1:>15}{2}\n {3:>15}{4}\n {5:>15}{6}\n {7:>15}{8}\n".format(
            stats[0],
            "Num of records: ", stats[1],
            "Consumed time: ", stats[2],
            "Start time: ", stats[3],
            "End time: ", stats[4],
        ))
        print(output)
