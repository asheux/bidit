"""Imports"""

import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from config.base_node import BiditNode
from .models import Item as ItemModel
from apps.users.schema import UserNode

class ItemNode(DjangoObjectType):
    """
    Creates item node interface using base node
    """
    owner = graphene.Field(UserNode)

    class Meta:
        model = ItemModel
        interfaces = (BiditNode, )
