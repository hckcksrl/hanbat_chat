from hanbat.chat.repositories.repository import \
    StudentRepository, \
    DomitoryRepository, \
    StaffRepository
import datetime


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
        day = kwargs['userRequest']['utterance']
        day_list = ['월', '화', '수', '목', '금']
        if day in day_list:
            return self.repository.get_menu(day=day)

        today_id = datetime.datetime.today().weekday()
        if today_id > 4 :
            return None
        today = day_list[today_id]
        return self.repository.get_menu(day=today)