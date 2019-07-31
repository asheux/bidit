import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model
from config.node import BiditNode
from .models import User as UserModel

class UserFilter(FilterSet):
    model = UserModel
    filter_fields = ['first_name', 'last_name', 'email']

class UserNode(DjangoObjectType):
    class Meta:
        model = UserModel
        interfaces = (BiditNode, )

class Query(graphene.ObjectType):
    user = BiditNode.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

