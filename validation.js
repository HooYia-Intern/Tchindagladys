















function validateForm() {
     let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    
    let confirmPassword = document.getElementById("confirm-password").value;
    let fullname = document.getElementById("fullname").value;

    let isValid = true;

let emailpattern=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;
let passwordpattern= /.{7,}/;
let fullnamePattern = /^[A-Z]+$/;

if(!email.match(emailpattern)){
    alert('please enter a valid email address')
    return false;
}
if(!fullname.match(fullnamePattern)){
    alert('full name must be in uppercase letters only.');
    return false;
}
alert('registration successful!');
return true;
}