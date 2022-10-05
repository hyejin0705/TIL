from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        # 직접 참조하는 것을 권장하지 않음.
        # model = User
        
        # 활성화된 유저 모델을 리턴 (간접적 호출)
        model = get_user_model()

        # user모델이 존재하는 컬럼만 사용가능
        # 없는 컬럼을 사용하면, UnKnown field Error 발생
        # 이메일 확장해서 커스텀하기
        fields = UserCreationForm.Meta.fields + ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()

        # fields 부분을 재정의 해야 함.
        fields = ('email', 'first_name', 'last_name', )