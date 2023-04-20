from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # all field in the Room model. notice it is double lower slash
        fields = "__all__"
