from stringprep import c22_specials

from cursonline.entities.curso import Curso
from cursonline.entities.plataforma import Plataforma
from entities.instrutor import Instrutor

inst1 = Instrutor("Lucas", 400)
inst2 = Instrutor("Maria", 30)

c1 = Curso("Como vender drogas online rapido", 50, inst1)
c2 = Curso("Violao", 9999, inst1)
c3 = Curso("Direito Fundiário", 100, inst2)
c4 = Curso("MS Office", 999999, inst2)

plat1 = Plataforma("Alura")

plat1.addCurso(c1)
plat1.addCurso(c2)
plat1.addCurso(c3)
plat1.addCurso(c4)


plat1.listCursos()