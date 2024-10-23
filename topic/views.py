# topic/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import SalesForm
from .models import SalesForm_Data
from .sales.topic_sales_data_processing import process_sales_data

#topic/sales
def sales(request):
    return render(request, 'topic/sales/sales.html')

def handle_sales_form(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            # 使用新模塊處理表單數據
            response_text = process_sales_data(form)
            
            # 返回字串作為JSON回應
            return JsonResponse({'response_text': response_text})
            
            """
            # 渲染 sales_output.html 並傳遞 response_text
            return render(request, 'topic/sales/sales_output.html', {'response_text': response_text})
            """
        else:
            return JsonResponse({'error': 'Form is not valid'}, status=400)
    else:
        form = SalesForm()
        return render(request, 'topic/sales/sales.html', {'form': form})

