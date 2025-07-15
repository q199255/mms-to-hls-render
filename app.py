from flask import Flask, Response, render_template_string
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <h2>收聽廣播中…</h2>
    <audio controls autoplay>
        <source src="/stream.mp3" type="audio/mpeg">
        您的瀏覽器不支援音訊播放。
    </audio>
    '''

@app.route("/stream.mp3")
def stream_audio():
    mms_url = "mms://61.219.156.163:9090"
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", mms_url,
        "-vn",
        "-acodec", "libmp3lame",
        "-ar", "44100",
        "-f", "mp3",
        "-"
    ]
    process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    def generate():
        try:
            while True:
                data = process.stdout.read(1024)
                if not data:
                    break
                yield data
        finally:
            process.kill()

    return Response(generate(), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

