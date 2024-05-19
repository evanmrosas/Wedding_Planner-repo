// document.addEventListener('DOMContentLoaded', (event) => {
//     const messages = JSON.parse(document.getElementById('flash-messages').textContent);
//     if (messages && messages.length > 0) {
//         const alertContainer = document.getElementById('alert-container');
//         messages.forEach(message => {
//             const alertBox = document.createElement('div');
//             alertBox.className = 'alert alert-danger';
//             alertBox.role = 'alert';
//             alertBox.innerText = message;
//             alertContainer.appendChild(alertBox);
//         });
//     }
// });
document.addEventListener('DOMContentLoaded', (event) => {
    const messages = JSON.parse(document.getElementById('flash-messages').textContent);
    const alertContainer = document.getElementById('alert-container');

    // Function to display alert messages
    function displayAlerts(messages) {
        messages.forEach(message => {
            const alertBox = document.createElement('div');
            alertBox.className = 'alert alert-danger';
            alertBox.role = 'alert';
            alertBox.innerText = message;
            alertContainer.appendChild(alertBox);
        });
    }

    // Display initial flash messages
    if (messages && messages.length > 0) {
        displayAlerts(messages);
    }

    // Real-time validation
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input');
    const errorMessages = {
        first_name: 'First name required! Must have 2 characters',
        last_name: 'Last name required! Must have 2 characters',
        email: 'Invalid email address!',
        password: 'Password must contain an uppercase and lowercase letter and a number.',
        confirm_password: 'Password must match!'
    };

    function validateInput(input) {
        const name = input.name;
        let errorMessage = '';

        switch (name) {
            case 'first_name':
                if (input.value.length < 2) {
                    errorMessage = errorMessages.first_name;
                }
                break;
            case 'last_name':
                if (input.value.length < 2) {
                    errorMessage = errorMessages.last_name;
                }
                break;
            case 'email':
                const emailRegex = /^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$/;
                if (!emailRegex.test(input.value)) {
                    errorMessage = errorMessages.email;
                }
                break;
            case 'password':
                const passwordPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
                if (!passwordPattern.test(input.value)) {
                    errorMessage = errorMessages.password;
                }
                break;
            case 'confirm_password':
                const passwordInput = form.querySelector('input[name="password"]');
                if (input.value !== passwordInput.value) {
                    errorMessage = errorMessages.confirm_password;
                }
                break;
        }

        return errorMessage;
    }

    inputs.forEach(input => {
        input.addEventListener('input', () => {
            const alertBox = alertContainer.querySelector(`.alert[data-field="${input.name}"]`);
            if (alertBox) {
                alertBox.remove();
            }
            const errorMessage = validateInput(input);
            if (errorMessage) {
                const newAlertBox = document.createElement('div');
                newAlertBox.className = 'alert alert-danger';
                newAlertBox.role = 'alert';
                newAlertBox.innerText = errorMessage;
                newAlertBox.setAttribute('data-field', input.name);
                alertContainer.appendChild(newAlertBox);
            }
        });
    });
});
