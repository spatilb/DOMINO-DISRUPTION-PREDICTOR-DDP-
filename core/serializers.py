from rest_framework import serializers
from .models import Tag, DisruptionEntry, RootCauseRule, SuggestionTemplate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class DisruptionEntrySerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source='tag.name', read_only=True)
    root_cause_suggestion = serializers.SerializerMethodField()

    class Meta:
        model = DisruptionEntry
        fields = '__all__'
        read_only_fields = ('user',)

    def get_root_cause_suggestion(self, obj):
        if not obj.tag:
            return None
            
        # Prioritize rules with keywords
        rules = RootCauseRule.objects.filter(tag=obj.tag).order_by('-keyword') 
        
        text_to_search = (obj.context or "") + " " + (obj.notes or "")
        text_to_search = text_to_search.lower()

        for rule in rules:
            if rule.keyword:
                if rule.keyword.lower() in text_to_search:
                    return rule.root_cause_label
            else:
                # If rule has no keyword, it's a generic rule for this tag
                # We return it only if we haven't found a more specific one? 
                # Or maybe return it as a fallback.
                # Since we ordered by -keyword, empty keywords (length 0) come last (or first depending on null handling).
                # Safer to just return it if we are here.
                return rule.root_cause_label
        
        return None

class RootCauseRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RootCauseRule
        fields = '__all__'

class SuggestionTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionTemplate
        fields = '__all__'