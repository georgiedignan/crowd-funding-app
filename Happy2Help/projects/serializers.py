from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    not_for_profit = serializers.BooleanField(default=False)
    amount = serializers.IntegerField(required=False)
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.CharField(max_length=200)

    def validate(self,data):
        # if data["not_for_profit"] == True:
            # if 'amount' in data:
                # raise serializers.ValidationError("")
        # else:
            # if 'amount' not in data:
                # raise serializers.ValidationError("")
        # return data

        if data["not_for_profit"] == True and 'amount' in data:
            raise serializers.ValidationError("")
        elif data["not_for_profit"] == False and 'amount' not in data:
            raise serializers.ValidationError("")
        return data

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
