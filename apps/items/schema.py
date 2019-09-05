"""Imports"""

import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from config.base_node import BiditNode
from .models import Item as ItemModel
from apps.users.schema import UserNode

class ItemFilter(FilterSet):
    model = ItemModel
    filter_fields = ('title', 'description')

class ItemNode(DjangoObjectType):
    """
    Creates item node interface using base node
    """
    class Meta:
        model = ItemModel
        interfaces = (BiditNode, )


class ItemQuery(graphene.AbstractType):
    """
    Creates the item query schema
    """

    item = BiditNode.Field(ItemNode)
    items = DjangoFilterConnectionField(ItemNode, filterset_class=ItemFilter)
