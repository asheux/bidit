"""Imports"""

import graphene
import graphql_jwt
from apps.users.schema import UserQuery
from apps.items.schema import ItemQuery
from apps.items.mutations import ItemMutation
from apps.users.mutations import (
        LoginMutation,
        LoginUser,
        RegisterMutation
        )


class Query(UserQuery, ItemQuery, graphene.ObjectType):
    """
    This class will inherit from multiple Queries
    as we begin to add more apps to our project
    """

class Mutation(RegisterMutation, LoginMutation, ItemMutation, graphene.ObjectType):
    """
    Base mutations
    """
    login_user = LoginUser()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

