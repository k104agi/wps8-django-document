from django.db import models


class Car(models.Model):
    # 제조사가 먼저 있어야 차를 생성할 수 있음
    manufacturer = models.ForeignKey(
        'Manufacturer',
        # 원래 그냥 Manufacturer이고
        # Manufacturer 클래스 먼저 정의하고 아래에 Car가 와야함
        # 하지만 ''를 붙여주면 해당 정의가 아래에 나와도 알아서 찾음(장고기능)
        on_delete=models.CASCADE,
        # DB 상에서 제조사가 사라지면 같이 사라짐
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey(
        # foreignkey이지만 self(자기자신)를 참조함
        'self',
        on_delete=models.SET_NULL,
        # DB상에서 강사가 사라진다해도 자기를 삭제하는게 아니라 NULL로 변경함
        blank=True,
        null=True,
        # null을 허용
        related_name='students',
        # 관계명을 새로 지정해줌(원래는 소문자이름_set임)
    )
