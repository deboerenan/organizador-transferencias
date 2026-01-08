#!/usr/bin/env python3
"""
ORGANIZADOR DE ARQUIVOS - Python
Organiza arquivos por tipo/extensão
"""

import os
import shutil
import time
from pathlib import Path

def mostrar_banner():
    print("\n" + "═"*60)
    print("📁 ORGANIZADOR DE ARQUIVOS AUTOMÁTICO")
    print("═"*60)

def criar_pastas(diretorio, categorias):
    """Cria as pastas de organização se não existirem"""
    for categoria in categorias.keys():
        pasta = os.path.join(diretorio, categoria)
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"  ✅ Criada pasta: {categoria}")

def organizar_arquivos():
    mostrar_banner()
    
    # Diretório padrão (Downloads do usuário)
    downloads_path = os.path.join(Path.home(), "Downloads")
    diretorio_atual = os.getcwd()
    
    print(f"\n📂 Diretório atual: {diretorio_atual}")
    print(f"📂 Pasta Downloads: {downloads_path}")
    
    print("\n📍 ONDE DESEJA ORGANIZAR OS ARQUIVOS?")
    print("  1. Diretório atual")
    print("  2. Pasta Downloads")
    print("  3. Outro diretório")
    
    try:
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            diretorio = diretorio_atual
        elif opcao == "2":
            diretorio = downloads_path
        elif opcao == "3":
            outro_dir = input("Digite o caminho completo: ").strip()
            if os.path.exists(outro_dir):
                diretorio = outro_dir
            else:
                print("❌ Diretório não existe! Usando diretório atual.")
                diretorio = diretorio_atual
        else:
            print("⚠️  Opção inválida! Usando diretório atual.")
            diretorio = diretorio_atual
            
    except KeyboardInterrupt:
        print("\n\n❌ Operação cancelada")
        return
    
    print(f"\n🎯 Organizando: {diretorio}")
    
    # Definição das categorias
    categorias = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'],
        'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.odt', '.rtf'],
        'Vídeos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v'],
        'Músicas': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
        'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        'Programação': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.php', '.json', '.xml'],
        'Executáveis': ['.exe', '.msi', '.sh', '.deb', '.rpm', '.apk', '.bat'],
        'Torrents': ['.torrent'],
        'ISOs_e_Imagens': ['.iso', '.img', '.dmg', '.vmdk'],
        'Fontes': ['.ttf', '.otf', '.woff', '.woff2']
    }
    
    # Contadores
    total_arquivos = 0
    arquivos_movidos = 0
    ignorados = []
    
    try:
        print("\n📊 Analisando arquivos...")
        time.sleep(1)
        
        # Lista todos os arquivos no diretório
        itens = os.listdir(diretorio)
        arquivos = [f for f in itens if os.path.isfile(os.path.join(diretorio, f))]
        
        if not arquivos:
            print("\n📭 Nenhum arquivo encontrado para organizar!")
            return
        
        total_arquivos = len(arquivos)
        print(f"\n📄 Encontrados {total_arquivos} arquivos")
        
        # Cria as pastas
        criar_pastas(diretorio, categorias)
        
        # Pasta para "Outros"
        outros_path = os.path.join(diretorio, "Outros")
        if not os.path.exists(outros_path):
            os.makedirs(outros_path)
        
        print("\n🔄 Movendo arquivos...")
        time.sleep(0.5)
        
        # Processa cada arquivo
        for arquivo in arquivos:
            origem = os.path.join(diretorio, arquivo)
            extensao = os.path.splitext(arquivo)[1].lower()
            
            # Ignora arquivos do sistema e o próprio script
            if arquivo in ['.DS_Store', 'desktop.ini', 'organizador_simples.py']:
                ignorados.append(arquivo)
                continue
            
            movido = False
            
            # Tenta encontrar categoria
            for categoria, extensoes in categorias.items():
                if extensao in extensoes:
                    destino = os.path.join(diretorio, categoria, arquivo)
                    
                    # Verifica se já existe arquivo com mesmo nome
                    contador = 1
                    nome_base, ext = os.path.splitext(arquivo)
                    while os.path.exists(destino):
                        novo_nome = f"{nome_base}_{contador}{ext}"
                        destino = os.path.join(diretorio, categoria, novo_nome)
                        contador += 1
                    
                    try:
                        shutil.move(origem, destino)
                        arquivos_movidos += 1
                        movido = True
                        break
                    except Exception as e:
                        print(f"  ❌ Erro ao mover {arquivo}: {e}")
            
            # Se não encontrou categoria, vai para "Outros"
            if not movido:
                destino = os.path.join(diretorio, "Outros", arquivo)
                try:
                    shutil.move(origem, destino)
                    arquivos_movidos += 1
                except Exception as e:
                    print(f"  ❌ Erro ao mover {arquivo} para Outros: {e}")
        
        # Mostra relatório
        print("\n" + "═"*60)
        print("📊 RELATÓRIO DA ORGANIZAÇÃO")
        print("═"*60)
        print(f"\n📂 Diretório: {diretorio}")
        print(f"📄 Total de arquivos encontrados: {total_arquivos}")
        print(f"✅ Arquivos organizados: {arquivos_movidos}")
        
        if ignorados:
            print(f"⚠️  Arquivos ignorados: {len(ignorados)}")
            for ig in ignorados:
                print(f"    - {ig}")
        
        print("\n📁 ESTRUTURA CRIADA:")
        print("─"*40)
        
        # Lista todas as pastas criadas
        for item in sorted(os.listdir(diretorio)):
            item_path = os.path.join(diretorio, item)
            if os.path.isdir(item_path):
                num_arquivos = len([f for f in os.listdir(item_path) 
                                  if os.path.isfile(os.path.join(item_path, f))])
                if num_arquivos > 0:
                    print(f"  📁 {item}: {num_arquivos} arquivo(s)")
        
        print("\n✅ Organização concluída com sucesso!")
        
    except Exception as e:
        print(f"\n❌ Erro durante a organização: {e}")
        print("   Verifique as permissões do diretório.")

def main():
    try:
        organizar_arquivos()
        input("\n🎯 Pressione Enter para sair...")
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n💥 Erro fatal: {e}")

if __name__ == "__main__":
    main()
