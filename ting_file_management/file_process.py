from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    queue_size = instance.size()
    queue_range = range(queue_size)

    for index in queue_range:
        file_processed = instance.search(index)
        if file_processed["nome_do_arquivo"] == path_file:
            return None

    file_lines = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }

    instance.enqueue(result)
    return print(result)


def remove(instance):
    removed_file = instance.dequeue()
    if removed_file:
        file_name = removed_file["nome_do_arquivo"]
        print(f'Arquivo {file_name} removido com sucesso')
    else:
        print('Não há elementos')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
