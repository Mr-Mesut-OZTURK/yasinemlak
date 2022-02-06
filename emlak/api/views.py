from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework import viewsets, generics

from ..models import EmlakKayit
from .serializers import EmlakSerializer

from rest_framework.permissions import IsAuthenticated 


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# ViewSets define the view behavior.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'emlak': reverse('snippet-list', request=request, format=format)
    })




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class EmlakList(generics.ListCreateAPIView):
    queryset = EmlakKayit.objects.all()
    serializer_class = EmlakSerializer
    permission_classes =[IsAuthenticated]


class EmlakDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmlakKayit.objects.all()
    serializer_class = EmlakSerializer
    permission_classes =[IsAuthenticated]
