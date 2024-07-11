import django_filters

from users.models import CustomUser



class MyUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = "__all__"