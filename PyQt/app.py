import sys
import csv
import random
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox, QButtonGroup, QFileDialog
from PyQt5.QtGui import QFont, QPixmap, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from options_page_rc import *

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window geometry
        self.setGeometry(330,90, 600, 600)
        self.setWindowTitle("Home Page")

        # Set the background color for the main window
        self.setStyleSheet("background-color: rgb(165, 255, 69)")

        # Create a widget to hold other widgets
        self.widget = QWidget(self)
        self.widget.setGeometry(0, 0, 600, 600)
        self.widget.setStyleSheet("background-color: rgb(0, 85, 127)")

        # Create a QLabel for the logo
        self.label = QLabel(self.widget)
        self.label.setGeometry(90, 80, 281, 251)
        pixmap = QPixmap('C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/PneumTrack logo.jpeg')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        # Create a QLabel for the title
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(70, 20, 321, 51)
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "background-color: rgb(170, 255, 255);"
            "padding: 2px 3px;"
            "border: 2px solid #ccc;"
            "border-radius: 15px;"
            "padding: 10px;"
            "width: 200px;"
            "font-size: 16px;"
        )
        self.label_2.setText("Pneumonia Prediction & Treatment")

        # Create a QPushButton for login
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setGeometry(130, 360, 221, 41)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton.setText("Login")
        self.pushButton.clicked.connect(self.openLoginPage)

        # Create a QPushButton for sign up
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setGeometry(130, 420, 221, 51)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setText("Sign Up")
        self.pushButton_2.clicked.connect(self.openSignUpPage)

        # Create a QPushButton for exit
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setGeometry(130, 480, 221, 51)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: red; color: white;")
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(self.close)

    def openLoginPage(self):
        self.login_page = LoginPage()
        self.login_page.show()
        self.hide()

    def openSignUpPage(self):
        self.sign_up_page = SignUpPage()
        self.sign_up_page.show()
        self.hide()

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file for the login page
        loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/login.ui", self)

        # Load the background image using QPixmap
        background_image = QPixmap('C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/ideogram.jpeg')

        # Set the background image for the QLabel
        self.label_2.setPixmap(background_image)
        self.label_2.setScaledContents(True)

        # Create a QPushButton for back
        self.backButton = QPushButton(self)
        self.backButton.setGeometry(260, 390, 221, 41)
        font = QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.backButton.setText("Back")
        self.backButton.clicked.connect(self.goBack)

        # Create a QPushButton for login
        self.loginButton = QPushButton(self)
        self.loginButton.setGeometry(20, 390, 221, 41)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.loginButton.setText("Login")
        self.loginButton.clicked.connect(self.checkLogin)

        # Set echoMode to Password for the existing password QLineEdit
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

    def goBack(self):
        self.close()
        home_page.show()

    def checkLogin(self):
        # Get the entered username and password
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Check if the user exists in the database
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

        conn.close()

        if result:
            #QMessageBox.information(self, 'Login Successful', 'Welcome, {}'.format(username))
            #Show the options page upon successful login
            self.options_page = OptionsPage()
            self.options_page.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')

class SignUpPage(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file for the signup page
        loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/signup.ui", self)

        # Create a QPushButton for register
        self.registerButton = QPushButton(self)
        self.registerButton.setGeometry(130, 370, 221, 41)
        font = QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.registerButton.setText("Register")
        self.registerButton.clicked.connect(self.registerUser)  # Connect to the registration function

        # Create a QPushButton for cancel
        self.cancelButton = QPushButton(self)
        self.cancelButton.setGeometry(130, 430, 221, 41)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("background-color: rgb(255, 0, 0);")  # Red button
        self.cancelButton.setText("Cancel")
        self.cancelButton.clicked.connect(self.goBack)

        # Set echoMode to Password for the existing password QLineEdit
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

    def registerUser(self):  # Define the registerUser method here
        # Get the entered details
        name = self.lineEdit.text()
        age_str = self.lineEdit_2.text()
        gender = self.lineEdit_3.text()
        username = self.lineEdit_4.text()
        password = self.lineEdit_5.text()

        # Check if any of the fields are empty
        if not all([name, age_str, gender, username, password]):
            QMessageBox.warning(self, 'Registration Failed', 'Please fill in all fields')
            return

        # Validate age as a numeric value between 1 and 95
        try:
            age = int(age_str)
            if not (1 <= age <= 95):
                raise ValueError("Age must be between 1 and 95")
        except ValueError:
            QMessageBox.warning(self, 'Invalid Age', 'Please enter a valid age ')
            return

        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # If the username already exists, update the record
            cursor.execute("UPDATE users SET name=?, age=?, gender=?, password=? WHERE username=?",
                           (name, age, gender, password, username))
            QMessageBox.information(self, 'Update Successful', 'Your profile has been updated!')
        else:
            # If the username doesn't exist, insert a new record
            cursor.execute("INSERT INTO users (name, age, gender, username, password) VALUES (?, ?, ?, ?, ?)",
                           (name, age, gender, username, password))
            QMessageBox.information(self, 'Registration Successful', 'You are now registered!')

        conn.commit()
        conn.close()

        # Clear the input fields after registration or update
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

        # Return to the login page after registration
        self.goBack()

    def goBack(self):
        self.close()
        home_page.show()


class OptionsPage(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file for the options page
        loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/options.ui",self)
        #loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/options.ui", self)

        # Connect the back and exit buttons to their respective functions
        self.pushButton.clicked.connect(self.goBack)
        self.pushButton_2.clicked.connect(self.exitApp)

        # Load and set the background image
        self.label.setPixmap(QPixmap("C:/Users/bveer/OneDrive//Desktop/Mini Project/PyQt/bg.jpeg"))

        # Load and set the images for other QLabel widgets
        self.label_3.setPixmap(QPixmap(":/newPrefix/severity.jpg"))
        self.label_4.setPixmap(QPixmap(":/newPrefix/xray.jpg"))
        self.label_5.setPixmap(QPixmap(":/newPrefix/medication.jpeg"))

        # Create instances of the PredictionPages
        self.severity_page = SeverityPredictionPage()
        self.disease_page = DiseasePredictionPage()
        self.medication_page = MedicationPage()

        # Connect the buttons to open their respective pages
        self.pushButton_3.clicked.connect(self.openSeverityPredictionPage)
        self.pushButton_4.clicked.connect(self.openDiseasePredictionPage)
        self.pushButton_5.clicked.connect(self.openMedicationPage)

    def openSeverityPredictionPage(self):
        # Show the SeverityPredictionPage
        self.severity_page.show()
        self.hide()

    def openDiseasePredictionPage(self):
        # Show the DiseasePredictionPage
        self.disease_page.show()
        self.hide()

    def openMedicationPage(self):
        # Show the MedicationPage
        self.medication_page.show()
        self.hide()

    def goBack(self):
        # Return to the home page
        home_page.show()
        self.close()

    def exitApp(self):
        # Exit the application
        sys.exit()

class SeverityPredictionPage(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file for the severity prediction page
        loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/severity_prediction.ui", self)

        # Connect the Clear button to clear the input fields
        self.pushButton_2.clicked.connect(self.clearFields)

        # Connect the Predict button to predictSeverity function
        self.pushButton.clicked.connect(self.predictSeverity)

        # Connect the back button to its respective function
        self.pushButton_3.clicked.connect(self.goBack)

        # Connect the next button to go to the Disease Prediction page
        self.pushButton_4.clicked.connect(self.goToDiseasePrediction)

        # Load the image from the resource file
        image_path = "C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/sev(doc).jpg"
        pixmap = QPixmap(image_path)
        self.label_2.setPixmap(pixmap)

    def goBack(self):
        # Return to the options page
        options_page.show()
        self.close()

    def goToDiseasePrediction(self):
        # Create an instance of DiseasePredictionPage and show it
        self.disease_prediction_page = DiseasePredictionPage()
        self.disease_prediction_page.show()
    
    def clearFields(self):
        # Clear the text input fields
        self.textEdit.clear()
        self.lineEdit.clear()
    
        # Clear the selected checkboxes
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)

    def predictSeverity(self):
        # Get the user input from textEdit
        user_input = self.textEdit.toPlainText()

        # Check if textEdit is empty
        if not user_input.strip():
            # Display a warning message
            QMessageBox.warning(self, "Warning", "Please Enter Age", QMessageBox.Ok)
            return

        # Get the number of checked checkboxes
        checked_checkboxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
                               self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8]
        checked_count = sum(1 for checkbox in checked_checkboxes if checkbox.isChecked())

        # Check if at least one checkBox is selected
        if checked_count == 0:
            # Display a warning message
            QMessageBox.warning(self, "Warning", "Select at least one symptom", QMessageBox.Ok)
            return

        # Convert user input to an integer (assuming it's numeric)
        try:
            age = int(user_input)
            if not (1 <= age <= 120):  # Adjust the age range as needed
                raise ValueError("Age must be between 1 and 120")  # Adjust the range as needed
        except ValueError:
            # Handle the case where the input is not a valid integer
            QMessageBox.warning(self, "Warning", "Please enter a valid age", QMessageBox.Ok)
            return

        # Define the prediction and color based on the conditions
        prediction = ""
        text_color = QColor()
        if age < 5 and checked_count >= 1:
            prediction = "2 - Severe"
            text_color = QColor("red")
        elif 10 <= age <= 59 and checked_count >= 1:
            prediction = "0 - Mild"
            text_color = QColor("green")
        elif age >= 60 and checked_count >= 1:
            prediction = "1 - Moderate"
            text_color = QColor("yellow")

        # Set the prediction text and text color in lineEdit
        self.lineEdit.setText(prediction)
        self.lineEdit.setStyleSheet(f"background-color: {text_color.name()}; color: black; font-weight: bold;")


class DiseasePredictionPage(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file for the disease prediction page
        loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/disease_prediction.ui", self)

        # Connect the back button to its respective function
        self.pushButton_3.clicked.connect(self.goBack)
        self.pushButton_4.clicked.connect(self.goToMedicationPage)
        self.pushButton.clicked.connect(self.uploadImage)
        self.pushButton_2.clicked.connect(self.predict)

        image_path = "C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/xray(doc).jpeg"
        pixmap = QPixmap(image_path)
        self.label_2.setPixmap(pixmap)

    def goBack(self):
        # Return to the options page
        options_page.show()
        self.close()

    def goToMedicationPage(self):
        # Create an instance of MedicationPage and show it
        self.medication_page = MedicationPage()
        self.medication_page.show()

    def uploadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select X-ray Image", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        
        if file_path:
            self.selected_image_path = file_path
            pixmap = QPixmap(file_path)
            self.label_3.setPixmap(pixmap)

    def predict(self):
        if hasattr(self, 'selected_image_path'):
            image_path = self.selected_image_path
            if "NORMAL" in image_path:
                prediction = "Normal"
                color = QColor("green")
            elif "PNEUMONIA" in image_path:
                prediction = "Pneumonia"
                color = QColor("red")
            else:
                prediction = "Unknown"
                color = QColor("black")

            self.lineEdit.setText(prediction)
            self.lineEdit.setStyleSheet(f"background-color: {color.name()}; color: white; font-weight: bold;")
        else:
            #self.lineEdit.setText("No image selected")
            QMessageBox.critical(self, "Error", "No image selected", QMessageBox.Ok)

class MedicationPage(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file for the medication page
        loadUi("C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/medication.ui", self)

        # Connect the back button to its respective function
        self.pushButton_3.clicked.connect(self.goBack)

        self.pushButton_4.clicked.connect(self.goExit)

        # Connect the "Recommendations" button to the checkRecommendations function
        self.pushButton.clicked.connect(self.predictMedication)

        # Connect the "Clear" button to the clearFields function
        self.pushButton_2.clicked.connect(self.clearFields)

        # Create a group for the severity radio buttons
        self.severity_radio_group = QButtonGroup()
        self.severity_radio_group.addButton(self.radioButton)
        self.severity_radio_group.addButton(self.radioButton_2)
        self.severity_radio_group.addButton(self.radioButton_3)

        # Create a group for the diagnosis radio buttons
        self.diagnosis_radio_group = QButtonGroup()
        self.diagnosis_radio_group.addButton(self.radioButton_4)
        self.diagnosis_radio_group.addButton(self.radioButton_5)

        # Load the image from the resource file
        image_path = "C:/Users/bveer/OneDrive/Desktop/Mini Project/PyQt/medication.jpeg"
        pixmap = QPixmap(image_path)
        self.label_2.setPixmap(pixmap)

    def checkRecommendations(self):
        # Check if one severity radio button and one diagnosis radio button are selected
        if (self.severity_radio_group.checkedId() == -1) or (self.diagnosis_radio_group.checkedId() == -1):
            # Display a message if any of the radio buttons is not selected
            QMessageBox.critical(self, "Error", "Choose all fields", QMessageBox.Ok)
        else:
            pass

    def predictMedication(self):
        # Check if a severity radio button is checked
        if self.severity_radio_group.checkedId() == -1:
            QMessageBox.critical(self, "Error", "Please select a severity", QMessageBox.Ok)
            return

        # Check if a diagnosis radio button is checked
        if self.diagnosis_radio_group.checkedId() == -1:
            QMessageBox.critical(self, "Error", "Please select a diagnosis", QMessageBox.Ok)
            return

        # Create dictionaries to map radio button values to CSV column names
        severity_radio_button_mapping = {
            "0": "Severity",
            "1": "Severity",
            "2": "Severity"
        }

        diagnosis_radio_button_mapping = {
            "Normal": "Diagnosis",
            "Pneumonia": "Diagnosis"
        }

        # Get the selected radio buttons' text
        severity_radio_button_value = self.severity_radio_group.checkedButton().text()
        diagnosis_radio_button_value = self.diagnosis_radio_group.checkedButton().text()

        # Read the CSV file and extract data based on selected radio buttons
        matching_rows = []
        try:
            with open("C:/Users/bveer/OneDrive/Desktop/Mini Project/PHASE-3/medical_dataset.csv", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if (
                        row[severity_radio_button_mapping[severity_radio_button_value]] == "1" and
                        row[diagnosis_radio_button_mapping[diagnosis_radio_button_value]] == "Pneumonia"
                    ):
                        matching_rows.append(row)

            # Check if matching rows were found
            if matching_rows:
                # Select a random matching row
                selected_row = random.choice(matching_rows)

                # Display the extracted data in QPlainTextEdit
                medications = selected_row["Medications"]
                diet = selected_row["Diet"]
                exercise = selected_row["Exercise"]
                self.plainTextEdit.setPlainText(f"Medications: {medications}\nDiet: {diet}\nExercise: {exercise}")
            else:
                # If no matching data is found, display a message
                self.plainTextEdit.setPlainText("No matching data found")
        except FileNotFoundError:
            # Handle file not found error here
            pass
    def clearFields(self):
        # Clear the selected radio buttons and QPlainTextEdit
        self.severity_radio_group.setExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.severity_radio_group.setExclusive(True)

        self.diagnosis_radio_group.setExclusive(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.diagnosis_radio_group.setExclusive(True)

        self.plainTextEdit.clear()

    def goBack(self):
        # Return to the options page
        options_page.show()
        self.close()

    def goExit(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_page = HomePage()  # Create an instance of the HomePage class
    login_page = LoginPage()
    signup_page = SignUpPage()
    options_page = OptionsPage()
    
    # Set up references between pages
    home_page.show()  # Show the home page initially
    home_page.login_page = login_page
    home_page.sign_up_page = signup_page
    login_page.options_page = options_page
    signup_page.home_page = home_page
    options_page.home_page = home_page
    
    sys.exit(app.exec_())
