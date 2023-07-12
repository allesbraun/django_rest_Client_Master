from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("The cpf must contain eleven digits.")
        return cpf
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("The rg must contain nine digits.")
        return rg
    def validate_name(self, name):
        if not name.isalpha():
            raise serializers.ValidationError("The name must contain only letters")
        return name
    def validate_cellphone(self, cellphone):
        if len(cellphone) < 11:
            raise serializers.ValidationError("The cellphone number must contain at least eleven digits.")
        return cellphone