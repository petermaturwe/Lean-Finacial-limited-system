// Function to show the calculator popup
function showCalculatorPopup() {
    document.getElementById('calculator-popup').style.display = 'flex';
}

// Function to hide the calculator popup
function hideCalculatorPopup() {
    document.getElementById('calculator-popup').style.display = 'none';
}

// Event listener for the calculator button
document.getElementById('calculator-button').addEventListener('click', showCalculatorPopup);

// Event listener for the close button of the calculator popup
document.querySelector('.close-button').addEventListener('click', hideCalculatorPopup);

// Event listener for the clear button
document.getElementById('clear-button').addEventListener('click', function() {
    document.getElementById('results').style.display = 'none';
});

// Event listener for the calculate button
document.getElementById('calculate-button').addEventListener('click', function() {
    // Perform calculation logic here and update the results
    // This is where you would calculate the payment details and update the DOM
    // For now, we will just show the results section
    document.getElementById('results').style.display = 'block';
});

// Prevent form from submitting as we are using button clicks to handle actions
document.getElementById('loan-form').addEventListener('submit', function(event) {
    event.preventDefault();
});
