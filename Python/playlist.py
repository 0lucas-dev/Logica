class Musica:
    def __init__(self, nome_artista, nome_musica, duracao, genero):
        self.nome_artista = nome_artista
        self.nome_musica = nome_musica
        self.duracao = duracao
        self.genero = genero

    # Uso isso so para dizer como o objeto vai ser exibido quando chamado se não ia mostrar o endereço dele, daria para fazer usando getters mas no python não e muito comum usar isso
    def __str__(self):
        return f"{self.nome_artista} - {self.nome_musica} ({self.duracao} min) [{self.genero}]"

class Playlist:
    def __init__(self, nome_playlist):
        self.nome_playlist = nome_playlist
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, nome_musica):
        for musica in self.musicas:
            if musica.nome_musica.lower() == nome_musica.lower():
                self.musicas.remove(musica)
                print(f"Música '{nome_musica}' removida da playlist.")
                return
        print(f"Música '{nome_musica}' não encontrada.")

    def listar_musicas(self):
        if not self.musicas:
            print("A playlist está vazia.")
            return
        
        print(f"Playlist: {self.nome_playlist}")
        for musica in self.musicas:
            print(musica)

    def total_duracao(self):
        soma = 0
        for musica in self.musicas:
            soma += musica.duracao
        return f"Total de {soma} minutos."

    def duracao_genero(self, genero):
        soma_genero = 0
        for musica in self.musicas:
            if genero.lower() == musica.genero.lower():
                soma_genero += musica.duracao
        return f"A duração total de {genero} é de {soma_genero} minutos."

musica1 = Musica("Matuee", "Tue", 3, "Trap")
musica2 = Musica("Teto", "Os cara tao no Teto", 2, "Pop")

playlist1 = Playlist("Minha_Play")

playlist1.adicionar_musica(musica1)
playlist1.adicionar_musica(musica2)

playlist1.listar_musicas()

print(playlist1.total_duracao())
print(playlist1.duracao_genero("pop"))

playlist1.remover_musica("Tue")

playlist1.listar_musicas()