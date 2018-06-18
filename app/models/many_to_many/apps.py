from django.apps import AppConfig
#python manage.py startapp many_to_many
#many_to_many 패키지를 models 안으로 이동
#apps.py를 수정 (앞에 models.붙이기)
#config -> settings -> INSTALLED_APPS에 추가
#models.py작성

class ManyToManyConfig(AppConfig):
    name = 'models.many_to_many'
