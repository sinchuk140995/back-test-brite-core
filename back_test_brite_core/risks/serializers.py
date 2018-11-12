from rest_framework import serializers

from . import models


class InsuranceRiskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InsuranceRisk
        fields = ('id', 'name')


class SelectOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SelectOption
        fields = ('name',)


class FieldSerializer(serializers.ModelSerializer):
    options = SelectOptionSerializer(many=True, required=False)

    class Meta:
        model = models.Field
        fields = ('id', 'name', 'field_type', 'options')

    def create(self, validated_data):
        print(validated_data)


class InsuranceRiskSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = models.InsuranceRisk
        fields = ('id', 'name', 'fields')

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        insurance_risk = models.InsuranceRisk.objects.create(**validated_data)

        for field_data in fields_data:
            field_serializer = FieldSerializer(data=field_data)
            if field_serializer.is_valid():
                field_serializer.save()
            # field = models.Field.objects.create(insurance_risk=insurance_risk, **field)
        return insurance_risk
