from classes1.Livro.entities.livroDigital import LivroDigital
from classes1.Livro.entities.livroFisico import LivroFisico
from classes1.Livro.entities.biblioteca import Biblioteca



domcas = LivroDigital("Dom Casmurro", "Machado de Assis", 300, 1890)


Biblioteca.addLivro(domcas)
print(Biblioteca.catalogo)

