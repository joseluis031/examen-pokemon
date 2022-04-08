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
        
        
    def __del__(self):
        

        
        pokemon.lista_ids.remove(self.id)


    def __str__(self):
        
        human_readable_string = ("Pokemon ID " + str(self.id) +
                                 " with name " + self.nombre +
                                 " has as weapon " + self.arma.name +
                                 " and health " + str(self.salud))

        return human_readable_string


    def get_id(self):
        
        return self.id


    def get_nombre(self):
        
        return self.nombre


    def get_arma(self):
        
        return self.arma


    def get_salud(self):
        
        return self.salud


    def get_ataque(self):
        
        return self.ataque


    def get_defensa(self):
        

        return self.defensa


    def set_nombre(self, pokemon_name_to_be_set):
        
        if isinstance(pokemon_name_to_be_set, str):
            self.nombre = pokemon_name_to_be_set
        else:
            raise TypeError("The parameter pokemon_name_to_be_set should be a String.")


    def set_arma(self, weapon_type_to_be_set):
        
        if isinstance(weapon_type_to_be_set, WeaponType):
            self.arma = weapon_type_to_be_set
        else:
            raise TypeError("The parameter weapon_type should be a WeaponType.")


    def set_ataque(self, ataque_to_be_set):
      
        if isinstance(ataque_to_be_set, int):
            if 1 <= ataque_to_be_set <= 10:
                self.ataque = ataque_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")


    def set_defensa(self, defensa_to_be_set):
        
        if isinstance(defensa_to_be_set, int):
            if 1 <= defensa_to_be_set <= 10:
                self._defensa = defensa_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")


    def is_alive(self):
        
        return not bool(self.salud == 0)



    def fight_attack(self, pokemon_to_attack):
        
        points_of_damage = self.ataque

        print("The Pokemon " + self.nombre +
              " hits the Pokemon " + pokemon_to_attack.get_nombre() +
              " with " + str(points_of_damage) + " points of damage!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit


    def fight_defense(self, points_of_damage):
        
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The Pokemon " + self.nombre +
              " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        if points_of_damage > self.defensa:
            self.salud = (self.salud -
                                   (points_of_damage - self.defensa))
            pokemon_was_hit = True
        else:
            print("No damage received.")
            pokemon_was_hit = False

        # Normalizing the defeat of the Pokemon.
        if self.salud < 1:
            self.salud = 0

        return pokemon_was_hit


def main():
    
    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_nombre() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().nombre == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_salud() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defensa() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_salud() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



if __name__ == "__main__":
    main()