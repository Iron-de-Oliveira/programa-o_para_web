function deletarAluno(id) {
    if (confirm("Tem certeza que deseja deletar este aluno?")) {
        fetch(`/aluno/${id}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            window.location.reload(); // Recarrega a página para atualizar a lista
        })
        .catch(error => {
            console.error('Erro ao deletar aluno:', error);
            alert('Erro ao deletar aluno.');
        });
    }
}

function abrirFormularioEdicao(id, nome, email, senha) {
    document.getElementById('form-editar').style.display = 'block';
    document.getElementById('edit-id').value = id;
    document.getElementById('edit-nome').value = nome;
    document.getElementById('edit-email').value = email;
    document.getElementById('edit-senha').value = senha;
}

function cancelarEdicao() {
    document.getElementById('form-editar').style.display = 'none';
}

function salvarEdicao() {
    const id = document.getElementById('edit-id').value;
    const nome = document.getElementById('edit-nome').value;
    const email = document.getElementById('edit-email').value;
    const senha = document.getElementById('edit-senha').value;

    fetch(`/aluno/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome, email, senha }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.reload(); // Atualiza a página para mostrar mudanças
    })
    .catch(error => {
        console.error('Erro ao atualizar aluno:', error);
        alert('Erro ao atualizar aluno.');
    });
}

function home(){
    window.location.href =("cadastro.html")
}