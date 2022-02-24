from testApp.models import AddressBook
from rest_framework.serializers import ModelSerializer
class AddressSerializer(ModelSerializer):
    class Meta:
        model = AddressBook
        fields = '__all__'
        