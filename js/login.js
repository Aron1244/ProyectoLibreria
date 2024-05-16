// Función para manejar el inicio de sesión
function iniciarSesion(event) {
    event.preventDefault(); // Evita que el formulario se envíe y la página se recargue

    const usuario = document.getElementById('inputUsuario').value;
    const contra = document.getElementById('inputContra').value;

    // Valores de "super usuario"
    const superUsuario = 'admin';
    const superContra = 'admin123';

    // Verifica si el usuario y la contraseña coinciden
    if (usuario === superUsuario && contra === superContra) {
        alert('Inicio de sesión exitoso!');
        // Redirigir a otra página o realizar alguna acción adicional aquí
    } else {
        alert('Usuario o contraseña incorrectos. Inténtelo de nuevo.');
    }

    return false; // Impide el envío del formulario
}