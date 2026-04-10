import os

# Funções para calcular os valores de cada tipo de contrato
def calcular_salario_estagiario(valor_fixo):
    # Estagiário não tem descontos, recebe o valor cheio
    return valor_fixo, 0.0, 0.0, valor_fixo

def calcular_salario_clt(bruto):
    # Aplica 8% de INSS e 10% de IRRF se passar de 2000
    inss = bruto * 0.08
    irrf = bruto * 0.10 if bruto > 2000 else 0.0
    liquido = bruto - (inss + irrf)
    return bruto, inss, irrf, liquido

def calcular_salario_freelancer(horas, valor_hora):
    # Calcula o bruto e tira o desconto fixo de 5%
    bruto = horas * valor_hora
    desconto = bruto * 0.05
    liquido = bruto - desconto
    return bruto, desconto, 0.0, liquido

# Função para ler os dados e validar as entradas
def cadastrar_funcionario():
    while True:
        try:
            nome = input("Nome do funcionário: ").strip()
            if not nome:
                print("O nome é obrigatório!")
                continue

            tipo = input("Tipo (Estagiário, CLT ou Freelancer): ").strip().lower()
            if tipo not in ['estagiario', 'clt', 'freelancer']:
                print("Tipo inválido! Tente novamente.")
                continue

            if tipo == 'freelancer':
                h = float(input("Quantidade de horas: "))
                v = float(input("Valor por hora: "))
                if h <= 0 or v <= 0: raise ValueError
                return {"nome": nome, "tipo": tipo, "horas": h, "valor_h": v}
            else:
                sal = float(input("Valor do salário: "))
                if sal <= 0: raise ValueError
                return {"nome": nome, "tipo": tipo, "salario": sal}

        except ValueError:
            print("Erro: Por favor, digite números válidos e maiores que zero.")

# Organiza os cálculos em um dicionário para o relatório
def processar_pagamento(dados):
    tipo = dados['tipo']
    if tipo == 'estagiario':
        bruto, inss, irrf, liq = calcular_salario_estagiario(dados['salario'])
    elif tipo == 'clt':
        bruto, inss, irrf, liq = calcular_salario_clt(dados['salario'])
    else:
        bruto, inss, irrf, liq = calcular_salario_freelancer(dados['horas'], dados['valor_h'])
    
    return {
        "nome": dados['nome'],
        "tipo": tipo.capitalize(),
        "bruto": bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": liq
    }

# Monta o texto do relatório formatado
def gerar_relatorio(lista_funcionarios):
    texto = "=== Relatório de Folha de Pagamento ===\n"
    total_geral = 0
    for f in lista_funcionarios:
        texto += f"Nome: {f['nome']}\n"
        texto += f"Tipo: {f['tipo']}\n"
        texto += f"Salário Bruto: R$ {f['bruto']:.2f}\n"
        texto += f"Desconto INSS: R$ {f['inss']:.2f}\n"
        texto += f"Desconto IRRF: R$ {f['irrf']:.2f}\n"
        texto += f"Salário Líquido: R$ {f['liquido']:.2f}\n"
        texto += "-" * 30 + "\n"
        total_geral += f['liquido']
    
    texto += f"Total pago pela empresa: R$ {total_geral:.2f}"
    return texto

# Salva o resultado final em um arquivo txt
def salvar_em_arquivo(conteudo):
    try:
        with open("relatorio_folha.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print("Relatório salvo no arquivo 'relatorio_folha.txt'!")
    except Exception as e:
        print(f"Erro ao tentar salvar o arquivo: {e}")

# Função principal que controla o menu
def main():
    funcionarios = []
    while True:
        print("\n1-Cadastrar | 2-Relatório | 3-Salvar TXT | 4-Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dados = cadastrar_funcionario()
            resultado = processar_pagamento(dados)
            funcionarios.append(resultado)
            print("Funcionário cadastrado!")
        elif opcao == '2':
            if funcionarios:
                print("\n" + gerar_relatorio(funcionarios))
            else:
                print("Nenhum funcionário na lista.")
        elif opcao == '3':
            if funcionarios:
                salvar_em_arquivo(gerar_relatorio(funcionarios))
            else:
                print("Não há dados para salvar.")
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
