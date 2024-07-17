from django.urls import path
from persona.views import CreatePerson, GetPersonById, EditPersonById, DeletePersonById, GetAllPersons

urlpatterns = [
    path('createPerson', CreatePerson.as_view(), name='create-person'),
    path('getPersonById/<int:pk>', GetPersonById.as_view(), name='get-person-by-id'),
    path('deletePersonById/<int:pk>', DeletePersonById.as_view(), name='delete-person-by-id'),
    path('editPersonById/<int:pk>', EditPersonById.as_view(), name='edit-person-by-id'),
    path('getAllPersons', GetAllPersons.as_view(), name='get-all-persons'),
]
