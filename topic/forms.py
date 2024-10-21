# forms.py
from django import forms
from .models import SalesForm_Data

class SalesForm(forms.ModelForm):
    productName = forms.CharField(label='產品名稱', max_length=100)  # 自定義字段
    productFeatures = forms.CharField(label='產品特性或相關數據', widget=forms.Textarea)  # 自定義字段
    style = forms.ChoiceField(label='風格', choices=[('Style1', '雷軍'), ('Style2', 'Style 2'), ('Style3', 'Style 3')])  # 自定義字段
    wordCount = forms.IntegerField(label='字數 (200~1000字)', min_value=200, max_value=1000)  # 自定義字段
    otherRequirements = forms.CharField(label='其他要求', widget=forms.Textarea, required=False)  # 自定義字段

    class Meta:
        model = SalesForm_Data  # 指定使用的模型
        fields = ['productName', 'productFeatures', 'style', 'wordCount', 'otherRequirements']  # 包含的字段
