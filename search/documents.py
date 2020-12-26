from django_elasticsearch_dsl import Index, Document
from django_elasticsearch_dsl.documents import DocType
from mainApp.models import Post

posts = Index('posts')


@posts.doc_type
class PostDocument(DocType):
    class Django:
        model = Post

        fields = [
            'title',
            'slug',
            'text',
            'under_title',
            'published',
            'status'
        ]
