// Función para mostrar mensajes de alerta si existen
document.addEventListener('DOMContentLoaded', function() {
    const mensajes = document.getElementById('idMensajes');
    if (mensajes && mensajes.innerText.trim() !== '') {
        alert(mensajes.innerText.trim());
    }

    const errorMessage = document.querySelector('#error-message')?.dataset?.message;
    if (errorMessage) {
        showErrorMessage(errorMessage);
    }

    validateForm();
});

// Función para actualizar el contenido de la página
function actualizarContenido() {
    // Aquí podrías hacer una solicitud AJAX para obtener nuevos datos y actualizar el DOM
    console.log('Actualizar contenido');
}

// Función para validar formularios antes de enviarlos
function validarFormulario() {
    const formulario = document.querySelector('form');
    formulario.addEventListener('submit', (event) => {
        const esValido = validateForm(); // Llama a la función validateForm
        if (!esValido) {
            event.preventDefault(); // Detener el envío del formulario si no es válido
            alert('Por favor, completa todos los campos requeridos.');
        }
    });
}

// Función para validar la contraseña y otros campos
function validateForm() {
    let errors = [];
    const password1 = document.querySelector("#id_password1")?.value;
    const password2 = document.querySelector("#id_password2")?.value;

    if (password1 && password2 && password1 !== password2) {
        errors.push("Las contraseñas no coinciden.");
    }

    if (errors.length > 0) {
        const errorDiv = document.getElementById("errors");
        errorDiv.innerHTML = "";
        errors.forEach(error => {
            const errorElement = document.createElement("p");
            errorElement.textContent = error;
            errorDiv.appendChild(errorElement);
        });
        return false;
    }
    return true;
}

// Función para mostrar mensajes de error
function showErrorMessage(message) {
    const errorMessageDiv = document.getElementById('error-message');
    if (errorMessageDiv) {
        errorMessageDiv.textContent = message;
        errorMessageDiv.style.display = 'block';
    }
}

// Evento para manejar el scroll y añadir una clase al navbar
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 50) { // Ajusta este valor según tus necesidades
            navbar.classList.add('navbar-scroll');
        } else {
            navbar.classList.remove('navbar-scroll');
        }
    }
});

// Ejecutar las funciones al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    actualizarContenido();
    validarFormulario();
});
