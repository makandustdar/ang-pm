from django import forms

from .models import Review

PERIOD = (
    ('day', 'روز'),
    ('month', 'ماه'),
    ('year', 'سال'),
)


class ReviewForm(forms.ModelForm):
    reviewPeriod = forms.ChoiceField(choices=PERIOD, label='دوره بازدید')

    class Meta:
        model = Review
        fields = ['part', 'machine', 'reviewPeriod', 'reviewCount']
        labels = {'part': 'نام قطعه', 'machine': 'نام دستگاه', 'reviewCount': 'زمان بازدید'}

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['part'].widget.attrs['class'] = 'select2 form-select form-select-lg'
        self.fields['machine'].widget.attrs['class'] = 'select2 form-select form-select-lg'
