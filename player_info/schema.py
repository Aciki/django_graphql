import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from django.db.models import Q
from .models import P_info
from club.models import Club_model


class P_infoType(DjangoObjectType):
    class Meta:
        model = P_info


class Query(graphene.ObjectType):
    P_infos = graphene.List(P_infoType , search = graphene.String(),first = graphene.Int(),skip = graphene.Int())

    def resolve_P_infos(self, info,search = None,first = None,skip = None,**kwargs):
        qs = P_info.objects.all()
        if search:
            filter = (
                Q(first_name__icontains=search)|
                Q(last_name__icontains=search)
            )
            gs = gs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

class CreateP_info(graphene.Mutation):
    create_p_info = graphene.Field(P_infoType)
    id = graphene.Int()
    first_name = graphene.String()
    last_name  = graphene.String()
    date_of_birth = graphene.DateTime()
    height = graphene.Int()
    rating = graphene.Int()
    is_available = graphene.Boolean()
    club_name = graphene.Int()
    posted_by = graphene.Field(UserType)
   

    #2
    class Arguments:
        first_name = graphene.String()
        last_name  = graphene.String()
        date_of_birth = graphene.DateTime()
        height = graphene.Int()
        rating = graphene.Int()
        is_available = graphene.Boolean()
        club_name = graphene.Int()

    #3
    def mutate(self, info, first_name,last_name,date_of_birth,height,rating,is_available,club_name):
        user =  info.context.user or None
        p_info = P_info(first_name = first_name ,last_name = last_name ,date_of_birth = date_of_birth,
        height = height,rating = rating, is_available = is_available,
        posted_by=user, )
        
        c = Club_model.objects.get(id = club_name )
        p_info.club_name = c
        p_info.save()

        return CreateP_info(first_name = p_info.first_name ,last_name = p_info.last_name ,
        date_of_birth = p_info.date_of_birth,
        height = p_info.height,rating = p_info.rating, is_available = p_info.is_available ,
        id = p_info.id, posted_by = p_info.posted_by)

class Mutation(graphene.ObjectType):
    Createp_info = CreateP_info.Field()

        
            
            
        


