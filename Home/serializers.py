from rest_framework import serializers
from Home.models import Role,Faculty,User,Contribution,FileType

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = ('__all__')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('__all__')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('__all__')

class FileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = ('__all__')