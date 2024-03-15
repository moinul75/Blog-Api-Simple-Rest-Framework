from rest_framework import generics, permissions,pagination,filters
from .models import Category, Tag, Image, Blog, Reaction, Comment, Reply, BlogReadingTime, BlogWatchTime
from .serializers import CategorySerializer, TagSerializer, ImageSerializer, BlogSerializer, ReactionSerializer, CommentSerializer, ReplySerializer, BlogReadingTimeSerializer, BlogWatchTimeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CustomPagination(pagination.PageNumberPagination):
    page_size = 1  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = 'page'
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer 
    permission_classes = [permissions.IsAuthenticated]

class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer 
    permission_classes = [permissions.IsAuthenticated]

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer 
    permission_classes = [permissions.IsAuthenticated]

class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    def get_permissions(self):
        if self.request.method == 'GET': 
            return []
        else: 
            return [permissions.IsAuthenticated()] 

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    permission_classes = [permissions.IsAuthenticated]

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 
    search_fields = ['title', 'blog_text']
    filter_backends = [filters.SearchFilter] 
    pagination_class = CustomPagination
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        else:
            return [permissions.IsAuthenticated()]

class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 
    permission_classes = [permissions.IsAuthenticated] 
    

class ReactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer 
    permission_classes = [permissions.IsAuthenticated]

class ReactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer 
    permission_classes = [permissions.IsAuthenticated]

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [permissions.IsAuthenticated]

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [permissions.IsAuthenticated]

class ReplyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer 
    permission_classes = [permissions.IsAuthenticated]

class ReplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class BlogReadingTimeListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogReadingTime.objects.all()
    serializer_class = BlogReadingTimeSerializer 
    permission_classes = [permissions.IsAuthenticated]

class BlogReadingTimeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogReadingTime.objects.all()
    serializer_class = BlogReadingTimeSerializer 
    permission_classes = [permissions.IsAuthenticated] 

class BlogWatchTimeListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogWatchTime.objects.all()
    serializer_class = BlogWatchTimeSerializer 
    permission_classes = [permissions.IsAuthenticated]

class BlogWatchTimeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogWatchTime.objects.all()
    serializer_class = BlogWatchTimeSerializer 
    permission_classes = [permissions.IsAuthenticated]
    