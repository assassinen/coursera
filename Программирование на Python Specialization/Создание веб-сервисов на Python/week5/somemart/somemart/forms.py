from django.forms import Form


class GoodForm(Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(max_length=1024)
    price = forms.IntegerField(min_value=1, max_value=1000000)


class ReviewForm(Form):
    text = forms.CharField(max_length=1024)
    grade = forms.IntegerField(min_value=1, max_value=10)
