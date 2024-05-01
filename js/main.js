// Función para cambiar entre los modos claro y oscuro
const cambiarModo = () => {
  const body = document.body;
  body.classList.toggle("light-mode");
  body.classList.toggle("dark-mode");

  // Guarda el modo actual en el almacenamiento local para mantenerlo entre sesiones
  const modoActual = body.classList.contains("light-mode") ? "light" : "dark";
  localStorage.setItem("modo", modoActual);
};

// Agrega un event listener al botón de cambio de modo
document.getElementById("modo-btn").addEventListener("click", cambiarModo);

// Verifica si hay un modo guardado en el almacenamiento local y aplícalo
const modoGuardado = localStorage.getItem("modo");
if (modoGuardado === "dark") {
  cambiarModo();
}

