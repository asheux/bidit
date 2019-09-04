""" Imports """

import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from config.base_node import BiditNode
from .models import User as UserModel


class UserFilter(FilterSet):
    """
    Filters the users according to the field specified
    """
    model = UserModel
    filter_fields = ['first_name', 'last_name', 'email']

class UserNode(DjangoObjectType):
    """Creates an interface using the base node"""
    class Meta:
        model = UserModel
        interfaces = (BiditNode, )

class UserQuery(graphene.AbstractType):
    """
    Creates the users query schema
    """
    current_user = graphene.Field(UserNode)
    user = BiditNode.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    def resolve_current_user(root, info, **kwargs):
        """
        get current logged in user
        """
        user = info.context.user
        if user.is_anonymous:
            return None
        return user

