from abc import ABCMeta, abstractmethod
import requests


class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass


class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass


class API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)

        try:
            request = requests.get(URL)
            response = request.json()
            data = (
                response.get("id"),
                response.get("name"),
                response.get("species")
            )
            return data

        except Exception as error:
            print(f"Ocorreu um erro na requisição: {error}")


class API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)

        try:
            request = requests.get(URL)
            response = request.json()

            # Descomentar as linhas abaixo caso queira retornar os nomes dos filmes ao invés dos links.
            # films = response.get("films")
            # filmsNamesList = []

            # for film in films:
            #     filmRequest = requests.get(film).json()
            #     filmsNamesList.append(filmRequest.get("title"))

            SW_data = (
                response.get("name"),
                response.get("films"),
                # filmsNamesList
            )
            return SW_data

        except Exception as error:
            print(f"Ocorreu um erro na requisição: {error}")


class API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)

        try:
            request = requests.get(URL)
            response = request.json()

            IaF_data = (
                response.get("name"),
                response.get("tvSeries")
            )
            return IaF_data

        except Exception as error:
            print(f"Ocorreu um erro na requisição: {error}")
