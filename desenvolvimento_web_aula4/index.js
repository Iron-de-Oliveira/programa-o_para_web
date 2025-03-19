console.log("java script carregado")

let genero = ""
function genero_feminino(){

    genero = "feminino";
  
    document.getElementById("resultado").innerHTML = genero;
    localStorage.setItem("genero", genero);
    console.log("genero add")
    
}

function genero_masculino(){

    genero = "masculino";
  
    document.getElementById("resultado").innerHTML = genero;
    localStorage.setItem("genero", genero);
    console.log("genero add")
}

document.getElementById("formulario").addEventListener("submit", function(event){
    event.preventDefault();

    let altura = document.getElementById("altura").value;
    let nome = document.getElementById("nome").value;
    // let genero = document.getElementById("genero").value;

    if (!altura || !nome) {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    localStorage.setItem("altura", altura);
    localStorage.setItem("nome", nome);
   
    


    window.location.href = "pagina1.html";
});
