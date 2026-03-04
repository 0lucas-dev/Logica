class Usuario {
    constructor(nome, email, senha){
        this.nome = nome;
        this.email = email;
        this.senha = senha;
    }
}

class Sistema{
    constructor(){
        this.usuarios = [];
    }

    addUsuario(user){
        this.usuarios.push(user)
    }

    listarUsuarios(){
        console.log(this.usuarios)
    }

    deletarUsuario(){

    }

    editarUsuario(){
          
    }
}

usuario1 = new Usuario("joao", "joao@email.com", 1234)
usuario2 = new Usuario("maria", "maria@email.com", 1234)
sistema = new Sistema()
sistema.addUsuario(usuario1)
sistema.addUsuario(usuario2)
sistema.listarUsuarios()