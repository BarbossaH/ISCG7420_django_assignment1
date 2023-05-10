from django.forms import ModelForm


class RoomForm(ModelForm):
    class Meta:
        # all field in the GradeBookClass model. notice it is double lower slash
        fields = "__all__"
