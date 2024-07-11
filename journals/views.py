from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.db.models.functions import TruncDay,TruncWeek,TruncMonth,TruncYear

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status


from journals.models import JournalEntry
from journals.dbhelper import MyDBCRUDHelper
from journals.serializers import JournalEntrySerializer,GetJournalEntriesSerializer
from journals.filters import JournalEntryFilter







@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def journal_list(request):
    mydbhelper = MyDBCRUDHelper(myrequest=request, 
                mymodel=JournalEntry, 
                mymodelfilter=JournalEntryFilter, 
                getterSerializer=GetJournalEntriesSerializer,
                mymodelserializer=JournalEntrySerializer)
    if request.method == 'GET':
        return mydbhelper.list_objects()
    elif request.method == 'POST':
        return mydbhelper.create_object()
    


@api_view(['GET','PUT','DELETE'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def journal_detail(request,pk):
    mydbhelper = MyDBCRUDHelper(myrequest=request, 
                mymodel=JournalEntry, 
                mymodelfilter=JournalEntryFilter, 
                mymodelserializer=JournalEntrySerializer,
                mypk=pk,
                getterSerializer=GetJournalEntriesSerializer
                )

    if request.method == 'GET':
        return mydbhelper.list_object()
    elif request.method == 'PUT':
        return mydbhelper.update_object()
    elif request.method == 'DELETE':
        return mydbhelper.delete_object()
    


@api_view(['GET'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def journal_summary(request):
    period = request.get('period')
    user = request.user
    
    if period == 'daily':
        journals_data = JournalEntry.objects.filter(user=user).annotate(date=TruncDay('date')).values('date').annotate(count=Count('id')).order_by('-date')
    elif period == 'weekly':
        journals_data = JournalEntry.objects.filter(user=user).annotate(date=TruncWeek('date')).values('date').annotate(count=Count('id')).order_by('-date')
    elif period == 'monthly':
        journals_data = JournalEntry.objects.filter(user=user).annotate(date=TruncMonth('date')).values('date').annotate(count=Count('id')).order_by('-date')
    elif period == 'yearly':
        journals_data = JournalEntry.objects.filter(user=user).annotate(date=TruncYear('date')).values('date').annotate(count=Count('id')).order_by('-date')

    return Response(journals_data, status=status.HTTP_200_OK)