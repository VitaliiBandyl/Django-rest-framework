from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, Author
from .serializers import ArticleSerializer


# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})
#
#     def post(self, request):
#         article = request.data.get('article')
#         # Create an article from the above data
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({"success": f"Article '{article_saved.title}' created successfully"})
#
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({
#                 "success": f"Article '{article_saved.title}' updated successfully"
#             })
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "message": f"Article with id `{pk}` has been deleted."
#         }, status=204)

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer