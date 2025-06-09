from flask import Flask, render_template, request

app = Flask(__name__)

hello_dict = {
    'japan': 'こんにちは世界',
    'english': 'Hello World',
    'french': 'Bonjour le monde',
    'spanish': '¡Hola Mundo!',
    'german': 'Hallo Welt',
    'chinese': '你好，世界',
    'korean': '안녕하세요 세계',
    'italian': 'Ciao mondo',
    'russian': 'Привет, мир',
    'arabic': 'مرحبا بالعالم',
}

country_names = {
    'japan': '日本語：日本語',
    'english': 'English：英語',
    'french': 'Français：フランス語',
    'spanish': 'Español：スペイン語',
    'german': 'Deutsch：ドイツ語',
    'chinese': '中文：中国語',
    'korean': '한국어：韓国語',
    'italian': 'Italiano：イタリア語',
    'russian': 'Русский：ロシア語',
    'arabic': 'العربية：アラビア語',
}


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    selected = "english"
    if request.method == "POST":
        selected = request.form.get("country", "english")
        message = hello_dict.get(selected, "Hello World")
    return render_template(
        "index.html",
        country_names=country_names,
        message=message,
        selected=selected
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
