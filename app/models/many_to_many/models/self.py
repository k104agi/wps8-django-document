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

    def show_friends(self):
        # 본인의 친구목록
        # 이한영의 친구목록
        # - 천이수
        # - 박성민
        # (총 2명)

        friends_list = list()
        print(self.friends)
        print('위는 self.friends 출력 결과입니다')
        print()

        print(self.friends.all())
        print('위는 self.friends.all() 출력 결과입니다')
        print()

        for x in self.friends.all():
            friends_list.append(x)

        # 리스트에 인덱스 연산 사용
        print(f'- {friends_list[0]}\n'
              f'- {friends_list[1]}\n'
              f'(총 {len(friends_list)}명)')

        # print(f'- {self.friends.first()} \n '
        #       f'- {self.friends.second()}\n '
        #       f'(총 {len(self.friends)}명)')
