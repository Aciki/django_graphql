from club.models import Club_model
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id #needed for updating
from .models import P_info
from users.schema import UserType


#1
class P_infoNode(DjangoObjectType):
    class Meta:
        model = P_info
        filter_fields = [ "first_name",
        "last_name"  ,
        "date_of_birth" ,
        "height" ,
        "is_available" ,
        "club_name",
        ]

        interfaces = (graphene.relay.Node,)


class Club_modelNode(DjangoObjectType):
    class Meta:
        model = Club_model
        filter_fields = [ "club_name"]
        interfaces = (graphene.relay.Node,)

class CreateClub(graphene.relay.ClientIDMutation):
    club_name = graphene.Field(Club_modelNode)

    class Input:
        club_name = graphene.String()

    def mutate_and_get_payload(self, info, **input):

        club_name = Club_model(
            club_name=input.get('club_name')
        )
        club_name.save()

        return CreateClub(club_name=club_name)

class CreateP_info(graphene.relay.ClientIDMutation):
    player = graphene.Field(P_infoNode)
    posted_by = graphene.Field(UserType)

    class Input:
        
        first_name = graphene.String()
        last_name  = graphene.String()
        date_of_birth = graphene.DateTime()
        height = graphene.Int()
        rating = graphene.Int()
        is_available = graphene.Boolean()
        club_name = graphene.String()
        

    def mutate_and_get_payload(self, info, **input):
        user =  info.context.user or None

        player = P_info(
            first_name=input.get("first_name"),
            club_name=Club_model.objects.get(club_name=input.get("club_name")),
            last_name= input.get("last_name"),
            rating    = input.get("rating"),
            date_of_birth = input.get("date_of_birth"),
            height = input.get("height"),
            is_available = input.get("is_available"),
            posted_by = user,
            
        )
        player.save()

        return CreateP_info(player=player)


class UpdatePlayer(graphene.relay.ClientIDMutation):
    player = graphene.Field(P_infoNode)

    class Input:
        id = graphene.String()
        first_name = graphene.String()
        last_name  = graphene.String()
        date_of_birth = graphene.DateTime()
        height = graphene.Int()
        rating = graphene.Int()
        is_available = graphene.Boolean()
        club_name = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user =  info.context.user or None

        player = P_info.objects.get(pk=from_global_id(input.get('id'))[1])
        player.first_name = input.get('first_name')
        player.last_name  = input.get("last_name")
        player.date_of_birth = input.get("date_of_birth")
        player.height = input.get("height")
        player.rating = input.get("rating")
        player.is_available = input.get("is_available")
        player.club_name=Club_model.objects.get(club_name=input.get("club_name"))
        player.posted_by = user
        player.save()

        return UpdatePlayer(player=player)


class DeletePlayer(graphene.relay.ClientIDMutation):
    player = graphene.Field(P_infoNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):

        player = P_info.objects.get(pk=from_global_id(input.get('id'))[1])
        player.delete()

        return DeletePlayer(player=player)



class Mutation(graphene.AbstractType):
    create_club   = CreateClub.Field()
    create_player = CreateP_info.Field()
    update_player = UpdatePlayer.Field()
    delete_player = DeletePlayer.Field()






      