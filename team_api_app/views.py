# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import TeamMember
from .serializers import TeamMemberSerializer
from rest_framework import generics


class TeamMemberList(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
