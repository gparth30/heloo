from pyexpat import model
from wsgiref.validate import validator
from rest_framework import serializers
from api.models import Student




class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Student
        exclude = ['id']
    def roll(data):
        if data >= 200:
            raise serializers.ValidationError('Seat Full')
        return roll
        
def roll(data):
    if data <= 0:
        raise serializers.ValidationError('Rollno must be Greater than 0')
    else:
        return roll