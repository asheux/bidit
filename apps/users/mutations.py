import graphene
from django.core.validators import validate_email
from graphql import GraphQLError
from .schema import UserNode
from .models import User

class CreateUser(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate_and_get_payload(root, info, **kwargs):
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

        return CreateUser(user=user)

class Mutation(graphene.AbstractType):
    create_user = CreateUser.Field()
