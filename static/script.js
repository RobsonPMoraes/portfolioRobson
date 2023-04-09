// Abrir e fechar o menu lateral em modo mobile

const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click', () =>{
    menuMobile.classList.contains("bi-list") //Se em menuMobile na lista de classes contém uma classe bi-list
    // Ao encontrar a classe bi-list, fazemos um condicional ternário que diz:
    // Se menuMobile encontrar a classe bi-list, troca pelo ícone bi-x e vice versa.
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list");
    // Adicionando uma classe ao body para fazer o header aparecer
    body.classList.toggle("menu-nav-active")
})