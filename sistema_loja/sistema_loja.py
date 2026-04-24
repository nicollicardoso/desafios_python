import os

def cadastrar_produto(produtos):
    print("\n--- Cadastro de Produto ---")
    try:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Erro: O nome não pode ser vazio.")
            return produtos
        
        # Verifica se o produto já existe
        if any(p['nome'].lower() == nome.lower() for p in produtos):
            print("Erro: Este produto já está cadastrado.")
            return produtos

        preco = float(input("Preço: R$ "))
        if preco <= 0:
            print("Erro: O preço deve ser maior que zero.")
            return produtos

        estoque = int(input("Estoque inicial: "))
        if estoque < 0:
            print("Erro: O estoque não pode ser negativo.")
            return produtos

        produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
        print(f"Produto '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("Erro: Entrada inválida. Preço e estoque devem ser numéricos.")
    
    return produtos

def listar_produtos(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return False
    
    print("\n--- Produtos Disponíveis ---")
    for i, p in enumerate(produtos):
        print(f"{i + 1}. {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['estoque']})")
    return True

def realizar_venda(produtos, vendas):
    if not listar_produtos(produtos):
        return

    try:
        cliente = input("\nNome do cliente: ").strip()
        if not cliente:
            print("Erro: Nome do cliente é obrigatório.")
            return

        indice = int(input("Selecione o número do produto: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Erro: Produto inexistente.")
            return

        produto = produtos[indice]
        quantidade = int(input(f"Quantidade de '{produto['nome']}' (Disponível: {produto['estoque']}): "))

        if quantidade <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return
        
        if quantidade > produto['estoque']:
            print(f"Erro: Estoque insuficiente. Temos apenas {produto['estoque']} unidades.")
            return

        # Cálculos
        valor_bruto = produto['preco'] * quantidade
        desconto = 0.0
        if quantidade > 10:
            desconto = valor_bruto * 0.05
        
        valor_final = valor_bruto - desconto

        # Atualiza estoque e registra venda
        produto['estoque'] -= quantidade
        venda = {
            "cliente": cliente,
            "produto": produto['nome'],
            "quantidade": quantidade,
            "valor_bruto": valor_bruto,
            "desconto": desconto,
            "valor_final": valor_final
        }
        vendas.append(venda)
        print("\nVenda realizada com sucesso!")
        
    except ValueError:
        print("Erro: Entrada inválida. Digite números para seleção e quantidade.")

def formatar_relatorio(vendas):
    if not vendas:
        return "Nenhuma venda realizada até o momento."

    relatorio = "=== Relatório de Vendas ===\n"
    total_geral = 0
    
    for v in vendas:
        relatorio += f"\nCliente: {v['cliente']}\n"
        relatorio += f"Produto: {v['produto']}\n"
        relatorio += f"Quantidade: {v['quantidade']}\n"
        relatorio += f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n"
        relatorio += f"Desconto: R$ {v['desconto']:.2f}\n"
        relatorio += f"Valor Final: R$ {v['valor_final']:.2f}\n"
        relatorio += "-" * 25 + "\n"
        total_geral += v['valor_final']
    
    relatorio += f"\nTotal arrecadado pela loja: R$ {total_geral:.2f}\n"
    return relatorio

def salvar_relatorio(vendas):
    if not vendas:
        print("Não há vendas para salvar.")
        return

    caminho = input("Digite o caminho completo ou nome do arquivo (ex: relatorio.txt): ")
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(formatar_relatorio(vendas))
        print(f"Relatório salvo com sucesso em: {os.path.abspath(caminho)}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def main():
    produtos = []
    vendas = [] # Usada como lista/pilha

    while True:
        print("\n--- MENU LOJA ---")
        print("1. Cadastrar Produto")
        print("2. Realizar Venda")
        print("3. Gerar Relatório")
        print("4. Salvar Relatório em Arquivo")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            produtos = cadastrar_produto(produtos)
        elif opcao == '2':
            realizar_venda(produtos, vendas)
        elif opcao == '3':
            print("\n" + formatar_relatorio(vendas))
        elif opcao == '4':
            salvar_relatorio(vendas)
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()