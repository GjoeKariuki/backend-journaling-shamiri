from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response

from journals.models import JournalEntry
from journals.dbhelper import MyDBCRUDHelper
from journals.serializers import JournalEntrySerializer,GetJournalEntriesSerializer
from journals.filters import JournalEntryFilter

# Create your views here.


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