from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>MMS Radio Player</title>
  </head>
  <body>
    <h2>收聽廣播中...</h2>
    <audio controls autoplay>
      <source src="{{ url }}" type="audio/mpeg">
      您的瀏覽器不支援播放。
    </audio>
  </body>
</html>
"""

@app.route("/player")
def player():
    return render_template_string(HTML, url="http://61.219.156.163:9090")

@app.route("/")
def home():
    return "服務運行中"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
