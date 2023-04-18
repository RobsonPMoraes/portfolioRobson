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
});

// Fecha o menu quando clicar em algum item e muda o ícone para list


// vamos acionar o link pela classe nav-list

const navItem = document.querySelectorAll('.nav-item')

navItem.forEach(item =>{
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")){
            body.classList.remove("menu-nav-active")
            menuMobile.classList.replace("bi-x", "bi-list");
        }
    })
    /*Explicando o texto acima: 
navItem é um array, assim vamos varrer a array item a item com o forEach(item =>)
Assim, ao encontrar um navItem, ele vai atribuir uma função de adicionar um evento através do addEventListener.
Se no body encontrar a classList menu-nav-active (linha 25) ele vai remover essa classe (linha 26) e vai substituir o X pelo menu hamburguer (linha 27).*/ 
})

