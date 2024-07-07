from django.urls import path
from journals.views import journal_detail,journal_list





urlpatterns = [
        path('journal_list/', journal_list,name="journals"),
        path('journal_detail/<str:pk>/',journal_detail, name="journaldetails")

]

