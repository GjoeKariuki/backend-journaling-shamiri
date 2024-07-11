import django_filters 
from journals.models import JournalEntry



class JournalEntryFilter(django_filters.FilterSet):
    class Meta:
        model = JournalEntry
        fields = "__all__"