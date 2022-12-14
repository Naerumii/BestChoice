from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from festivals.serializers import BookMarkSerializer
from recruits.serializers import RecruitSerializer


# 회원가입과 회원정보수정에서 사용할 serial
class UserProfileSerializer(serializers.ModelSerializer):
    bookmark_set = BookMarkSerializer(many=True)
    recruit_user_set = RecruitSerializer(many=True)
    #승연님이 만드신거 리크룻 
    class Meta:
        model = User
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_nickname", "user_introduce", "user_address", "user_phone", "user_profile_img"]

# 로그인 시 사용할 serial
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token
    