import graphene
import graphql_jwt
from apps.users.schema import Query as UserQuery
from apps.users.mutations import Mutation as UserMutation

class Query(UserQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(UserMutation, graphene.ObjectType):
    auth_token = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

