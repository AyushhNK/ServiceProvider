# documents.py

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Service

@registry.register_document
class ServiceDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'services'

    class Django:
        model = Service  # The model associated with this Document

        fields = [
            'title',
            'description',
            'price',
            'discount',
        ]

    # Add a field for the seller if needed
    seller = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
    })

    def get_queryset(self):
        """Override the default queryset to include related fields."""
        return super().get_queryset().select_related('seller')