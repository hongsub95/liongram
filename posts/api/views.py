from .serializers import QnASerializer,FAQBaseSerializer,CommentBaseSerializer
from rest_framework import generics,permissions,viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from posts import models as posts_models


class QnAViewset(viewsets.ModelViewSet):
    queryset = posts_models.QnA.objects.all()
    serializer_class = QnASerializer

    @action(detail=True, methods=['get'])
    def get_comment(self,request,pk=None):
        post = self.get_object()
        comments = post.Comment.all()
        serializer = CommentBaseSerializer(comments,many=True)
        return Response(serializer.data)
        
    """
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            pass
            return [permission() for permission in permission_classes]
    """




class FaQListView(generics.ListAPIView):
    queryset = posts_models.FAQ.objects.all()
    serializer_class = FAQBaseSerializer

class CommentListView(generics.ListAPIView):
    queryset = posts_models.Comment.objects.all()
    serializer_class = CommentBaseSerializer


    
    

      