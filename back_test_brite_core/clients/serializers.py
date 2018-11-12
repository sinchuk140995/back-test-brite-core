from rest_framework import serializers

from . import models


class ClientInsuranceRiskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientInsuranceRisk
        fields = ('id', 'name')


class ClientFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientField
        fields = ('id', 'field', 'value', 'select_option')


class ClientInsuranceRiskSerializer(serializers.ModelSerializer):
    client_fields = ClientFieldSerializer(many=True)

    class Meta:
        model = models.ClientInsuranceRisk
        fields = ('id', 'insurance_risk', 'post_date', 'client_fields')

    def create(self, validated_data):
        client_fields = validated_data.pop('client_fields')
        client_insurance_risk = models.ClientInsuranceRisk.objects \
            .create(**validated_data)

        for field_data in client_fields:
            models.ClientField.objects.create(
                client_insurance_risk=client_insurance_risk,
                **field_data
            )
        return client_insurance_risk
