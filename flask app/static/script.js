function predictSeverity() {
    // Get input data
    const age = document.getElementById("age").value;
    const symptoms = [];
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    checkboxes.forEach(checkbox => {
        symptoms.push(checkbox.value);
    });

    // Call API to get prediction (mocked with random values)
    const severities = [0, 1, 2];
    const severity = severities[Math.floor(Math.random() * severities.length)];

    // Display result
    document.getElementById("result").innerHTML = `Predicted Severity: ${severity}`;
}
