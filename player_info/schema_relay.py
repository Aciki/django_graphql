import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from club.models import Club_model

from .models import P_info


#1
class P_infoFilter(django_filters.FilterSet):
    class Meta:
        model = P_info
        fields = [ "first_name",
        "last_name"  ,
        "date_of_birth" ,
        "height" ,
        "is_available" ,
        "club_name",
        
        
        ]


#2
class P_infoNode(DjangoObjectType):
    class Meta:
        model = P_info
        #3
        interfaces = (graphene.relay.Node, )




class RelayQuery(graphene.ObjectType):
    #4
    relay_p_info = graphene.relay.Node.Field(P_infoNode)
    #5
    relay_p_info = DjangoFilterConnectionField(P_infoNode, filterset_class=P_infoFilter)




      