import random, queue, time, threading

class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3,11))

class Cafe():
    def __init__(self, queue, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        pass

    def discuss_guests(self):
        pass

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

# def getter(queue):
#     while True:
#         time.sleep(5)
#         item = queue.get()
#         print(threading.current_thread(), "взят элемент ", item)
#
# q = Queue(maxsize=5)
# t1 = threading.Thread(target=getter, args=(q,), daemon=True)
# t1.start()
#
# for i in range(5):
#     time.sleep(2)
#     q.put(i)
#     print(threading.current_thread(), 'положил в очередь элемент', i)