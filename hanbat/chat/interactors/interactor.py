from hanbat.chat.repositories.repository import \
    StudentRepository, \
    DomitoryRepository, \
    StaffRepository


class StudentInteractor:
    def __init__(self):
        self.repository = StudentRepository()


class DomitoryInteractor:
    def __init__(self):
        self.repository = DomitoryRepository()


class StaffInteractor:
    def __init__(self):
        self.repository = StaffRepository()


class StudentGetMenuInteractor(StudentInteractor):
    def execute(self, **kwargs):
        return self.repository.get_menu(**kwargs)


class DomitoryGetMenuInteractor(DomitoryInteractor):
    def execute(self, **kwargs):
        return self.repository.get_menu(**kwargs)


class StaffGetMenuInteractor(StaffInteractor):
    def execute(self, **kwargs):
        return self.repository.get_menu(**kwargs)