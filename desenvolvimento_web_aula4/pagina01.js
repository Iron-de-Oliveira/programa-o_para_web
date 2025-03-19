console.log("JS carregado")

function carregar_dados(){
   let altura = localStorage.getItem("altura");
   let nome = localStorage.getItem("nome"); 
   let genero = localStorage.getItem("genero");

//    let peso = document.getElementById("peso").value;
 
   if (!altura || !nome) {
    document.getElementById("display").innerHTML = "Nenhum dado armazenado.";
    return;
    }

    altura = parseFloat(altura);
    peso = parseFloat(peso);

    if(genero == "feminino"){
        document.getElementById("sign").style.filter = "drop-shadow(0px 0px 5px  rgb(255, 0, 128))";
      
    }else {if(genero == "masculino"){
        document.getElementById("man").style.filter = "drop-shadow(0px 0px 3px rgb(88, 127, 255))";
      
    }};

    document.getElementById("genero").innerHTML = `Gênero: ${genero} `;
    document.getElementById("nome01").innerHTML = `Olá ${nome}! `;
    document.getElementById("altura01").innerHTML = ` Sua altura: ${altura}m `;
    // document.getElementById("peso01").innerHTML = imc.toFixed(2);
}

function calculo_imc(altura, peso){
     return peso / (altura * altura)

}

// function cor(){
//     let cor = localStorage.getItem("genero");
//     return{
//         gen_mas: cor == "femino"? "drop-shadow(0px 0px 5px #9900ff)" : "",
//     };
// }

function resultado_IMC(imc){
    return{
        // img roxa
    abaixo: imc < 18.5 ? "Abaixo do peso" : "",cor01: "purple", 
    satura01:imc < 18.5 ? "saturate(200%) drop-shadow(0px 0px 5px #9900ff)" : "", 
        // img verde
    normal: imc >= 18.5 && imc <= 24.99 ? "Peso normal" : "", cor02: "green", 
    satura02: imc >= 18.5 && imc <= 24.99 ?"saturate(100%) drop-shadow(0px 0px 5px #00ff1a)" : "", 
        // img laranja
    acima: imc >= 25 && imc <= 29.9 ? "Acima do peso" : "", cor03:"orange", 
    satura03:imc >= 25 && imc <= 29.9 ? "saturate(100%) drop-shadow(0px 0px 5px #ff8000)" : "",
        // img vermelha
    obeso: imc >= 30 ? "Obesidade" : "", cor04: "red", 
    satura04: imc >= 30 ? "saturate(100%) drop-shadow(0px 0px 5px #ff0000)" : "",
    }
}

document.getElementById("pai").addEventListener("submit", function(event){
    event.preventDefault();
    let peso = document.getElementById("peso").value;
    let altura = localStorage.getItem("altura");
  

    altura = parseFloat(altura);
    peso = parseFloat(peso);
 

    var imc = calculo_imc(altura, peso);
    var resultado = resultado_IMC(imc);

    document.getElementById("peso01").innerHTML = imc.toFixed(2);
    
    document.getElementById("verde").style.filter = resultado.satura02;
    document.getElementById("normal").style.color = resultado.cor02;
    document.getElementById("normal").innerText = resultado.normal;

    document.getElementById("roxo").style.filter = resultado.satura01;
    document.getElementById("abaixo").style.color = resultado.cor01;
    document.getElementById("abaixo").innerText = resultado.abaixo;

    document.getElementById("laranja").style.filter = resultado.satura03;
    document.getElementById("acima").style.color = resultado.cor03;
    document.getElementById("acima").innerText = resultado.acima;

    document.getElementById("vermelho").style.filter = resultado.satura04;
    document.getElementById("obeso").style.color = resultado.cor04;
    document.getElementById("obeso").innerText = resultado.obeso;
    return false;
});
    


window.onload = carregar_dados;