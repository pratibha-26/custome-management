from .models import User, Activityperiod
from .serializer import UserSerializer, ActivitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(APIView):
    """
    List all Users.
    """
    def get(self, request):
        """Get the user and activity data"""
        output = {}
        try:
            snippets = User.objects.all()
            serializer = UserSerializer(snippets, many=True)
            activity = Activityperiod.objects.all()
            activity_data = ActivitySerializer(activity, many=True)
            output['members'] = serializer.data
            output['activity_period'] = activity_data.data
        except:
            output['ok'] = 'False'
        return Response(output)
