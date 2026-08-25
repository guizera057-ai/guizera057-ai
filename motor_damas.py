import sys
import json

def executar_motor():
    # O sistema interceptará a instrução da jogada via argumento do terminal
    if len(sys.argv) > 1:
        jogada = sys.argv[1]
        print(f"[Operação] Instrução de jogada recebida com precisão: {jogada}")
    else:
        print("[Operação] Nenhuma instrução externa detectada no momento.")
        
    # A validação matemática e a atualização do estado_tabuleiro.json
    # serão incorporadas nesta arquitetura na próxima iteração.

if __name__ == "__main__":
    executar_motor()
