from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )
    


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)  # 외래키 == 읽기 전용 필드
        # 해당 필드를 유효성 검사에서 제외시키고 데이터 조회시에 출력.



class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    # 참조하기 위해서는 위에 존재해야 함. (위치변경)

    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 원래 ORM 코드 : article.comment_set.count()
    # article은 ArticleSerializer에서 실행되기 때문에 제거,
    # 문자열이기 때문에 () 제거

    class Meta:
        model = Article
        fields = '__all__'


