"""Imports"""
import graphene
from graphene import relay
from graphql import GraphQLError

from .models import Item
from .schema import ItemNode

class AddItem(relay.ClientIDMutation):
    """
    Perform mutations on the database by adding new items
    """
    item = graphene.Field(ItemNode)

    class Input:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        reserve_price = graphene.Int(required=True)
        photo = graphene.String(required=True) # TODO add real image

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        """
        adding to the database
        """
        user = info.context.user

        if user.is_anonymous:
            return GraphQLError("You must login to add item")

        item = Item(owner=user, **kwargs)
        item.save()

        return cls(item=item)


class ItemMutation(graphene.AbstractType):
    """Item mutation"""
    create_item = AddItem.Field()
