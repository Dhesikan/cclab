from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_cgpa():
    cgpa = None
    if request.method == 'POST':
        try:
            a = int(request.form.get('maths'))
            b = int(request.form.get('agile'))
            c = int(request.form.get('dbms'))
            d = int(request.form.get('java'))
            e = int(request.form.get('cn'))
            i = int(request.form.get('ids'))
            f = int(request.form.get('java_lab'))
            g = int(request.form.get('dbms_lab'))
            h = int(request.form.get('ss'))

            # CGPA Calculation
            total = (4*a) + (4*b) + (3*c) + (3*d) + (3*e) + (3*i) + (2*f) + (2*g) + h
            cgpa = total / 25
        except ValueError:
            cgpa = "Invalid input. Please enter valid numbers."

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CGPA Calculator</title>
    </head>
    <body>
        <h1>CGPA Calculator</h1>
        <form method="post">
            <label for="maths">Maths:</label>
            <input type="number" id="maths" name="maths" required>
            <br>
            <label for="agile">Agile:</label>
            <input type="number" id="agile" name="agile" required>
            <br>
            <label for="dbms">DBMS:</label>
            <input type="number" id="dbms" name="dbms" required>
            <br>
            <label for="java">Java:</label>
            <input type="number" id="java" name="java" required>
            <br>
            <label for="cn">CN:</label>
            <input type="number" id="cn" name="cn" required>
            <br>
            <label for="ids">IDS:</label>
            <input type="number" id="ids" name="ids" required>
            <br>
            <label for="java_lab">Java Lab:</label>
            <input type="number" id="java_lab" name="java_lab" required>
            <br>
            <label for="dbms_lab">DBMS Lab:</label>
            <input type="number" id="dbms_lab" name="dbms_lab" required>
            <br>
            <label for="ss">SS:</label>
            <input type="number" id="ss" name="ss" required>
            <br>
            <button type="submit">Calculate CGPA</button>
        </form>
        {% if cgpa is not none %}
            <h2>CGPA: {{ cgpa }}</h2>
        {% endif %}
    </body>
    </html>
    ''', cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
