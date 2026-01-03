# Sistema de Controle de Estoque - Loja de Eletrônicos
# Lista para armazenar os produtos
estoque = []
# Função para adicionar produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    # Verifica se o produto já existe
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Produto já existe no estoque.")
            return
    try:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
    except ValueError:
        print("Erro: preço ou quantidade inválidos!")
        return
    # Adiciona o produto à lista
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")
# Função para atualizar produto
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar:").strip()
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            try:
                produto['preco'] = float(input("Digite o novo preço do produto: "))
                produto['quantidade'] = int(input("Digite a nova quantidade em estoque: "))
            except ValueError:
                print("Erro: preço ou quantidade inválidos!")
                return
            print(f"Produto '{nome}' atualizado com sucesso!")
            return
    print("Produto não encontrado no estoque.")
# Função para excluir produto
def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ").strip()
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            estoque.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print("Produto não encontrado no estoque.")
# Função para visualizar estoque
def visualizar_estoque():
    if not estoque:
        print("O estoque está vazio.")
        return
    print("\n--- Estoque Atual ---")
    for produto in estoque:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    print("---------------------\n")
# Função principal com menu
def menu():
    while True:
        print("=== Sistema de Controle de Estoque ===")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Excluir produto")
        print("4. Visualizar estoque")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            atualizar_produto()
        elif escolha == "3":
            excluir_produto()
        elif escolha == "4":
            visualizar_estoque()
        elif escolha == "5":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
# Executa o sistema
if __name__ == "__main__":
    menu()