import random # Biblioteca para gerar números aleatórios, utilizada nos ataques.

# Criando as classes 
# Personagem: classe mãe (superclasse)
# Heroi: classe filha que será controlada pelo usuário
# Inimigo: classe filha que representa o adversário do jogador

class Personagem:
    """
    Classe base para personagens, contendo atributos como nome, vida e nível,
    além de métodos comuns como ataque e receber dano.
    """
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    # Métodos getter para acessar os atributos privados.

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        """
        Exibe os detalhes do personagem (nome, vida, nível).
        :return: String formatada com os detalhes.
        """

        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        """
        Realiza um ataque normal no alvo, causando dano aleatório baseado no nível do atacante.
        :param alvo: Instância do personagem alvo do ataque.
        """
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

class Heroi(Personagem):
    """
    Classe representando o herói, controlado pelo jogador.
    Inclui a habilidade especial exclusiva.
    """

    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        """
        Exibe detalhes do herói, incluindo a habilidade especial.
        :return: String formatada com os detalhes do herói.
        """
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        """
        Realiza o ataque especial no alvo, causando dano extra baseado no nível do herói.
        :param alvo: Instância do personagem alvo do ataque especial.
        """
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano.")

class Inimigo(Personagem):
    """
    Classe representando o inimigo, adversário do jogador.
    Inclui um tipo específico de inimigo.
    """
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        """
        Exibe detalhes do inimigo, incluindo o tipo de inimigo.
        :return: String formatada com os detalhes do inimigo.
        """
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

class Jogo:
    """ 
    Classe orquestradora do jogo. Gerencia o herói e o inimigo, além de controlar os turnos de batalha.
    """
    def __init__(self):
        self.heroi = Heroi(nome="Heroi", vida=100, nivel=2, habilidade="Super força")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=2, tipo="Velocidade")
    
    def iniciar_batalha(self):
        """
        Inicia e gerencia a batalha entre o herói e o inimigo em turnos. O jogo continua até que
        um dos personagens tenha sua vida reduzida a 0.
        """
        print("Iniciando a batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")
            
            # Se o inimigo ainda estiver vivo, ele contra-ataca.
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
        
        # Verifica o resultado da batalha.
        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")

# Criar a instância do jogo e iniciar batalha.
jogo = Jogo()
jogo.iniciar_batalha()

