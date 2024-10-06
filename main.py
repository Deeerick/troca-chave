import os
from tqdm import tqdm


# Função para substituir códigos antigos por um novo código em um arquivo específico
def replace_code_in_file(file_path, old_codes, new_code):
    try:
        # Tenta abrir o arquivo para leitura usando a codificação 'latin-1'
        with open(file_path, 'r', encoding='latin-1') as file:
            file_data = file.read()
    except Exception as e:
        # Se ocorrer um erro ao ler o arquivo, imprime uma mensagem de erro
        print(f"Error reading file {file_path}: {e}")
        return

    original_data = file_data

    # Itera sobre a lista de códigos antigos e substitui cada um pelo novo código
    for old_code in old_codes:
        if old_code in file_data:
            print(f"Found '{old_code}' in {file_path}")
        file_data = file_data.replace(old_code, new_code)

    # Se o conteúdo do arquivo foi alterado, tenta escrever as alterações de volta no arquivo
    if file_data != original_data:
        try:
            with open(file_path, 'w', encoding='latin-1') as file:
                file.write(file_data)
            print(f"Replaced code in {file_path}")
        except Exception as e:
            # Se ocorrer um erro ao escrever no arquivo, imprime uma mensagem de erro
            print(f"Error writing file {file_path}: {e}")
    else:
        # Se não houve alterações no conteúdo do arquivo, imprime uma mensagem
        print(f"No changes made to {file_path}")


# Função para substituir códigos antigos por um novo código em todos os arquivos .txt de um diretório
def replace_code_in_directory(directory, old_codes, new_code):
    # Conta o número total de arquivos .txt no diretório
    total_files = sum(
        [len(files) for r, d, files in os.walk(directory)
         if any(f.endswith('.txt') for f in files)]
    )

    # Usa a barra de progresso tqdm para mostrar o progresso da operação
    with tqdm(total=total_files, desc="Processing files", unit="file") as pbar:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    replace_code_in_file(file_path, old_codes, new_code)
                    pbar.update(1)


# Caminho do diretório onde os arquivos estão localizados
directory_path = 'C:\\arquivos\\'
# Lista de códigos antigos a serem substituídos
old_codes = ['abc', 'ABC']
# Novo código que substituirá os antigos
new_code = 'FFF'

# Chama a função para substituir os códigos no diretório especificado
replace_code_in_directory(directory_path, old_codes, new_code)