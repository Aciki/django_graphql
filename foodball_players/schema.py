import graphene
import graphql_jwt
from player_info.models import P_info
import player_info.schema_relay
import player_info.schema 
import users.schema


class Query(users.schema.Query ,player_info.schema.Query, graphene.ObjectType):
    pass

class Mutation(player_info.schema_relay.Mutation,users.schema.Mutation, player_info.schema.Mutation,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    


schema = graphene.Schema(query=Query, mutation=Mutation)