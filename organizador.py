#!/usr/bin/env python3
"""
ORGANIZADOR DE TRANSFERÊNCIAS - VERSÃO 3.0
Menu interativo com design
Autor: Renan
"""

import os
import shutil
import sys

# ========= CONFIGURAÇÃO =========
PASTA_BASE = os.path.join(os.path.expanduser('~'), 'Transferências')

# ========= CORES PARA O TERMINAL =========
class Cores:
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    BRANCO = '\033[97m'

# ========= CATEGORIAS COMPLETAS =========
CATEGORIAS = {
    # Imagens
    '.jpg': '🖼️  Imagens', '.jpeg': '🖼️  Imagens', '.png': '🖼️  Imagens',
    '.gif': '🖼️  Imagens', '.bmp': '🖼️  Imagens', '.svg': '🖼️  Imagens',
    '.webp': '🖼️  Imagens',
    
    # Documentos
    '.pdf': '📄 Documentos', '.doc': '📄 Documentos', '.docx': '📄 Documentos',
    '.txt': '📄 Documentos', '.rtf': '📄 Documentos', '.odt': '📄 Documentos',
    '.md': '📄 Documentos',
    
    # Planilhas
    '.xls': '📊 Planilhas', '.xlsx': '📊 Planilhas', '.csv': '📊 Planilhas',
    
    # Compactados
    '.zip': '🗜️  Compactados', '.rar': '🗜️  Compactados', '.7z': '🗜️  Compactados',
    '.tar': '🗜️  Compactados', '.gz': '🗜️  Compactados',
    
    # Mídia
    '.mp3': '🎵 Músicas', '.wav': '🎵 Músicas', '.flac': '🎵 Músicas',
    '.mp4': '🎬 Vídeos', '.avi': '🎬 Vídeos', '.mkv': '🎬 Vídeos',
    '.mov': '🎬 Vídeos', '.wmv': '🎬 Vídeos',
    
    # Códigos
    '.py': '🐍 Python', '.js': '📜 JavaScript', '.java': '☕ Java',
    '.html': '🌐 HTML', '.css': '🎨 CSS', '.php': '🐘 PHP',
    '.c': '🔧 C', '.cpp': '⚙️  C++',
    
    # Executáveis
    '.exe': '⚙️  Executáveis', '.deb': '📦 Pacotes DEB', '.sh': '🐚 Scripts Shell',
    '.appimage': '📦 AppImage', '.msi': '⚙️  Instaladores',
    
    # Outros conhecidos
    '.torrent': '🧲 Torrents', '.iso': '💿 ISOs', '.dmg': '🍎 Mac DMG',
    '.ppt': '📊 Apresentações', '.pptx': '📊 Apresentações',
}

# ========= FUNÇÕES AUXILIARES =========
def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def cabecalho():
    """Exibe o cabeçalho do programa"""
    print(Cores.CIANO + "=" * 70 + Cores.RESET)
    print(Cores.NEGRITO + Cores.VERDE + "📁  ORGANIZADOR DE TRANSFERÊNCIAS - v3.0" + Cores.RESET)
    print(Cores.NEGRITO + Cores.AZUL + "📍  Pasta: " + PASTA_BASE + Cores.RESET)
    print(Cores.CIANO + "=" * 70 + Cores.RESET)

def menu_principal():
    """Exibe o menu principal"""
    print(f"\n{Cores.NEGRITO}{Cores.MAGENTA}📋  MENU PRINCIPAL{Cores.RESET}")
    print(Cores.AMARELO + "─" * 40 + Cores.RESET)
    
    opcoes = [
        f"{Cores.VERDE}1{Cores.RESET} 🔄  Organizar arquivos",
        f"{Cores.VERDE}2{Cores.RESET} 📊  Ver estatísticas",
        f"{Cores.VERDE}3{Cores.RESET} 📋  Ver categorias",
        f"{Cores.VERDE}4{Cores.RESET} ➕  Adicionar categoria",
        f"{Cores.VERDE}5{Cores.RESET} 🗂️   Ver estrutura atual",
        f"{Cores.VERDE}6{Cores.RESET} 🆘  Ajuda / Atalhos",
        f"{Cores.VERDE}0{Cores.RESET} 🚪  Sair"
    ]
    
    for opcao in opcoes:
        print(f"  {opcao}")
    
    print(Cores.AMARELO + "─" * 40 + Cores.RESET)
    
    escolha = input(f"\n{Cores.NEGRITO}👉  Escolha uma opção (0-6): {Cores.RESET}").strip()
    return escolha

def pausar():
    """Pausa a execução até Enter"""
    input(f"\n{Cores.AMARELO}👆  Pressione Enter para continuar...{Cores.RESET}")

# ========= FUNÇÕES PRINCIPAIS =========
def organizar_arquivos():
    """Organiza todos os arquivos"""
    limpar_tela()
    cabecalho()
    
    print(f"\n{Cores.NEGRITO}{Cores.VERDE}🔄  ORGANIZANDO ARQUIVOS{Cores.RESET}")
    print(Cores.AMARELO + "─" * 50 + Cores.RESET)
    
    if not os.path.exists(PASTA_BASE):
        print(f"{Cores.VERMELHO}❌  Pasta não encontrada!{Cores.RESET}")
        pausar()
        return
    
    # Listar arquivos
    arquivos = []
    for item in os.listdir(PASTA_BASE):
        caminho = os.path.join(PASTA_BASE, item)
        if os.path.isfile(caminho) and not item.startswith('.'):
            arquivos.append(item)
    
    if not arquivos:
        print(f"{Cores.AZUL}📭  Nenhum arquivo para organizar!{Cores.RESET}")
        pausar()
        return
    
    print(f"{Cores.CIANO}📊  Encontrados {len(arquivos)} arquivo(s){Cores.RESET}")
    
    # Mostrar preview
    if len(arquivos) <= 8:
        print(f"\n{Cores.BRANCO}📄  Arquivos encontrados:{Cores.RESET}")
        for i, arq in enumerate(arquivos, 1):
            print(f"  {Cores.VERDE}{i:2d}.{Cores.RESET} {arq}")
    else:
        print(f"\n{Cores.BRANCO}📄  Mostrando 8 de {len(arquivos)} arquivos:{Cores.RESET}")
        for i, arq in enumerate(arquivos[:8], 1):
            print(f"  {Cores.VERDE}{i:2d}.{Cores.RESET} {arq}")
        print(f"  {Cores.AMARELO}... e mais {len(arquivos) - 8} arquivos{Cores.RESET}")
    
    # Confirmar
    print(f"\n{Cores.VERMELHO}⚠️   ATENÇÃO: Arquivos serão MOVIDOS para pastas!{Cores.RESET}")
    resposta = input(f"{Cores.NEGRITO}❓  Deseja continuar? (s/n): {Cores.RESET}").strip().lower()
    
    if resposta != 's':
        print(f"{Cores.AMARELO}👌  Operação cancelada!{Cores.RESET}")
        pausar()
        return
    
    # Organizar
    print(f"\n{Cores.VERDE}🔄  Organizando...{Cores.RESET}")
    print(Cores.AMARELO + "─" * 50 + Cores.RESET)
    
    organizados = 0
    erros = 0
    
    for arquivo in arquivos:
        caminho_origem = os.path.join(PASTA_BASE, arquivo)
        nome_base, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        # Determinar categoria
        if extensao in CATEGORIAS:
            pasta_destino_nome = CATEGORIAS[extensao]
        else:
            pasta_destino_nome = "📦 Outros"
        
        pasta_destino = os.path.join(PASTA_BASE, pasta_destino_nome.split()[-1])
        
        # Criar pasta se não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
            print(f"{Cores.AZUL}📁  Criada: {pasta_destino_nome}{Cores.RESET}")
        
        # Mover arquivo
        try:
            destino_final = os.path.join(pasta_destino, arquivo)
            contador = 1
            
            while os.path.exists(destino_final):
                novo_nome = f"{nome_base}_{contador}{extensao}"
                destino_final = os.path.join(pasta_destino, novo_nome)
                contador += 1
            
            shutil.move(caminho_origem, destino_final)
            print(f"  {Cores.VERDE}✓{Cores.RESET} {arquivo[:40]:40} → {pasta_destino_nome}")
            organizados += 1
        except Exception as e:
            print(f"  {Cores.VERMELHO}✗{Cores.RESET} {arquivo[:40]:40} → ERRO: {str(e)[:30]}")
            erros += 1
    
    # Relatório
    print(f"\n{Cores.CIANO}=" * 60 + Cores.RESET)
    print(f"{Cores.NEGRITO}{Cores.VERDE}📊  RELATÓRIO FINAL{Cores.RESET}")
    print(f"{Cores.CIANO}=" * 60 + Cores.RESET)
    print(f"  {Cores.VERDE}✅  Organizados: {organizados}{Cores.RESET}")
    print(f"  {Cores.VERMELHO}❌  Erros: {erros}{Cores.RESET}")
    
    pausar()

def ver_estatisticas():
    """Mostra estatísticas da pasta"""
    limpar_tela()
    cabecalho()
    
    print(f"\n{Cores.NEGRITO}{Cores.AZUL}📊  ESTATÍSTICAS{Cores.RESET}")
    print(Cores.AMARELO + "─" * 50 + Cores.RESET)
    
    if not os.path.exists(PASTA_BASE):
        print(f"{Cores.VERMELHO}❌  Pasta não encontrada!{Cores.RESET}")
        pausar()
        return
    
    # Contar arquivos e pastas
    arquivos = []
    pastas = []
    
    for item in os.listdir(PASTA_BASE):
        caminho = os.path.join(PASTA_BASE, item)
        if os.path.isfile(caminho):
            arquivos.append(item)
        elif os.path.isdir(caminho):
            pastas.append(item)
    
    # Calcular tamanho total
    tamanho_total = 0
    for arquivo in arquivos:
        try:
            tamanho_total += os.path.getsize(os.path.join(PASTA_BASE, arquivo))
        except:
            pass
    
    # Exibir estatísticas
    print(f"{Cores.CIANO}📁  Pastas: {len(pastas)}{Cores.RESET}")
    print(f"{Cores.CIANO}📄  Arquivos: {len(arquivos)}{Cores.RESET}")
    print(f"{Cores.CIANO}💾  Tamanho total: {tamanho_total:,} bytes ({tamanho_total/1024/1024:.2f} MB){Cores.RESET}")
    
    # Top 5 maiores arquivos
    if arquivos:
        print(f"\n{Cores.VERDE}🏆  TOP 5 maiores arquivos:{Cores.RESET}")
        arquivos_com_tamanho = []
        for arq in arquivos:
            try:
                tamanho = os.path.getsize(os.path.join(PASTA_BASE, arq))
                arquivos_com_tamanho.append((arq, tamanho))
            except:
                pass
        
        arquivos_com_tamanho.sort(key=lambda x: x[1], reverse=True)
        
        for i, (arq, tamanho) in enumerate(arquivos_com_tamanho[:5], 1):
            print(f"  {Cores.AMARELO}{i}.{Cores.RESET} {arq[:40]:40} {tamanho/1024:8.1f} KB")
    
    pausar()

def ver_categorias():
    """Mostra todas as categorias disponíveis"""
    limpar_tela()
    cabecalho()
    
    print(f"\n{Cores.NEGRITO}{Cores.MAGENTA}📋  CATEGORIAS DISPONÍVEIS{Cores.RESET}")
    print(Cores.AMARELO + "─" * 60 + Cores.RESET)
    
    # Agrupar por categoria
    grupos = {}
    for ext, cat in CATEGORIAS.items():
        if cat not in grupos:
            grupos[cat] = []
        grupos[cat].append(ext)
    
    for categoria in sorted(grupos.keys()):
        extensoes = grupos[categoria]
        print(f"\n{Cores.NEGRITO}{categoria}:{Cores.RESET}")
        
        # Mostrar em colunas
        colunas = 6
        for i in range(0, len(extensoes), colunas):
            linha = extensoes[i:i+colunas]
            print("  " + " ".join([f"{Cores.VERDE}{ext}{Cores.RESET}" for ext in linha]))
    
    print(f"\n{Cores.CIANO}📊  Total: {len(CATEGORIAS)} extensões em {len(grupos)} categorias{Cores.RESET}")
    pausar()

def ver_estrutura():
    """Mostra a estrutura atual da pasta"""
    limpar_tela()
    cabecalho()
    
    print(f"\n{Cores.NEGRITO}{Cores.AZUL}🗂️   ESTRUTURA ATUAL{Cores.RESET}")
    print(Cores.AMARELO + "─" * 60 + Cores.RESET)
    
    if not os.path.exists(PASTA_BASE):
        print(f"{Cores.VERMELHO}❌  Pasta não encontrada!{Cores.RESET}")
        pausar()
        return
    
    def mostrar_arvore(pasta, prefixo="", is_last=True):
        """Função recursiva para mostrar árvore"""
        itens = sorted(os.listdir(pasta))
        
        for i, item in enumerate(itens):
            caminho = os.path.join(pasta, item)
            is_last_item = (i == len(itens) - 1)
            
            # Definir símbolos
            if is_last_item:
                simbolo = "└── "
                novo_prefixo = prefixo + "    "
            else:
                simbolo = "├── "
                novo_prefixo = prefixo + "│   "
            
            # Cor baseada no tipo
            if os.path.isdir(caminho):
                cor = Cores.CIANO
                simbolo_item = "📁 "
            else:
                cor = Cores.VERDE
                simbolo_item = "📄 "
            
            # Mostrar item
            print(f"{prefixo}{simbolo}{cor}{simbolo_item}{item}{Cores.RESET}")
            
            # Se for pasta, mostrar conteúdo (apenas 1 nível)
            if os.path.isdir(caminho) and pasta == PASTA_BASE:
                mostrar_arvore(caminho, novo_prefixo, is_last_item)
    
    mostrar_arvore(PASTA_BASE)
    pausar()

def mostrar_ajuda():
    """Mostra ajuda e atalhos"""
    limpar_tela()
    cabecalho()
    
    print(f"\n{Cores.NEGRITO}{Cores.AMARELO}🆘  AJUDA E ATALHOS{Cores.RESET}")
    print(Cores.AMARELO + "─" * 60 + Cores.RESET)
    
    ajuda = [
        (f"{Cores.VERDE}F1{Cores.RESET}", "Menu principal"),
        (f"{Cores.VERDE}Ctrl+C{Cores.RESET}", "Sair do programa"),
        (f"{Cores.VERDE}Enter{Cores.RESET}", "Confirmar/Continuar"),
        (f"{Cores.VERDE}s/n{Cores.RESET}", "Sim/Não em confirmações"),
    ]
    
    print(f"\n{Cores.CIANO}📋  ATALHOS DO TECLADO:{Cores.RESET}")
    for atalho, descricao in ajuda:
        print(f"  {atalho:15} → {descricao}")
    
    print(f"\n{Cores.CIANO}🎯  FUNCIONALIDADES:{Cores.RESET}")
    funcionalidades = [
        "📁 Organização automática por tipo de arquivo",
        "📊 Estatísticas detalhadas da pasta",
        "📋 Visualização de categorias disponíveis",
        "🗂️  Exibição em árvore da estrutura",
        "🎨 Interface colorida e intuitiva",
    ]
    
    for func in funcionalidades:
        print(f"  • {func}")
    
    print(f"\n{Cores.CIANO}💡  DICAS:{Cores.RESET}")
    print(f"  • Arquivos com extensões desconhecidas vão para '📦 Outros'")
    print(f"  • Pastas existentes não são modificadas")
    print(f"  • Arquivos duplicados são renomeados automaticamente")
    
    pausar()

# ========= PROGRAMA PRINCIPAL =========
def main():
    """Função principal"""
    limpar_tela()
    
    while True:
        try:
            limpar_tela()
            cabecalho()
            
            escolha = menu_principal()
            
            if escolha == "1":
                organizar_arquivos()
            elif escolha == "2":
                ver_estatisticas()
            elif escolha == "3":
                ver_categorias()
            elif escolha == "4":
                print(f"\n{Cores.AMARELO}🚧  Em desenvolvimento...{Cores.RESET}")
                pausar()
            elif escolha == "5":
                ver_estrutura()
            elif escolha == "6":
                mostrar_ajuda()
            elif escolha == "0":
                limpar_tela()
                print(f"\n{Cores.CIANO}=" * 60 + Cores.RESET)
                print(f"{Cores.NEGRITO}{Cores.VERDE}👋  OBRIGADO POR USAR O ORGANIZADOR!{Cores.RESET}")
                print(f"{Cores.CIANO}=" * 60 + Cores.RESET)
                print(f"\n{Cores.AMARELO}💾  Mantenha seus arquivos organizados!{Cores.RESET}\n")
                break
            else:
                print(f"\n{Cores.VERMELHO}❌  Opção inválida! Tente novamente.{Cores.RESET}")
                pausar()
                
        except KeyboardInterrupt:
            print(f"\n\n{Cores.VERMELHO}⚠️   Programa interrompido. Até logo!{Cores.RESET}")
            break
        except Exception as e:
            print(f"\n{Cores.VERMELHO}💥  ERRO: {e}{Cores.RESET}")
            pausar()

if __name__ == "__main__":
    main()

