from rest_framework.views import APIView, Http404
from rest_framework.response import Response
from .serializer import StudentApplicationSerializer, CreateMngtAccSerializer
from .permission import OnboardMngt
class StudentApplication(APIView):
    """SERVES AS THE ENTRANCE FOR INCOMIND STUDENT APPLICATION INTO THE SYSTEM"""
    serializer_class = StudentApplicationSerializer
    
    def post(self, request):
        serializer = StudentApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
    
    
    
class ManagementOnboarding(APIView):
    """
    I can use the django admin panel to create their account but this is only existing so a fellow management can add another management
    The way it work is one mngt role can add other mngt, if issue arises where its nt inudstry practice to allow a management add another management user
    I WILL JUST DISREGARD THIS ENDPOINT BYT INSTANTLY RETURNIG A 404
    TODO: Send email notification to all mngt if a new mngt is added
    """
    serializer_class = CreateMngtAccSerializer
    permission_classes = [OnboardMngt]
    def post(self, request):
        # raise Http404 #   UNCOMMENT THIS TO RENDER IT NOT FOUNDS
        serializer = CreateMngtAccSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
        
    