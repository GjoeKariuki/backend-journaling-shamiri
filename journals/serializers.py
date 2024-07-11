from rest_framework import serializers

from journals.models import JournalEntry




class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = "__all__"


class GetJournalEntriesSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = JournalEntry
        fields = "__all__"
    
    def get_user(self,obj):
        from users.serializers import GetUserSerializer
        serializer = GetUserSerializer(obj.user)
        return serializer.data  
    

