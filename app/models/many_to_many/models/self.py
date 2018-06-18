from django.db import models

__all__ = (
    'FacebookUser',
)
# 튜플은 1개라도 항상 맨 뒤가 ,로 끝나야 함


# Many to Many에서 Self를 참조하는 경우?

class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 관계가 대칭적으로 형성됨
    # A가 B를 친구로 추가하면, B의 friends에도 A가 추가됨

    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name
