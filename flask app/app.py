from flask import Flask, render_template, request

app = Flask(__name__)

# List of symptoms
symptoms = ['Fever', 'Cough', 'Shortness of Breath', 'Chest Pain', 'Chills', 'Headache', 'Fatigue', 'Sore Throat']

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        # Get age from the form
        age = request.form.get('age')

        # Check if age is a valid number
        try:
            age = float(age)
        except ValueError:
            return "Age must be a valid number."

        # Get selected symptoms from the form
        selected_symptoms = request.form.getlist('symptoms')

        # Perform prediction based on age and symptoms (you can use your prediction code here)
        # For demonstration purposes, we'll just return a message with the selected symptoms
        result = f"Selected Symptoms: {', '.join(selected_symptoms)}"

    return render_template('index.html', symptoms=symptoms, result=result)

if __name__ == '__main__':
    app.run(debug=True)
