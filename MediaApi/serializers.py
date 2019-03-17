from rest_framework import serializers
from  MediaApi.models import Images
from django.core.exceptions import ValidationError
import sys


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    description = serializers.CharField()
    createdby=serializers.CharField()
    image = serializers.FileField(max_length=255)


    def create(self, validated_data):
        return Images.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(validated_data)
        instance.name = validated_data["name"]
        if 'description' in validated_data.keys():
            instance.description = validated_data["description"]
        if 'createdby' in validated_data.keys():
            instance.createdby = validated_data["createdby"]
        instance.image = validated_data["image"]
        instance.save()
        return instance

    def validate(self,data):
        file_size = data['image'].size
        print("inside",file_size)
        limit_kb = 5000
        if file_size > limit_kb * 1024:
            raise serializers.ValidationError("Max size of file is 5 MB")
        else :
            return data
