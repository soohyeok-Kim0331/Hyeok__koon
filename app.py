from flask import Flask, render_template
app = Flask(__name__)
student_data = {
    1: {"name": "superman", "score": {"english": 90, "math": 65}},
    2: {"name": "wonderwoman", "score": {"english": 75, "korean": 80, "math": 75}}
}

@app.route('/')
def index():
    return render_template("index.html",
            template_students = student_data)


@app.route("/student/<int:id>")
def student(id):
    return render_template("student.html",
            template_name=student_data[id]["name"],
            template_score=student_data[id]["score"])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5009')