from django.db import models

__all__ = (
    'Person',
    'Group',
    'Membership',
)


# 중간모델(Intermediate)을 쓰는 경우

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        # 밑에 정의가 오기 때문에 ''안에 적어줌

        through_fields=('group', 'person'),
        # 앞이 source, 뒤가 타겟
        # 아래의 recommender 때문에 ForeignKey 여러개사용하는게 걸리는걸막으려고
        # through_fields를 추가한 것
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    # p1이라는 Person 인스턴스가 있을 때
    # Membership.objects.filter(person=p1)
    # Membership.objects.filter(recommender=p1) 두 경우가 같이 발생함

    # p1.membeship_set.all()

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    # recommender = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 위에 이거 쓰면 안됨
    # 왜냐면 중간모델에서 여러개의 ForeignKey가 한 곳을 바라보면 안됨
    # 쓰려면 어떻게 하느냐?? 위의 group에 through_fields 추가
    # 그리고 Membership에서 Person, recommender에 각각 related_name을 새로 지정

    recommender = models.ForeignKey(
        Person,
        related_name='memberships_by_recommender',
        on_delete=models.SET_NULL,
        blank=True, null=True)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return '{person} - {group} ({date})'.format(
            person=self.person.name,
            group=self.group.name,
            date=self.date_joined
        )
