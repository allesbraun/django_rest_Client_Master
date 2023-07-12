from rest_framework import serializers

from clients.models import Client
from clients.validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
    def validate(self, data):
        
        errors = {}
        
        if not valid_cpf(data['cpf']):    
            raise serializers.ValidationError({'cpf': "The cpf must contain eleven digits."})
        if not valid_rg(data['rg']):
            raise serializers.ValidationError({'rg': "The rg must contain nine digits."})
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name': ["The name must contain only letters"]})
        if not valid_cellphone(data['cellphone']):
            raise serializers.ValidationError({'cellphone': "The cellphone number must contain at least eleven digits."})
        
        if errors:
            raise serializers.ValidationError(errors)
        
        return data
    
    