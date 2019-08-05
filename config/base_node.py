from graphene.relay import Node
from graphql_relay import from_global_id


class BiditNode(Node):

    class Meta:
        name = 'MyNode'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        if only_type:
            return only_type._meta.model.objects.get(pk=global_id)

