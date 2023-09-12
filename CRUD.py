class Crud:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
    

    def leer(self):
        
        sql = ('SELECT * FROM aulas WHERE borrado = 1')
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado



    def crear(self, nuevo):

        sql = f"INSERT INTO aulas(idAula, descripcion, capacidad, idEdificio, equipoAudiovisual, usuario, borrado) VALUES ('{nuevo[0]}', '{nuevo[1]}', '{nuevo[2]}', '{nuevo[3]}', '{nuevo[4]}', '{nuevo[5]}', 1)"
        self.cursor.execute(sql)
        self.conexion.commit()


    def eliminar(self, aula):
        sql = f"UPDATE `aulas` SET `borrado`= 0 WHERE `idAula` = '{aula}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def ver_actualizar(self, aula):
        
        sql = f"SELECT * FROM aulas WHERE `idAula` = '{aula}'"
        self.cursor.execute(sql)
        actualizar_aulas = self.cursor.fetchall()
        self.conexion.commit()

        return actualizar_aulas
    
    def actualizar_datos(self,datos):
        
        sql = "UPDATE aulas SET descripcion = %s, capacidad = %s, idEdificio = %s, equipoAudiovisual = %s, usuario = %s WHERE idAula = %s"
        self.cursor.execute(sql, (datos[1], datos[2], datos[3], datos[4], datos[5], datos[0]))
        self.conexion.commit()
        print("Actualización de base exitosa")