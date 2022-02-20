from rest_framework.serializers import ModelSerializer
# from rest_framework.serializers import HyperlinkedIdentityField, HyperlinkedRelatedField - для использования ссылок
from .models import Project
from .models import ToDo


# сериализуем приложение Проекты
class ProjectSerializer(ModelSerializer):
    # Настройка сериализатора
    # Настройка Foreign Key
    # owner = HyperlinkedIdentityField(view_name='user-detail')
    # Настройка Many to many
    # users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


# сериализуем приложение Заметки
class ToDoSerializer(ModelSerializer):
    # project = HyperlinkedIdentityField(view_name='project-detail')
    # creator = HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = ToDo
        exclude = ('is_active',)
