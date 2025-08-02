from abc import ABC, abstractmethod
import uuid
from datetime import date

# -------------------------------------------------
# 1) Interface                                    🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        return f'{self._nome} logado!'

# -------------------------------------------------
# 2) Mixins                                       🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self):
        self.__id= uuid.uuid4() # TODO: gerar e armazenar um ID usando uuid.uuid4()
    def get_id(self):
        return self.__id # TODO: retornar o ID

class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        # TODO: imprimir no formato  [LOG] <evento>
        print(f'[LOG]: {evento}')

# -------------------------------------------------
# 3) Classe base Pessoa                           🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome= nome
        self._cpf= cpf
        # TODO: armazenar nome e cpf como atributos protegidos
    @property
    def nome(self):
        return self._nome
        # TODO: retornar o nome
    def __str__(self):
        return(f'{self._nome} ({self._cpf})')
        # TODO: "Maria (123.456.789-00)"

# -------------------------------------------------
# 4) Ingresso — classe simples                    🡇
# -------------------------------------------------
class Ingresso:
    def __init__(self, codigo: str, tipo: str, preco: float):
        self.codigo = codigo
        self.tipo = tipo  # ex.: 'Pista', 'VIP', 'Backstage'
        self.preco = preco
    def __str__(self):
        return f"[{self.codigo}] {self.tipo} – R$ {self.preco:.2f}"

# -------------------------------------------------
# 5) Cliente                                      🡇
# -------------------------------------------------
class Cliente(Pessoa):
    """Herda de Pessoa e possui ingressos."""
    def __init__(self, nome: str, cpf: str, email: str):
        super().__init__(nome,cpf)
        self._email=email
        self._ingressos=[]
        # TODO: chamar super().__init__ e criar lista vazia de ingressos

    def comprar_ingresso(self, ingresso: Ingresso):
        self._ingressos.append(ingresso)
        # TODO: adicionar ingresso à lista
    def listar_ingressos(self):
        print(self._ingressos)
        return
        # TODO: imprimir os ingressos


class Funcionario (AuditavelMixin,IdentificavelMixin,Pessoa,Logavel):
    def __init__(self, cargo, registro):
        self._cargo = cargo
        self._registro= registro
    def exibir_dados(self):
        return (f'nome:{self._nome}; cargo:{self._cargo}; registro:{self._registro}; ID:{self.get_id()}')
    def logar_entrada(self):
        return self.logar_entrada()


    '''SOCORRO'''
        

# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)      🡇
# -------------------------------------------------
# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, registro
# - Métodos:
#   • exibir_dados()    → imprime nome, cargo, registro e ID
#   • logar_entrada()   → registra no log

# -------------------------------------------------
# 7) Palco (objeto de composição)                 🡇
# -------------------------------------------------
class Palco:
    """Objeto que compõe o Festival."""
    def __init__(self, nome: str, capacidade: int):
        self.nome= nome
        self.capacidade= capacidade
        # TODO: armazenar nome e capacidade

    def resumo(self):
        return (self.nome,'-', self.capacidade)
        # TODO: retornar string "Palco X – cap. Y pessoas"


class Festival:
    def __init__(self,nome,data:date,local,palco: Palco):
        self.nome=nome
        self.data=data
        self.local=local
        self.palco=palco
        self.clientes=[]
        self.ingressos=[]
        self.equipe=[]

    def vender_ingresso(self,cliente: Cliente, ingresso: Ingresso):
        if (self.palco.capacidade - len(self.ingressos)) <=0:
            raise ValueError ("Ingressos esgotados!")
        else:
            self.ingressos.append(ingresso)
            
            #SOCORROOOOOOOOOOOOOOOOO

            self.clientes.append(cliente)
            return "Ingresso comprado!"
        
    def adicionar_funcionario(self,func:Funcionario):
        if func not in self.equipe:
            self.equipe.append(func)
            return 'funcionário cadastrado!'
        else: 
            return 'funcionário já cadastrado.'
        
    def listar_clientes(self):
        return self.clientes
    def listar_equipe(self):
        return self.equipe
    def listar_ingressos(self):
        return self.ingressos

        


    

# -------------------------------------------------
# 8) Festival (composição com Palco)              🡇
# -------------------------------------------------
# TODO: Implementar a classe Festival
# - Atributos: nome, data, local, palco
# - Listas: clientes, equipe, ingressos
# - Métodos:
#   • vender_ingresso(cliente, ingresso)  (checar duplicidade & capacidade)
#   • adicionar_funcionario(func)
#   • listar_clientes()
#   • listar_equipe()
#   • listar_ingressos()

# -------------------------------------------------
# 9) EmpresaEventos                               🡇
# -------------------------------------------------
class EmpresaEventos:
    """Agrupa seus festivais (has-a)."""
    def __init__(self, nome: str):
        # TODO: validar nome (≥ 3 letras) e criar lista vazia de festivais
        pass
    @property
    def nome(self):
        # TODO: retornar nome
        pass
    @nome.setter
    def nome(self, novo_nome: str):
        # TODO: validar + atualizar nome
        pass
    def adicionar_festival(self, festival):
        # TODO: adicionar festival à lista
        pass
    def buscar_festival(self, nome: str):
        # TODO: retornar festival ou None
        pass
    def listar_festivais(self):
        # TODO: imprimir todos os festivais
        pass

# -------------------------------------------------
# 10) Auditor (Identificável + Logável)           🡇
# -------------------------------------------------
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_festival(fest) → verifica:
#         ▸ Nº de clientes ≤ capacidade do palco
#         ▸ existe ao menos 1 funcionário
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"

# -------------------------------------------------
# 11) Bloco de teste                              🡇
# -------------------------------------------------
if __name__ == "__main__":
    """
    TODO:
      • Crie 1 empresa, 2 festivais, clientes, equipe e auditor.
      • Venda ingressos, liste participantes, audite festivais.
      • Mostre saídas no console para validar implementações.
    """
    pass
