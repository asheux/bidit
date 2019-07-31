from graphene.relay import Node
from graphql_relay import from_global_id

class BiditNode(Node):

    class Meta:
        name = 'Node'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        if only_type:
            model = only_type._meta.model
        return model.objects.get(id=global_id)

