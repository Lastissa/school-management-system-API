from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentApplicationSerializer

class StudentApplication(APIView):
    """SERVES AS THE ENTRANCE FOR INCOMIND STUDENT APPLICATION INTO THE SYSTEM"""
    serializer_class = StudentApplicationSerializer
    
    def post(self, request):
        serializer = StudentApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)