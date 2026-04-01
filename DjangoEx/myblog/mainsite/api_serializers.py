from rest_framework import serializers

from .models import Character, CharacterImage


class CharacterImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CharacterImage
        fields = ('id', 'image', 'image_url')
        read_only_fields = ('id', 'image_url')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if not obj.image:
            return None
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url


class CharacterSerializer(serializers.ModelSerializer):
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)
    images = CharacterImageSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'gender',
            'gender_display',
            'affiliation',
            'homeland',
            'occupation',
            'element',
            'first_appearance',
            'description',
            'images',
        )
        read_only_fields = ('id', 'gender_display', 'images')
