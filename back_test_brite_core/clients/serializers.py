from rest_framework import serializers

from . import models


class ClientInsuranceRiskListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='insurance_risk.name')

    class Meta:
        model = models.ClientInsuranceRisk
        fields = ('id', 'name', 'post_date')


class ClientFieldSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

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

    def update(self, instance, validated_data):
        # instance.insurance_risk = validated_data.get('insurance_risk', instance.insurance_risk)
        # instance.save()

        client_fields = validated_data.get('client_fields')

        for field_data in client_fields:
            field_id = field_data.get('id', None)

            if not field_id:
                continue

            client_field = models.ClientField.objects.get(id=field_id, client_insurance_risk=instance)
            if client_field.field.is_select:
                client_field.select_option = field_data.get('select_option', client_field.select_option)
            else:
                client_field.value = field_data.get('value', client_field.value)
            client_field.save()

        return instance


