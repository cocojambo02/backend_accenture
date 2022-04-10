class PacientRepository:
    def __init__(self):
        self.pacient_list = []

    def get_pacient(self):
        return self.pacient_list[0]

    def save(self, pacient):
        self.pacient_list.append(pacient.to_df())

    def empty(self):
        self.pacient_list.clear()