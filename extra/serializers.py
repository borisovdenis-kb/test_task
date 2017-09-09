from rest_framework import serializers
from test_task_app.models import (
    Offers, Claims, CreditOrganizations, WorkSheets
)


class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields = (
            'id', 'created_date', 'sent_date', 'worksheet', 'offer', 'status'
        )


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = (
            'id', 'created_date', 'changed_date', 'rotation_start_date', 'rotation_end_date',
            'title', 'offer_type', 'scoring_min', 'scoring_max', 'credit_org'
        )


class WorksheetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSheets
        fields = (
            'id', 'created_date', 'changed_date', 'first_name', 'last_name',
            'middle_name', 'birth_day', 'phone', 'passport_number', 'scoring'
        )


class CreditOrganisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditOrganizations
        fields = ('id', 'org_name', )
