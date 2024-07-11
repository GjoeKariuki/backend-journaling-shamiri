from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404






class MyDBCRUDHelper:

    """
    Helper class for performing CRUD operations on any model.
    """
    def __init__(self, myrequest, mymodel, mymodelfilter, mymodelserializer=None, getterSerializer=None ,mypk=None, partial=True):
        """
        Initialize the helper with necesssary parameters
        """
        self.mymodel = mymodel
        self.mymodelfilter = mymodelfilter
        self.mymodelserializer = mymodelserializer
        self.mypk = mypk
        self.partial = partial
        self.myrequest = myrequest
        self.getterSerializer = getterSerializer
        


    def list_objects(self):
        """
        List all objects filtered by query parameters.
        """
        try:
            obj_queryset  = self.mymodel.objects.all()
            obj_filterset = self.mymodelfilter(self.myrequest.GET, queryset=obj_queryset).qs
            serializer = self.getterSerializer(obj_filterset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def create_object(self):
        """
        Create a new object.
        """
        try:
            serializer = self.mymodelserializer(data=self.myrequest.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def list_object(self):
        """
        Retrieve a single object by its primary key.
        """
    
        try:
            obj = get_object_or_404(self.mymodel, pk=self.mypk)
            serializer = self.getterSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({'error':'Object not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def update_object(self):
        """ update object """
        try:
            obj = get_object_or_404(self.mymodel, pk=self.mypk)
            serializer = self.mymodelserializer(obj, self.myrequest.data, partial=self.partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'error':'Object not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete_object(self):
        """ finds object by id and deletes """
        try:
            obj = get_object_or_404(self.mymodel, pk=self.mypk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'error':'Object not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)








