from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class PersonListCreateView(generics.ListCreateAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name')
        age = self.request.query_params.get('age')
        email = self.request.query_params.get('email')

        if name:
            queryset = queryset.filter(name=name)

        if age:
            queryset = queryset.filter(age=age)

        if email:
            queryset = queryset.filter(email=email)

        return queryset

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

