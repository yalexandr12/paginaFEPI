const correo = document.getElementById('correo');
const contrasena = document.getElementById('pass');
const confirmarContrasena = document.getElementById('passConfir')

correo.addEventListener('input', () => {
    const patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!patronCorreo.test(correo.value)) {
      correo.setCustomValidity('Ingrese un correo electrónico válido');
    } else {
      correo.setCustomValidity('');
    }
  });

contrasena.addEventListener('input', () => {
    const patronContrasena = /^(?=.*[A-Z])(?=.*\d)(?=.*[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~])[A-Za-z\d!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]{6,10}$/;
    if (!patronContrasena.test(contrasena.value)) {
        contrasena.setCustomValidity('Escriba una contraseña con las caracteristicas especificadas');
    } else {
        contrasena.setCustomValidity('');
    }
});

confirmarContrasena.addEventListener('input', () => {
  if (contrasena.value != confirmarContrasena.value){
    confirmarContrasena.setCustomValidity('Las contraseñas no coinciden');
  } else {
    confirmarContrasena.setCustomValidity('');
  }
});
