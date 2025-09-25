from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML template
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Enter a number to see its multiplication table</h2>
    <form method="POST">
        <input type="number" name="number" required>
        <button type="submit">Generate</button>
    </form>
    {% if table %}
        <h3>Multiplication Table of {{ number }}</h3>
        <ul>
            {% for row in table %}
                <li>{{ row }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    table = []
    number = None
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            table = [f"{number} x {i} = {number*i}" for i in range(1, 11)]
        except ValueError:
            table = ["Invalid input. Please enter a number."]
    return render_template_string(HTML_TEMPLATE, table=table, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
