class PacientRepository:
    def __init__(self):
        self.pacient_list = []

    def save(self, pacient):
        self.pacient_list.append(pacient)

    def empty(self):
        self.pacient_list.clear()