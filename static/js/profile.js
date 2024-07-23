"use strict"

// DOM Variables
let emailInput = document.querySelector("#email");
let emailConfirmInput = document.querySelector("#email_confirm");
let form = document.querySelector("form")

// Callback functions
let checkForm = function(e) {
    let errorMessage = ""
    if (emailConfirmInput.value != emailInput.value) { 
        e.preventDefault();
        errorMessage = "Check that the two emails are correct and same!"
        window.alert(errorMessage)
    } else { 
        errorMessage = ""
    } 
    
}

let confirmEmail = function(e) { 
    let errorMessage = ""

    if (emailConfirmInput.value != emailInput.value) { 
        errorMessage = "The two email addresses must match."
    } else { 
        errorMessage = ""
    } 
    // Display Validity
    emailConfirmInput.setCustomValidity(errorMessage); 
    emailConfirmInput.reportValidity();
} 

// Event Listeners
emailConfirmInput.addEventListener("input", confirmEmail);
form.addEventListener("submit", checkForm);