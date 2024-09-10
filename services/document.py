from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Business

@registry.register_document
class BusinessDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'businesses'

    class Django:
        model = Business  # The model associated with this Document

        fields = [
            'name',
            'description',
            'address',
            'phone_number',
            'website',
            'email',
            'created_at',
            'updated_at',
        ]

    # Add a field for the owner if needed
    # owner = fields.ObjectField(properties={
    #     'id': fields.IntegerField(),
    #     'username': fields.TextField(),
    # })

    def get_queryset(self):
        """Override the default queryset to include related fields."""
        return super().get_queryset().select_related('owner')