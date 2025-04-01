function saveform(){
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const mensagem = document.getElementById("mensagem").value;

    // verificar se existem dados salvos on lovalStorage
let saveData  = JSON.parse(localStorage.getItem("formData")) || []

// cria um objeto para os dados do formlário
const FormData  = {
    name: name,
    email: email,
    senha: senha,
    mensagem: mensagem
}

// adiciona os dados ao array
    saveData.push(FormData)

// salvar o array no localstorage
localStorage.setItem("FormData", JSON.stringify(saveData));

// exibir alerta de sucesso
alert("sucesso")

// lipar fomrulario
 clearform();
};

function clearform(){
    document.getElementsById("mensagem").reset()
};
