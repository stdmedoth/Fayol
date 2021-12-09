from rest_framework import serializers
from api.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["name", "doc_type", "doc_id1", "doc_id2", "extern_code", "since", "user"]
