import abc
from typing import List
from hanbat.chat.models.models import \
    StudentKinds, \
    StudentMenu, \
    DomitoryDays, \
    DomitoryMenu, \
    StaffDays, \
    StaffMenu
from hanbat.chat.entities.entity import \
    StaffEntity, \
    StudentEntity, \
    DomitoryEntity


class StudentABCRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_menu(self, kinds: str):
        pass


class DomitoryABCRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_menu(self, kinds: str):
        pass


class StaffABCRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_menu(self, kinds: str):
        pass


class StudentRepository(StudentABCRepository):
    def get_menu(self, kinds: str) -> List[StudentEntity]:
        kinds_id = StudentKinds.objects.get(kinds=kinds)
        menus = StudentMenu.objects.filter(kinds=kinds_id)
        menu_entities = []

        for menu in menus:
            menu_entities.append(menu.to_entity())

        return menu_entities


class DomitoryRepository(DomitoryABCRepository):
    def get_menu(self, day: str) -> List[DomitoryEntity]:
        day_id = DomitoryDays.objects.get(day=day)
        menus = DomitoryMenu.objects.filter(day=day_id)
        menu_entities = []

        for menu in menus:
            menu_entities.append(menu.to_entity())

        return menu_entities


class StaffRepository(StaffABCRepository):
    def get_menu(self, day: str) -> List[StaffEntity]:
        day_id = StaffDays.objects.get(day=day)
        menus = StaffMenu.objects.filter(day=day_id)
        menu_entities = []

        for menu in menus:
            menu_entities.append(menu.to_entity())

        return menu_entities
