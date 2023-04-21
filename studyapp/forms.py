from django.forms import ModelForm
from .models import GradeBookClass


class RoomForm(ModelForm):
    class Meta:
        model = GradeBookClass
        # all field in the GradeBookClass model. notice it is double lower slash
        fields = "__all__"
