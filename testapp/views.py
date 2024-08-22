from rest_framework.views import APIView
from rest_framework.response import Response

class HelloworldView(APIView):
    
    def get(self, request):
        return Response({'message': 'Hello, world!'})
    


