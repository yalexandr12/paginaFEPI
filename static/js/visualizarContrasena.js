function togglePassword(inputId,nameId) {
    var passwordInput = document.getElementById(nameId);
    var showPasswordBtn = document.getElementById("show-password-btn-" + inputId);
    var showPasswordIcon = document.getElementById("myIcon-" + inputId);

    function showPassword() {
        passwordInput.type = "text";
        showPasswordIcon.classList.remove("fa-eye-slash");
        showPasswordIcon.classList.add("fa-eye");
    }

    function hidePassword() {
        passwordInput.type = "password";
        showPasswordIcon.classList.remove("fa-eye");
        showPasswordIcon.classList.add("fa-eye-slash");
    }

    showPasswordBtn.addEventListener("mousedown", showPassword);
    showPasswordBtn.addEventListener("mouseup", hidePassword);
}
setTimeout(function(){
            document.querySelector('.transition').classList.add('show');
        }, 100);