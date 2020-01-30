from dataclasses import dataclass


@dataclass
class StudentEntity:
    id: int = None
    menu: str = None
    price: str = None


@dataclass
class DomitoryEntity:
    id: int = None
    menu: str = None
    time: str = None


@dataclass
class StaffEntity:
    id: int = None
    menu: str = None
    time: str = None