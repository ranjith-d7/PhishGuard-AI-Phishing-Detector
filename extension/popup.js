document.addEventListener('DOMContentLoaded', function() {
    // 1. Get the current browser tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        let currentUrl = tabs[0].url;
        document.getElementById('url').innerText = currentUrl;

        // 2. Send URL to your Python Server
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: currentUrl })
        })
        .then(response => response.json())
        .then(data => {
            // 3. Show the result
            const resultDiv = document.getElementById('result');
            if (data.result === "PHISHING") {
                resultDiv.innerHTML = `<div class="danger">⚠️ PHISHING</div>Risk: ${data.risk}%`;
            } else {
                resultDiv.innerHTML = `<div class="safe">✅ SAFE</div>Risk: ${data.risk}%`;
            }
        })
        .catch(error => {
            document.getElementById('result').innerText = "Server Offline (Run python app.py)";
        });
    });
});