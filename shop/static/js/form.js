document.getElementById('orderForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Perform validation
    var form = event.target;
    var username = form.elements['username'].value;
    var email = form.elements['email'].value;

    if (!username.trim()) {
        alert('Please enter a username.');
        return;
    }

    // Additional validation logic...

    // If validation passes, submit the form
    form.submit();
});