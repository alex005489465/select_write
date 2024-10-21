# topic/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SalesForm
from .models import SalesForm_Data

def sales(request):
    return render(request, 'topic/sales.html')

def handle_sales_form(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            # 提取乾淨數據
            productName = form.cleaned_data['productName']
            productFeatures = form.cleaned_data['productFeatures']
            style = form.cleaned_data['style']
            wordCount = form.cleaned_data['wordCount']
            otherRequirements = form.cleaned_data['otherRequirements']
            
            # 保存乾淨數據到數據庫
            sales_data = SalesForm_Data(
                productName=productName,
                productFeatures=productFeatures,
                style=style,
                wordCount=wordCount,
                otherRequirements=otherRequirements
            )
            sales_data.save()

            # 處理數據並生成回應
            response_text = f"""
            
            description: 
            本模塊旨在幫助用戶模仿雷軍的演講風格，運用誇張的數據和百分比、口語化的語言、故事性的描述和創新挑戰的強調，將平凡的事物描述得引人注目。

            Background:
            雷軍以其獨特的演講風格聞名，特別擅長使用數據和百分比來強調事物的重要性和影響力，同時也善於運用情感化的語言、生動的故事和創新挑戰的描述，使得聽眾對於平凡事物產生極大的興趣。

            Goals:
            利用數字和百分比來誇大事物的重要性和效果。
            強調產品或觀點的創新性和克服的挑戰。
            和同類產品進行各種參數的對比。
            必須恰當地融入 [Tone] 中的經典語錄。

            Constrains:
            保持演講內容的真實性，不要完全脫離事實。
            使用的數據和百分比雖然誇張，但需要在合理的範圍內。
            確保演講內容易於理解，避免過於複雜的數據或術語。
            描述產品價格時不要過度煽情。
            生成字數 {wordCount} 字。

            Attention:
            絕對避免出現 “首先、其次、總而言之、想象一下”
            絕對避免出現 “你沒聽錯”“大吃一驚”
            避免書面語，加入更多口語元素
            避免出現煽情的語句，全程採用誠懇的表達

            Tone:
            科普性質較為濃厚，喜歡針對某幾個參數、技術進行科普。
            凸顯出真誠，“這個成本真的真的很高了，所以價格不會低的……”
            經典語錄：“不服跑個分”“我連夜睡服了高管，降價到……”

            (以上這些是從網路上抄來的提示詞)
            
            
            產品名稱: {productName}
            產品特性: {productFeatures}
            風格: {style}
            字數: {wordCount}
            其他要求: {otherRequirements}

            感謝您使用我們的服務！
            """

            
            # 渲染 sales_output.html 並傳遞 response_text
            return render(request, 'topic/sales_output.html', {'response_text': response_text})
    else:
        form = SalesForm()
        return render(request, 'topic/sales.html', {'form': form})

