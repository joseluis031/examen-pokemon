class pokemon:
    lista_ids= []
    def __init__(self,id,nombre,arma,salud,ataque,defensa):
       if isinstance(id, int):
            if id not in pokemon.lista_ids:
                self.id = id
                pokemon.lista_ids.append(self.id)
            else:
                raise ValueError("The parameter pokemon_id should be a new id not taken by other Pokemon.")
       else:
            raise TypeError("The parameter id should be a int.")

       if isinstance(nombre, str):
            self.nombre = nombre
       else:
            raise TypeError("The parameter pokemon_name should be a String.")

       if isinstance(arma, WeaponType):
            self.arma = arma
       else:
            raise TypeError("The parameter weapon_type should be a WeaponType.")

       if isinstance(salud, int):
            if 1 <= salud <= 100:
                self.salud = salud
            else:
                raise ValueError("The parameter health_points should be > 0 and <= 100.")
       else:
            raise TypeError("The parameter health_points should be a int.")

       if isinstance(ataque, int):
            if 1 <= ataque <= 10:
                self.ataque = ataque
            else:
                raise ValueError("The parameter attack_rating should be > 0 and <= 10.")
       else:
            raise TypeError("The parameter attack_rating should be a int.")

       if isinstance(defensa, int):
            if 1 <= defensa <= 10:
                self.defensa = defensa
            else:
                raise ValueError("The parameter defense_rating should be > 0 and <= 10.")
       else:
            raise TypeError("The parameter defense_rating should be a int.") 