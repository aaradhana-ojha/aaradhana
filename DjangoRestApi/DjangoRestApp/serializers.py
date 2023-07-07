from rest_framework import serializers
class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Posts
        fields=["post_title","post_description"]
