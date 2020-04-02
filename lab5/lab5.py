import csv
from datetime import datetime
from pathlib import Path


class Sort:
    def __init__(self):
        self.unordered = []
        self.ordered = []
        self.list_len = ""
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.algorithm = ""

    def set_input_data(self, file_path):
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
        try:
            with open(file_path, 'w') as file_obj:
                writer = csv.writer(file_obj, delimiter=',', lineterminator='\n')
                for row in self.ordered:
                    writer.writerow(row)
        except PermissionError:
            raise PermissionError("Could not write " + file_path)

    def execute_bubble_sort(self, the_list):
        flag = True
        while flag:
            flag = False
            for idx in range(len(the_list) - 1):
                if the_list[idx] > the_list[idx + 1]:
                    the_list[idx], the_list[idx + 1] = the_list[idx + 1], the_list[idx]
                    flag = True
        return the_list

    def merge(self, left_list, right_list):
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
        if len(the_list) <= 1:
            return the_list
        mid = len(the_list) // 2
        left_list = self.execute_merge_sort(the_list[:mid])
        right_list = self.execute_merge_sort(the_list[mid:])
        return self.merge(left_list, right_list)

    def heapify(self, the_list, heap_size, root_index):
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
        # print('heapify')

    def execute_heap_sort(self, the_list):
        n = len(the_list)
        for i in range(n, -1, -1):
            self.heapify(the_list, n, i)
        for i in range(n - 1, 0, -1):
            the_list[i], the_list[0] = the_list[0], the_list[i]
            self.heapify(the_list, i, 0)
        return the_list

    def partition(self, the_list, low, high):
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
        def quick_sort(items, low, high):
            if low < high:
                split_index = self.partition(items, low, high)
                quick_sort(items, low, split_index)
                quick_sort(items, split_index + 1, high)
        quick_sort(the_list, 0, len(the_list) - 1)
        return the_list

    def get_performance_data(self, list_len, ini, end, algorithm):
        # This method returns the performance data associated to the last sorting execution
        # [Number of Records Sorted, TimeConsumed, StartTime, EndTime]
        stats = [algorithm,
                 str(list_len),
                 str(end - ini),
                 ini.strftime('%d/%b/%Y %H:%M:%S'),
                 end.strftime('%d/%b/%Y %H:%M:%S'),
                 ]
        return stats

    def print_stats(self, stats):
        output = ("{0:=^36}\n{1:>15}{2}\n {3:>15}{4}\n {5:>15}{6}\n {7:>15}{8}\n".format(
            stats[0],
            "Num of records: ", stats[1],
            "Consumed time: ", stats[2],
            "Start time: ", stats[3],
            "End time: ", stats[4],
        ))
        print(output)

# def main():
#     sort_obj = Sort()
#     aux = sort_obj.set_input_data("input.csv")
#
#     for x in aux:
#         print(x)
#         sort_obj.ordered.append(sort_obj.execute_quick_sort(x))
#
#     for x in sort_obj.ordered:
#         print(x)
#
#     for unordered_list in aux:
#         sort_obj.list_len = len(unordered_list)
#         sort_obj.start_time = datetime.now()
#         sort_obj.bubble_sort(unordered_list)
#         sort_obj.end_time = datetime.now()
#         sort_obj.algorithm = "Bubble Sort"
#         stats = sort_obj.get_performance_data(sort_obj.list_len, sort_obj.start_time, sort_obj.end_time, sort_obj.algorithm)
#         sort_obj.print_stats(stats)
#
# if __name__ == "__main__":
#     main()
