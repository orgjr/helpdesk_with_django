function abrirModal(chamadoId) {
  fetch(`/chamado/${chamadoId}/detalhes/`) // endpoint a ser criado
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("modalBody").innerHTML = data;
      document.getElementById("modalChamado").style.display = "block";
    });
}

function fecharModal() {
  document.getElementById("modalChamado").style.display = "none";
}

// Fechar com ESC
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    fecharModal();
  }
});
