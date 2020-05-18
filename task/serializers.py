from rest_framework_json_api import serializers
from task.models import Member, Activity_period


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class Activity_periodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity_period
        fields = '__all__'
