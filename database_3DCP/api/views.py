from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    # XXX: Just for test
    # return Response(UserSerializer({'node_type': 'printer', 'parent_node_id': 12345}).data)

    # XXX: The nodes is a list of object and is not yet "serialized"
    nodes = User.objects.all()

    # XXX: many=True --> as it might be a list
    serializer = UserSerializer(nodes, many=True)
    return Response(serializer.data)
    # return render(request, 'api/tools.html', UserSerializer({'node_type': 'printer', 'parent_node_id': 12345}).data)

# FIXME: change all "user" to "node"
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)