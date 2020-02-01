from hanbat.chat.repositories.repository import \
    StudentRepository, \
    DomitoryRepository, \
    StaffRepository
import datetime


class StudentInteractor:
    def __init__(self):
        self.repository = StudentRepository()
        self.result = {
            "version": "2.0",
            "data": {
                "location": '학생식당',
                "menu": ""
            }
        }


class DomitoryInteractor:
    def __init__(self):
        self.repository = DomitoryRepository()
        self.result = {
            "version": "2.0",
            "data": {
                "location": '기숙사식당',
                "menu": ""
            }
        }


class StaffInteractor:
    def __init__(self):
        self.repository = StaffRepository()
        self.result = {
            "version": "2.0",
            "data": {
                "location": '교직원식당',
                "menu": ""
            }
        }


class StudentGetMenuInteractor(StudentInteractor):
    def execute(self, **kwargs):
        return self.repository.get_menu(**kwargs)


class DomitoryGetMenuInteractor(DomitoryInteractor):
    def execute(self, **kwargs):
        return self.repository.get_menu(**kwargs)


class StaffGetMenuInteractor(StaffInteractor):
    def execute(self, data: dict):
        result = self.result
        day = data['userRequest']['utterance']
        day_list = ['월', '화', '수', '목', '금']

        if day in day_list:
            menus = self.repository.get_menu(day=day)
            for menu in menus:
                result['data']['menu'] = result['data']['menu'] + f'{menu.time}\n{menu.menu}\n\n'
            return result

        today_id = datetime.datetime.today().weekday()

        if today_id > 4:
            result['data']['menu'] = '운영 안함'
            return result

        today = day_list[today_id]
        menus = self.repository.get_menu(day=day)
        for menu in menus:
            result['data']['menu'] = result['data']['menu'] + f'{menu.time}\n{menu.menu}\n\n'
        return result
