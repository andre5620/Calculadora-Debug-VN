#!/usr/bin/env python3
"""
Decodificador de Status de Alarmes Hex
Decompõe um valor hexadecimal em estados individuais de bits de alarme
"""

def decodificar_status_alarme(valor_hex):
    """
    Decodifica valor hex em estados individuais de alarme
    
    Args:
        valor_hex: Representação string do valor hex (ex: '0008', '0x0008')
    """
    # Define nomes dos alarmes para cada posição de bit
    nomes_alarmes = [
        "statusCtrlSecao",           # bit 0
        "secByte1",                   # bit 1
        "existeMasterIsobus",         # bit 2
        "masterIsobus",               # bit 3
        "existeSensoresAgrosystem",  # bit 4
        "statusAgrosystemRow",        # bit 5
        "existePopulacao",            # bit 6
        "populacaoTravando"           # bit 7
    ]
    
    # Limpa entrada hex e converte para inteiro
    hex_limpo = valor_hex.replace('0x', '').replace('0X', '').strip()
    
    try:
        # Converte hex para inteiro
        valor = int(hex_limpo, 16)
        
        # Pega apenas os 8 bits inferiores (uint8_t)
        valor = valor & 0xFF
        
        print(f"\nEntrada Hex: 0x{hex_limpo.upper()}")
        print(f"Valor Decimal: {valor}")
        print(f"Binário: {format(valor, '08b')}")
        print("\n" + "="*50)
        print("DETALHAMENTO DO STATUS DOS ALARMES:")
        print("="*50)
        
        # Verifica cada bit
        alarmes_ativos = []
        for pos_bit in range(8):
            # Verifica se o bit está setado (1) ou limpo (0)
            estado_bit = (valor >> pos_bit) & 1
            status = "ATIVO" if estado_bit else "inativo"
            
            # Formata saída com indicação visual
            if estado_bit:
                print(f"Bit {pos_bit}: [{status:^8}] - {nomes_alarmes[pos_bit]}")
                alarmes_ativos.append(nomes_alarmes[pos_bit])
            else:
                print(f"Bit {pos_bit}: [{status:^8}] - {nomes_alarmes[pos_bit]}")
        
        print("\n" + "="*50)
        if alarmes_ativos:
            print("ALARMES ATIVOS:")
            for alarme in alarmes_ativos:
                print(f"  ✓ {alarme}")
        else:
            print("Nenhum alarme ativo")
        print("="*50)
        
    except ValueError:
        print(f"Erro: Valor hexadecimal inválido '{valor_hex}'")
        return

def principal():
    """Função principal para executar o decodificador"""
    print("Decodificador de Status de Alarmes Hex")
    print("=======================================\n")
    
    # Exemplo com o valor fornecido
    print("Exemplo com o valor fornecido:")
    decodificar_status_alarme("0008")
    
    print("\n" + "-"*50)
    print("\nVocê pode testar com outros valores hexadecimais:")
    print("-"*50)
    
    # Modo interativo
    while True:
        print("\nDigite o valor hex (ou 's' para sair): ", end="")
        entrada_usuario = input().strip()
        
        if entrada_usuario.lower() == 's':
            print("Saindo...")
            break
            
        if entrada_usuario:
            decodificar_status_alarme(entrada_usuario)

if __name__ == "__main__":
    principal()