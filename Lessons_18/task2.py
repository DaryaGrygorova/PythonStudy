"""Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that
allows you to add workers to a Boss. You're not allowed to add instances of
Boss class to workers list directly via access to attribute, use getters and setters instead!
You can refactor the existing code.
id_ - is just a random unique integer
"""


class Boss:
    """Create boss object that include list of workers"""

    __id = 1

    def __init__(self, name: str, company: str):
        self.id = Boss.__id
        self.name = name
        self.company = company
        self._workers = []
        Boss.__id += 1

    def add_worker(self, worker):
        """Add new worker to the list of workers"""
        if worker not in self._workers:
            self._workers.append(worker)
        else:
            raise ValueError("This worker already in the list!")

    def remove_workers(self, worker):
        """Remove worker from the list of workers"""
        if worker in self._workers:
            self._workers.remove(worker)
        else:
            raise ValueError("This worker not found in the list!")

    def get_workers(self):
        """Return list of workers"""
        return self._workers

    def __str__(self):
        return f"{self.name}"


class Worker:
    """Create worker object"""

    __id = 1

    def __init__(self, name: str, boss: Boss):
        self.id = Worker.__id
        self.name = name
        self.company = None
        self._boss = None
        self.boss = boss
        Worker.__id += 1

    def __str__(self):
        return f"{self.name}: id: {self.id}, company: {self.company}, boss: {self.boss}"

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"

    @property
    def boss(self):
        """Return boss for worker instance"""
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        """Set worker's boss and set list of workers in boss instance"""
        if isinstance(new_boss, Boss):
            if self.boss is not None:
                self._boss.remove_workers(self)
            self._boss = new_boss
            new_boss.add_worker(self)
            self.company = new_boss.company
        else:
            raise ValueError("Boss not class Boss instance!")

    def set_boss(self, new_boss):
        """Set current boss in worker object"""
        self.boss = new_boss


boss_1 = Boss("Hugo", "Hugo Boss AG")
boss_2 = Boss("Serge", "Sergio Cotti")

worker_1 = Worker("Geralt", boss_1)
worker_2 = Worker("Lutik", boss_2)
worker_3 = Worker("Andrzej", boss_2)

print("All workers:")
print(worker_1)
print(worker_2)
print(worker_3)
print("Workers by boss:")
print(f"{boss_1.name} workers:", boss_1.get_workers())
print(f"{boss_2.name} workers:", boss_2.get_workers())

worker_2.set_boss(boss_1)
print("\nLutik change the work: ")
print(worker_2)
print("Workers by boss:")
print(f"{boss_1.name} workers:", boss_1.get_workers())
print(f"{boss_2.name} workers:", boss_2.get_workers())
