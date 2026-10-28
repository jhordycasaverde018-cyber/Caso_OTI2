class Matricula:
    def __init__(self, semestre: str, codigo: str, monto_base=60):
        self.__semestre_academico = semestre
        self.__codigo_estudiante = codigo
        self.__monto_base = monto_base

    def calcular_costo(self):
        return self.__monto_base


class MatriculaBecados(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() / 2


class MatriculaExtemporanea(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() + 15


class MatriculaJalados(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() + 15


class MatriculaDoble(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() + 15 + 15


estudiante_becado = MatriculaBecados("2026-II", "27250106")
estudiante_extemporaneo = MatriculaExtemporanea("2026-II", "27250110")
estudiante_jalado = MatriculaJalados("2026-II", "27250116")

print(f"Costo Becado: S/ {estudiante_becado.calcular_costo():.2f}")
print(f"Costo Extemporáneo: S/ {estudiante_extemporaneo.calcular_costo():.2f}")
print(f"Costo Jalado: S/ {estudiante_jalado.calcular_costo():.2f}")
