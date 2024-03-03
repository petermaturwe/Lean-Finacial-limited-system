document.getElementById('pay-button').addEventListener('click', function() {
    var form = document.getElementById('payment-form');
    var successMessage = document.getElementById('success-message');

    // Hide the form
    form.style.display = 'none';

    // Show the success message
    successMessage.classList.remove('hidden');
});

document.getElementById('save-transaction').addEventListener('click', function() {
    // Here you can handle the saving of the transaction
    alert('Transaction saved!'); // Placeholder for demonstration
});
