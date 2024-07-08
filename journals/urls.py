from django.urls import path
from journals.views import journal_detail,journal_list, journal_summary





urlpatterns = [
        path('journal_list/', journal_list,name="journals"),
        path('journal_detail/<str:pk>/',journal_detail, name="journaldetails"),
        path('journal_summary/',journal_summary, name="journalsummary"),
]

