import graphene
import graphql_jwt
from apps.users.schema import UserQuery
from apps.users.mutations import (
        LoginMutation,
        LoginUser, 
#         SocialAuthMutation,
#         SocialAuth,
        RegisterMutation
        ) 


class Query(UserQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
        RegisterMutation,
        LoginMutation,
#         SocialAuthMutation,
        graphene.ObjectType
        ):
    login_user = LoginUser()
#     social_auth = SocialAuth()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

