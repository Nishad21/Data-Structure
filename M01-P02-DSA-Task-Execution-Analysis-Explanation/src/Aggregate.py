from src.LinkedList import LinkedList
"""
Aggregate class is responsible for implementing various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""

class Aggregate:

    # Initializing linked list object for various operations
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list

    # Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):
        execute_time = self.linked_list.head
        task_id = []
        min_task = []

        while execute_time:
            task_id.append(execute_time.task_id)
            min_task.append(execute_time.end_time - execute_time.start_time)
            execute_time = execute_time.next
        min_task_time = min(min_task)
        index = min_task.index(min_task_time)
        return task_id[index], min_task_time

    # Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        execute_time = self.linked_list.head
        task_id = []
        max_task = []

        while execute_time:
            task_id.append(execute_time.task_id)
            max_task.append(execute_time.end_time - execute_time.start_time)
            execute_time = execute_time.next

        max_task_time = max(max_task)
        index = max_task.index(max_task_time)
        return task_id[index], max_task_time

    # Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        execute_time = self.linked_list.head
        task_id = []
        avg_task = []

        while execute_time:
            task_id.append(execute_time.task_id)
            avg_task.append(execute_time.end_time - execute_time.start_time)
            execute_time = execute_time.next
        average = float(sum(avg_task) // 20)

        sum_task_times = sum(avg_task)

        no_of_nodes = len(task_id)
        return average, sum_task_times, no_of_nodes



