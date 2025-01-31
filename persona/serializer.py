from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'type_document', 'document_number', 'name', 'last_name', 'hobbie']
        read_only_fields = ['id']
    
    
    def validate(self, attrs):
        if Persona.objects.filter(document_number=attrs['document_number']).exists():
            raise serializers.ValidationError(f'Ya existe una persona con el número de documento {attrs["document_number"]}')
        return attrs
    
    
    def validate_tipo_documento(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("El tipo de documento debe contener solo letras.")
        return value
    
    def validate_exist_person_by_id(self, value):
        if not Persona.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"No se encontró la persona con el id {value}")
        return value
    

class PersonaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['name', 'last_name', 'hobbie']
    
    
    def validate(self, attrs):
        if 'name' in attrs and not all(c.isalpha() or c.isspace() for c in attrs['name']):
            raise serializers.ValidationError("El nombre debe contener solo letras .")
        if 'last_name' in attrs and not all(c.isalpha() or c.isspace() for c in attrs['last_name']):
            raise serializers.ValidationError("El apellido debe contener solo letras .")
        return attrs