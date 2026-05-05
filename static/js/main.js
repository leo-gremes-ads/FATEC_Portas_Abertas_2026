(function() {
  "use strict";


  /**
   * AOS (animação do bem-vindo)
   */
  function aosInit() {
    if (typeof AOS !== "undefined") {
      AOS.init({
        duration: 600,
        easing: 'ease-in-out',
        once: true,
        mirror: false
      });
    }
  }
  window.addEventListener('load', aosInit);

//CADASTRO

const btnSeguinte = document.getElementById("btn-seguinte");

if (btnSeguinte) {
  btnSeguinte.addEventListener("click", function () {

    const nome = document.querySelector('input[name="name"]').value.trim();
    const email = document.querySelector('input[name="email"]').value.trim();
    const telefone = document.querySelector('input[name="phone"]').value.trim();
    const escolaridade = document.querySelector('select[name="education"]').value;

    const areas = document.querySelectorAll('input[name="areas[]"]:checked');

    if (!nome) return alert("Preencha o nome");
    if (!email) return alert("Preencha o email");

    if (!email.includes("@") || !email.includes(".")) {
      return alert("Digite um email válido");
    }

    if (!escolaridade) return alert("Selecione a escolaridade");

    if (areas.length === 0) return alert("Selecione pelo menos uma área de interesse");

    //window.location.href = "oraculo.html";
  });
}

//ORACULO

const form = document.getElementById("oraculo-form");
const resultado = document.getElementById("resultado-oraculo");
const btnVoltar = document.getElementById("btn-voltar");

if (form) {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const cor = document.querySelector('input[name="cor"]:checked')?.value;
    const pedra = document.querySelector('input[name="pedra"]:checked')?.value;

    if (!cor || !pedra) {
      alert("Selecione cor e pedra");
      return;
    }

    //const mensagem = `A combinação de ${cor} e ${pedra} revela um novo caminho.`;

    document.getElementById("mensagem").innerText = MENSAGEM;

    // 🔥 troca de telas
    form.classList.add("hidden");
    resultado.classList.remove("hidden");
  });
}

if (btnVoltar) {
  btnVoltar.addEventListener("click", function () {
    // volta para o formulário
    //form.classList.remove("hidden");
    //resultado.classList.add("hidden");
    window.location.href = "/";

    // opcional: limpar seleção
    document.querySelectorAll('input[name="cor"]').forEach(i => i.checked = false);
    document.querySelectorAll('input[name="pedra"]').forEach(i => i.checked = false);
  });
}


})();