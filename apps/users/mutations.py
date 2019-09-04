"""Imports"""

import graphene
import graphql_jwt
from django.core.validators import validate_email
from graphql import GraphQLError
from .schema import UserNode
from .models import User


class RegisterUser(graphene.relay.ClientIDMutation):
    """Add user"""
    user = graphene.Field(UserNode)

    class Input:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        """
        change database by adding new user
        """
        if not kwargs.get('email'):
            raise GraphQLError('Users must have an email address')
        if kwargs.get('email'):
            validate_email(kwargs.get('email'))
        try:
            user = User.objects.get(email=kwargs.get('email'))
            if user:
                raise GraphQLError('User already exists')
        except User.DoesNotExist:
            user = User.objects.create_user(**kwargs)
            user.save()

        return cls(user=user)


class LoginUser(graphql_jwt.JSONWebTokenMutation):
    """Login user"""
    user = graphene.Field(UserNode)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        """user resolver"""
        user = info.context.user
        return cls(user=user)

class RegisterMutation(graphene.AbstractType):
    """register mutation"""
    create_user = RegisterUser.Field()


class LoginMutation(graphene.AbstractType):
    """Login mutation"""
    login_user = LoginUser.Field()

