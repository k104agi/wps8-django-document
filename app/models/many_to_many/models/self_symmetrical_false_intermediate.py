from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


# InstagramUser에서 만든 기능에 더해서
# 팔로우한 시점을 기록하는 클래스 만들기
# 중간모델 사용할 것
class TwitterUser(models.Model):
    """
    User간의 관계는 두 종류로 나뉨
    follow와 block(차단당한이)
    
    관계를 나타내는 Relation 클래스 사용 (중개모델)    
    """

    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    """
    TwitterUser간의 MTM관계를 정의
        from_user
        to_user
        follow인지, block인지
    """
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )

    # from_user와 to_user 둘 다 foreignkey로 TwitterUser를 연결해서 에러나는듯.
    # User에서 relation - > from user / to user에서 정보 가져오려고연결할때
    # 둘 다 relation_set으로 이름이 똑같아져서에러나는것

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )
    # 입력값을 제한하는 Choices 옵션 추가
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )
    # 관계생성일을 기록하기
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # get_FOO_display() 함수를 사용해서 choices를 사용한 필드의 출력값을 사용
        # 왼쪽의 f, b를 follow, block으로 표시함
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )
