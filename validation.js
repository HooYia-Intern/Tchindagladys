function validateForm() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    
    let confirmPassword = document.getElementById("confirm-password").value;
    let fullname = document.getElementById("fullname").value;

    let isValid = true;

   
    if (fullname.trim() === "") {
        fullnameError.textContent = "fullname is required.";
        fullnameError.style.display = "block";
        isValid = false;
    } else {
        fullnameError.style.display = "none";
    }

    
    if (email.trim() === "") {
        emailError.textContent = "Email is required.";
        emailError.style.display = "block";
        isValid = false;
    } else if (!validateEmail(email)) {
        emailError.textContent = "Please enter a valid email address.";
        emailError.style.display = "block";
        isValid = false;
    } else {
        emailError.style.display = "none";
    }

    
    if (password.trim() === "") {
        passwordError.textContent = "Password is required.";
        passwordError.style.display = "block";
        isValid = false;
    } else if (password.length < 8) {
        passwordError.textContent = "Password must be at least 8 characters long.";
        passwordError.style.display = "block";
        isValid = false;
    } else {
        passwordError.style.display = "none";
    }

    
    if (confirmPassword.trim() === "") {
        confirmPasswordError.textContent = "Confirm password is required.";
        confirmPasswordError.style.display = "block";
        isValid = false;
    } else if (confirmPassword !== password) {
        confirmPasswordError.textContent = "Passwords do not match.";
        confirmPasswordError.style.display = "block";
        isValid = false;
    } else {
        confirmPasswordError.style.display = "none";
    }

    return isValid;
}

function validateEmail(email) {
    // Regular expression for email validation
    const re = /^[^s@]+@[^s@]+.[^s@]+$/;
    return re.test(email);
}