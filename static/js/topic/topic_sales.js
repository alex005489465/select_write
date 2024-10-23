document.addEventListener('DOMContentLoaded', function() {
    // 當DOM結構加載完成後執行
    const form = document.querySelector('form'); // 選取頁面上的第一個表單元素
    form.onsubmit = function(event) {
        event.preventDefault(); // 阻止表單的默認提交行為
        const formData = new FormData(form); // 創建一個包含表單數據的FormData對象
        const url = form.action; // 從表單的 action 屬性中獲取完整的URL
        
        fetch(url, { // 使用從表單中獲取的URL
            method: "POST", // 指定請求方法為POST
            body: formData, // 將FormData對象作為請求的body
            headers: {
                "X-CSRFToken": formData.get('csrfmiddlewaretoken') // 添加CSRF令牌到請求頭
            }
        })
        .then(response => response.json()) // 將返回的響應解析為JSON
        .then(data => {
            document.getElementById('response-text').textContent = data.response_text; // 更新頁面上的元素內容
        })
        .catch(error => console.error('Error:', error)); // 錯誤處理
    };
});
