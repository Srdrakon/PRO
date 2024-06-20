document.addEventListener('DOMContentLoaded', function() {
    const mensajes = document.getElementById('idMensajes');
    if (mensajes && mensajes.innerText.trim() !== '') {
        alert(mensajes.innerText.trim());
    }
});
document.addEventListener('DOMContentLoaded', () => {
    // Funcionalidad para actualizar dinámicamente el contenido de la página
    function actualizarContenido() {
        // Aquí podrías hacer una solicitud AJAX para obtener nuevos datos y actualizar el DOM
        console.log('Actualizar contenido');
    }

    // Funcionalidad para validar formularios antes de enviarlos
    function validarFormulario() {
        const formulario = document.querySelector('form');
        formulario.addEventListener('submit', (event) => {
            // Validar los campos del formulario aquí
            const esValido = true; // Cambiar según la lógica de validación
            if (!esValido) {
                event.preventDefault(); // Detener el envío del formulario si no es válido
                alert('Por favor, completa todos los campos requeridos.');
            }
        });
    }

    // Ejecutar las funciones al cargar la página
    actualizarContenido();
    validarFormulario();
});
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if(window.scrollY > 50) { // Ajusta este valor según tus necesidades
        navbar.classList.add('navbar-scroll');
    } else {
        navbar.classList.remove('navbar-scroll');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const errorMessage = document.querySelector('#error-message').dataset.message;
    if (errorMessage) {
        showErrorMessage(errorMessage);
    }
});

function showErrorMessage(message) {
    const errorMessageDiv = document.getElementById('error-message');
    errorMessageDiv.textContent = message;
    errorMessageDiv.style.display = 'block';
}
function showErrorMessage(message) {
    const errorMessageDiv = document.getElementById('error-message');
    errorMessageDiv.textContent = message;
    errorMessageDiv.style.display = 'block';
}
function validateForm() {
    var errors = [];
    var password1 = document.querySelector("#id_password1").value;
    var password2 = document.querySelector("#id_password2").value;
    
    if (password1 !== password2) {
        errors.push("Las contraseñas no coinciden.");
    }

    if (errors.length > 0) {
        var errorDiv = document.getElementById("errors");
        errorDiv.innerHTML = "";
        for (var i = 0; i < errors.length; i++) {
            var error = document.createElement("p");
            error.textContent = errors[i];
            errorDiv.appendChild(error);
        }
        return false;
    }
    return true;
}
