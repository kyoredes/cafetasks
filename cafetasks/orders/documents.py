from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.registries import registry
from cafetasks.orders.models import Order


@registry.register_document
class OrderDocument(Document):
    status = fields.NestedField(properties={"name": fields.TextField()})

    class Index:
        name = "orders"

    class Django:
        model = Order
        fields = ["id", "table_number"]

    def prepare_orders(self, instance):
        return [{"name": status.name} for status in instance.status.all()]
