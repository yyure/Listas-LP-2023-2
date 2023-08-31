from statistics import mean
from typing import Optional

def add_person(data: list[dict], name: str, age: int,
               city: str, hobbies: list[str]) -> list[dict]:
    """Adiciona uma pessoa em um conjunto de dados

    :param data: Conjunto de dados
    :type data: list[dict]
    :param name: Nome da pessoa
    :type name: str
    :param age: Idade da pessoa
    :type age: int
    :param city: Cidade da pessoa
    :type city: str
    :param hobbies: Hobbies da pessoa
    :type hobbies: list[str]
    :raises ValueError: Se 'age' não está entre 0 e 100
    :raises ValueError: Se 'hobbies' é uma lista vazia
    :return: Conjunto de dados com a pessoa adicionada
    :rtype: list[dict]
    """

    for person in data:
        if person['name'] == name:
            print("Essa pessoa já está no conjunto de dados")
            return data
    
    try:
        if age < 0 or age > 100:
            raise ValueError
    except ValueError:
        print("A idade deve ser um inteiro entre 0 e 100")
        return data
    
    try:
        if len(hobbies) == 0:
            raise ValueError
    except ValueError:
        print("A lista de hobbies não pode ser vazia")
        return data
    
    try:
        if type(city) != str:
            raise TypeError
    except TypeError:
        print("O tipo do valor passado para o argumento 'city' não é uma string.")
        return data
    
    person = {'name': name, 'age': age, 'hobbies': hobbies}
    data.append(person)
    return data


def remove_person(data: list[dict], name: str) -> list[dict]:
    """Remove uma pessoa de um conjunto de dados

    :param data: Conjunto de dados
    :type data: list[dict]
    :param name: Nome da pessoa
    :type name: str
    :return: Conjunto de dados com a pessoa removida
    :rtype: list[dict]
    """

    for person in data:
        if person['name'] == name:
            data.remove(person)
            return data
        
    print("Não existe nenhuma pessoa listada com esse nome")
    return data


def get_ages(data: list[dict]) -> tuple[int, int, int]:
    """Retorna uma tupla contendo, em ordem, a idade da pessoa mais nova,
    a média de idade das pessoas e a idade da pessoa mais velha.

    :param data: Conjunto de dados
    :type data: list[dict]
    :return: Tupla contendo as idades 
    :rtype: tuple[int, int, int]
    """

    #Cria uma lista contendo as idades de todas as pessoas
    ages: list[int] = list()
    for person in data:
        ages.append(person['age'])
    
    min_age = min(ages)
    mean_age = round(mean(ages))
    max_age = max(ages)

    return (min_age, mean_age, max_age)


def get_hobbies(data: list[dict]) -> set[str]:
    """Retorna um conjunto com todos os hobbies das pessoas em um conjunto de dados

    :param data: Conjunto de dados
    :type data: list[dict]
    :return: Conjunto com todos os hobbies em 'data'
    :rtype: set[str]
    """

    #Cria um conjunto e adiciona os hobbies de todas as pessoas
    set_hobbies = set()
    for person in data:
        for hobbie in person['hobbies']:
            set_hobbies.add(hobbie)
    
    return set_hobbies


def get_people_by_hobbies(data: list[dict], hobbies: set[str]) -> list[str]:
    """Recebe um conjunto de dados e um conjunto de strings (representando hobbies)
    e retorna uma lista contendo os nomes das pessoas que possuem pelo menos um
    desses hobbies, ordenados por idade (do mais novo para o mais velho).

    :param data: Conjunto de dados
    :type data: list[dict]
    :param hobbies: Conjunto de hobbies
    :type hobbies: set[str]
    :return: Lista com os nomes das pessoas
    :rtype: list[str]
    """

    names = list()

    #Ordena as pessoas no conjunto de dados, do mais novo para o mais velho
    sorted_data = sorted(data, key=lambda d: d['age'])

    set_hobbies = set(hobbies)

    #Adiciona o nome de uma pessoa na lista caso ela possua pelo menos
    #um dos hobbies no conjunto 'hobbies'
    for person in sorted_data:
        if len(set_hobbies.intersection(person['hobbies'])) > 0:
            names.append(person['name'])
    
    return names


def match_people(data: list[dict], name: Optional[str] = None,
                 min_age: Optional[int] = None, max_age: Optional[int] = None, 
                 city: Optional[int] = None, hobbies: Optional[list[str]] = []) -> list[str]:
    """Recebe um conjunto de dados e pode receber alguns parâmetros opcionais:
    um nome, uma idade mínima, uma idade máxima, uma cidade ou um conjunto de hobbies.
    A função retorna uma lista contendo os nomes das pessoas que atendem simultaneamente 
    a todos os critérios passados, ordenados por idade (do mais novo para o mais velho).

    :param data: Conjunto de dados
    :type data: list[dict]
    :param name: Nome da pessoa, defaults to None
    :type name: Optional[str], optional
    :param min_age: Idade mínima, defaults to None
    :type min_age: Optional[int], optional
    :param max_age: Idade máxima, defaults to None
    :type max_age: Optional[int], optional
    :param city: Nome da cidade, defaults to None
    :type city: Optional[int], optional
    :param hobbies: Lista de hobbies, defaults to []
    :type hobbies: Optional[list[str]], optional
    :raises ValueError: Caso 'min_age' seja maior do que 'max_age'
    :return: Lista com os nomes das pessoas
    :rtype: list[str]
    """

    names: list[str] = list()

    try:
        if (min_age is not None) and (max_age is not None) and (min_age > max_age) :
            raise ValueError
    except ValueError:
        print("'min_age' deve ser menor ou igual a 'max_age'")
        return names

    #Ordena as pessoas no conjunto de dados, do mais novo para o mais velho
    sorted_data = sorted(data, key=lambda d: d['age'])

    if hobbies is not None:
        set_hobbies = set(hobbies)

    #Verifica para cada pessoa se as condições são satisfeitas
    for person in sorted_data:
        if name is not None:
            if person['name'] != name:
                continue

        if min_age is not None:
            if person['age'] < min_age:
                continue
        
        if max_age is not None:
            if person['age'] > max_age:
                continue
        
        if city is not None:
            if person['city'] != city:
                continue
        
        if hobbies is not None:
            if set_hobbies.issuperset(person['hobbies']) == False:
                continue
        
        names.append(person['name'])
    
    return names