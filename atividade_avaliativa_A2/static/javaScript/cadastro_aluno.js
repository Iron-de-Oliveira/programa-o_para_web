console.log("js carregado")

function coletar_dados(){
    const data_nome = document.getElementById("nome").value;
    const data_email = document.getElementById("email").value;
    const data_senha = document.getElementById("senha").value;

    const dados_aluno = {
        nome: data_nome,
        email: data_email,
        senha: data_senha,
    };

    fetch('http://localhost:5000/Alunos', {

        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados_aluno)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Erro ao cadastrar aluno");
    });

}

