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
    owner = serializers.ReadOnlyField(source='owner.id')

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

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.amount = validated_data.get('amount',instance.amount)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.save()
        
        return instance
