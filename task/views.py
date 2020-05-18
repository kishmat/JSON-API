from django.shortcuts import render
from task.models import Member, Activity_period
from task.serializers import MemberSerializer, Activity_periodSerializer
from rest_framework import viewsets
# Create your views here.


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class Activity_periodViewSet(viewsets.ModelViewSet):
    queryset = Activity_period.objects.all()
    serializer_class = Activity_periodSerializer
