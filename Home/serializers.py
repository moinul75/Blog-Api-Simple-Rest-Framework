from rest_framework import serializers
from .models import Category, Tag, Image, Blog, Reaction, Comment, Reply, BlogReadingTime, BlogWatchTime

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    watch_count = serializers.SerializerMethodField()
    reaction_count = serializers.SerializerMethodField()

    def get_watch_count(self, obj):
        return obj.watch_times.count()

    def get_reaction_count(self, obj):
        return obj.reactions.count()

    class Meta:
        model = Blog
        fields = ['uid','user','images', 'title','category', 'blog_text','main_image', 'comments', 'tags', 'category', 'watch_count', 'reaction_count','created_at','updated_at']

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class BlogReadingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogReadingTime
        fields = '__all__'

class BlogWatchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogWatchTime
        fields = '__all__'

        