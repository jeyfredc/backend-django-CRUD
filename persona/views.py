from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .serializer import PersonaSerializer, PersonaUpdateSerializer
from .models import Persona
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


class CreatePerson(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=PersonaSerializer)
    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        errors = {
            "error": True,
            "description": serializer.errors['non_field_errors'][0] 
            if 'non_field_errors' in serializer.errors 
            else f"No se encontró la persona con el número de documento {request.data.get('document_number', '')}"
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class GetPersonById(APIView):
    def get(self, request, pk):
        try:
            person = Persona.objects.get(pk=pk)
            serializer = PersonaSerializer(person)
            return Response(serializer.data)
        except Persona.DoesNotExist:
            return Response({
                "error": True,
                "description": f"No se encontró la persona con el ID {pk}"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": True, "description": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditPersonById(APIView):
    """
    put:
    Actualiza una persona con los campos dados. Solo se pueden actualizar los campos: nombres, apellidos, hobbie.
    """
    @swagger_auto_schema(request_body=PersonaUpdateSerializer)
    def put(self, request, pk):
        try:
            person = Persona.objects.get(pk=pk)
            serializer = PersonaUpdateSerializer(person, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({
                "error": True,
                "description": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Persona.DoesNotExist:
            return Response({
                "error": True,
                "description": f"No se encontró la persona con el ID {pk}"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": True, "description": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeletePersonById(APIView):
    @swagger_auto_schema()
    def delete(self, request, pk):
        try:
            person = Persona.objects.get(pk=pk)
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response({
                "error": True,
                "description": f"No se encontró la persona con el ID {pk}"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": True, "description": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAllPersons(APIView):
    @swagger_auto_schema()
    def get(self, request):
        persons = Persona.objects.all()
        serializer = PersonaSerializer(persons, many=True)
        return Response(serializer.data)
