class Node:
    def __init__(self, task_name : str, duration : int, priority : int):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_task(self, task_name : str, duration : int, priority : int):
        NewTask = Node(task_name, duration, priority)
        if self.tail is None:
            self.head = NewTask
            self.tail = NewTask
            self.size = 1

        else:
            self.tail.next = NewTask
            self.tail = NewTask
            self.size += 1

    def remove_task(self, task_name : str):
        if self.head is None:
            return None
        if self.head.task_name == task_name:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return None

        current  = self.head
        while current.next is not None:
            if current.next.task_name == task_name:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return None
            current = current.next
        return None

    def display_tasks(self):
        current = self.head
        while current is not None:
            print(current.task_name)
            current = current.next

    def find_task(self, task_name : str):
        current = self.head
        while current is not None:
            if current.task_name == task_name:
                return f"Task_Name : {current.task_name}, Duration : {current.duration}, Priority : {current.priority}"
            current = current.next
        return None

    def calculate_total_duration(self):
        dur=0
        current = self.head
        while current is not None:
            dur += current.duration
            current = current.next

        return dur

    def read_tasks_from_csv(self,file_path : str):

        try:
            file = open(file_path, 'r')
        except:
            print("File doesnt exist")
            return None

        file.readline()
        line = file.readline()
        while line != "":
            lijst = line.split(',')
            task_name = lijst[0]
            duration = int(lijst[1])
            priority = int(lijst[2])
            self.add_task(task_name, duration, priority)
            line = file.readline()

        file.close()

    def sorted_insert_by_priority(self, task_name : str, duration : int, priority : int):
        node = Node(task_name, duration, priority)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
            return None

        if node.priority <= self.head.priority:
            node.next = self.head
            self.head = node
            self.size += 1
            return None
        current = self.head
        while current.next is not None:
            if node.priority <= current.next.priority:
                node.next = current.next
                current.next = node
                self.size += 1
                return None
            current = current.next

        self.tail.next = node
        self.tail = node
        self.size += 1


    def reorder_tasks_by_priority(self):
        templist = LinkedList()
        current = self.head
        while current is not None:
            templist.sorted_insert_by_priority(current.task_name, current.duration, current.priority)
            current = current.next

        self.head = templist.head
        self.tail = templist.tail


    def sorted_insert_by_priority_duration(self, task_name : str, duration : int, priority : int):
        node = Node(task_name, duration, priority)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
            return None

        if node.priority < self.head.priority:
            node.next = self.head
            self.head = node
            self.size += 1
            return None
        elif node.priority == self.head.priority:
            if node.duration <= self.head.duration:
                node.next = self.head
                self.head = node
                self.size += 1
                return None

        current = self.head
        while current.next is not None:
            if node.priority <= current.next.priority:
                node.next = current.next
                current.next = node
                self.size += 1
                return None
            elif node.priority == self.head.priority:
                if node.duration <= current.next.duration:
                    node.next = current.next
                    current.next = node
                    self.size += 1
                    return None

            current = current.next

        self.tail.next = node
        self.tail = node
        self.size += 1

    def reorder_tasks_by_priority_duration(self):
        templist = LinkedList()
        current = self.head
        while current is not None:
            templist.sorted_insert_by_priority_duration(current.task_name, current.duration, current.priority)
            current = current.next

        self.head = templist.head
        self.tail = templist.tail


x= LinkedList()
x.read_tasks_from_csv("tasks.csv")
x.reorder_tasks_by_priority_duration()

x.display_tasks()












