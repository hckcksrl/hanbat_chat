from django.db import models
from hanbat.chat.entities.entity import StudentEntity, DomitoryEntity, StaffEntity


class StudentKinds(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    kinds = models.CharField(max_length=255, default='')


class StudentMenu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    menu = models.TextField(null=True)
    price = models.CharField(null=True, max_length=255, default='')
    kinds = models.ForeignKey('StudentKinds', on_delete=models.CASCADE)

    def to_entity(self) -> StudentEntity:
        return StudentEntity(
            id=self.id,
            menu=self.menu,
            price=self.price
        )

class DomitoryDays(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    day = models.CharField(max_length=255, default='')


class DomitoryMenu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(max_length=255, default='', null=True)
    menu = models.TextField(null=True)
    day = models.ForeignKey('DomitoryDays', on_delete=models.CASCADE)

    def to_entity(self) -> DomitoryEntity:
        return DomitoryEntity(
            id=self.id,
            menu=self.menu,
            time=self.time
        )


class StaffDays(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    day = models.CharField(max_length=255, default='')


class StaffMenu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    time = models.CharField(max_length=255, default='', null=True)
    menu = models.TextField(null=True)
    day = models.ForeignKey('StaffDays', on_delete=models.CASCADE)

    def to_entity(self) -> StaffEntity:
        return StaffEntity(
            id=self.id,
            menu=self.menu,
            time=self.time
        )
