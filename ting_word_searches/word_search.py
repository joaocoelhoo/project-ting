def find_ocurrencies(file_lines, word):
    result = []
    for index, line in enumerate(file_lines):
        if word.lower() in line.lower():
            result.append({"linha": index + 1})

    return result


def find_ocurrencies_and_content(file_lines, word):
    result = []
    for index, line in enumerate(file_lines):
        if word.lower() in line.lower():
            result.append({
                "linha": index + 1,
                "conteudo": line
            })

    return result


def find_word(word, instance, with_content):
    queue_size = instance.size()
    queue_range = range(queue_size)
    result = []

    for index in queue_range:
        file_processed = instance.search(index)
        search_result = {
            "palavra": word,
            "arquivo": file_processed["nome_do_arquivo"],
            "ocorrencias": []
        }

        file_lines = file_processed["linhas_do_arquivo"]
        if with_content:
            ocurrencies = find_ocurrencies_and_content(file_lines, word)
        else:
            ocurrencies = find_ocurrencies(file_lines, word)
        search_result["ocorrencias"].extend(ocurrencies)

        if search_result["ocorrencias"]:
            result.append(search_result)

    return result


def exists_word(word, instance):
    return find_word(word, instance, False)


def search_by_word(word, instance):
    return find_word(word, instance, True)
