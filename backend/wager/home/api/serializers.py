from rest_framework import serializers
from home.models import Questions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'creator', 'name', 'age', 'education_lvl', 'annual_income', 'net_worth', 'known_expenses', 'possible_expenses', 'liquidity_needs', 'investment_objectives', 'risk_tolerance', 'reviewed_notes', 'beta', 'investment_experience' )
