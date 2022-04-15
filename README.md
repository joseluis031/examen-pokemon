# examen-pokemon
El link del repositorio es el siguiente:[GitHub](https://github.com/joseluis031/examen-pokemon.git)

1.[Main](#id1)

2.[Pokemon](#id2)

3.[Pokemon agua](#id3)

4.[Pokemon aire](#id4)

5.[Pokemon electrico](#id5)

6.[Pokemon tierra](#id6)

7.[Weapon type](#id7)


## Main <a name="id1"></a>
```
import csv
import copy

from weapon_type import WeaponType
from pokemon import Pokemon


def get_data_from_user(name_file):
    
    set_of_pokemons = []

    if not isinstance(name_file, str):
        raise TypeError("The paramenter name_file is not a String.")

    name_file_s = name_file

    try:
        with open(name_file_s, newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)

        for temp_pokemon_csv in data_from_file:
            coach_pokemon = Pokemon(int(temp_pokemon_csv[0]),
                                    temp_pokemon_csv[1],
                                    WeaponType.from_str(temp_pokemon_csv[2]),
                                    int(temp_pokemon_csv[3]),
                                    int(temp_pokemon_csv[4]),
                                    int(temp_pokemon_csv[5]))

            set_of_pokemons.append(coach_pokemon)

    except SyntaxError:
        print("Oops! The Pokemons of the coach were not introduced correctly." +
                " Try again...")

    return set_of_pokemons


def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    
    if isinstance(list_of_pokemons,list):

        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("All pokemons should be Pokemon Type")
        print("Please Coach " + str(coach_to_ask) + " introduce the ID of the Pokemon: " + "\n")

        while True:
            print("List of Pokemons: " + "\n")
            
            for i in list_of_pokemons:
                print(i)
            
            string_introduced = input(":~>")
            try:
                int_introduced= int(string_introduced)
            except ValueError:
                print("Please, introduce an ID present in the list:")
            for temp_pokemon in list_of_pokemons:
                if int_introduced == temp_pokemon.get_id():
                    return temp_pokemon
            print("Please, introduce a number present in the list: ")
    else:
        raise TypeError("list_pokemons should be a list")


def coach_is_undefeated(list_of_pokemons):
    

    if isinstance(list_of_pokemons, list):
        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("All pokemons should be pokemon Type")

    defeated = True

    for temp_pokemon in list_of_pokemons:
        if temp_pokemon.is_alive():
            defeated = False

    return not defeated


def main():
    

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    print("For Game User 1: \n")
    game_user_1 = get_data_from_user("coach_1_pokemons.csv")

    # Get configuration for Game User 2.
    print("For Game User 2: \n")
    game_user_2 = get_data_from_user("coach_2_pokemons.csv")

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    temp_list_pokemons_from_coach_1 = game_user_1
    list_pokemons_alive_coach_1 = copy.copy(temp_list_pokemons_from_coach_1)

    temp_list_pokemons_from_coach_2 = game_user_2
    list_pokemons_alive_coach_2 = copy.copy(temp_list_pokemons_from_coach_2)

    # Choose first pokemons
    print("Coach 1 choose your first pokemon")
    temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Please coach 1 introduce the id of the pokemon:", list_pokemons_alive_coach_1)
    print("Coach 2 choose your first pokemon")
    temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Please coach 2 introduce the id of the pokemon:",list_pokemons_alive_coach_2)

    while(coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):

        if not temp_pokemon_coach_1.is_alive():
            # Select a new pokemon
            print("Coach 1 your pokemon: " + str(temp_pokemon_coach_1) + " has been defeated. Please select the new pokemon to fight ")
            list_pokemons_alive_coach_1.remove(temp_pokemon_coach_1)
            temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Please coach 1 introduce the id of the pokemon", list_pokemons_alive_coach_1)
        if not temp_pokemon_coach_2.is_alive():
            # Select a new pokemon
            print("Coach 2 your pokemon: " + str(temp_pokemon_coach_2) + " has been defeated. Please select the new pokemon to fight ")
            list_pokemons_alive_coach_2.remove(temp_pokemon_coach_2)
            temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Please coach 2 introduce the id of the pokemon", list_pokemons_alive_coach_2)

        print("pokemon from Game User 1 attacks.")
        temp_pokemon_coach_1.fight_attack(temp_pokemon_coach_2)
        print("pokemon from Game User 2 attacks.")
        temp_pokemon_coach_2.fight_attack(temp_pokemon_coach_1)


    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")
    if (coach_is_undefeated(temp_list_pokemons_from_coach_1)and not coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("The WINNER is Game User 1.")
    elif (not coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("The WINNER is Game User 2.")
    else:
        print("Both Game Users have been defeated. There is a DRAW.")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    for temp_pokemon in temp_list_pokemons_from_coach_1:
        print(temp_pokemon)

    print("Game User 2:")
    for temp_pokemon in temp_list_pokemons_from_coach_2:
        print(temp_pokemon)


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()

```

## Pokemon <a name="id2"></a>
```
from weapon_type import WeaponType

class Pokemon():
    lista_ids= []
    def __init__(self,id,nombre,arma,salud,ataque,defensa):
       if isinstance(id, int):
            if id not in Pokemon.lista_ids:
                self.id = id
                Pokemon.lista_ids.append(self.id)
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
        

        
        Pokemon.lista_ids.remove(self.id)


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
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

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
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

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
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_salud() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

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
```

## Pokemon agua <a name="id3"></a>
```
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonWater(Pokemon):
    


    def __init__(self,id,nombre,arma,salud,ataque,defensa):
        

        super().__init__(id,nombre,arma,salud,ataque,
                         10, defensa)

        if isinstance(ataque, int):
            if 11 <= ataque <= 20:
                self._ataque = ataque
            else:
                raise ValueError("The parameter attack_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating should be a int.")


    def set_ataque(self, ataque_to_be_set):
        
        if isinstance(ataque_to_be_set, int):
            if 11 <= ataque_to_be_set <= 20:
                self._ataque = ataque_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")


def main():
    

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonWater(1, "Squirtle", WeaponType.HEADBUTT, 100, 12, 8)

    if pokemon_1.get_nombre() == "Squirtle":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_salud() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_ataque() == 12:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defensa() == 8:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", WeaponType.HEADBUTT, 100,15, 7)

    if str(pokemon_2) == "Pokemon ID 7 with name Squirtle has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", WeaponType.KICK, 97, 15, 8)

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
    pokemon_4 = PokemonWater(4, "Squirtle", WeaponType.ELBOW, 93, 11, 9)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 32:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", WeaponType.PUNCH, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", WeaponType.PUNCH, 99, 18, 9)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 88:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```

## Pokemon aire <a name="id4"></a>
```

import random

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonAir(Pokemon):
    


    def __init__(self,id,nombre,arma,salud,ataque,defensa):
        

        super().__init__(self,id,nombre,arma,salud,ataque,defensa)


    def fight_defense(self, points_of_damage):
        
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The Pokemon " + self._nombre +
              " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        failure_probability = random.randrange(0, 2)

        if failure_probability == 0:  # Normal defense applied.
            if points_of_damage > self._defensa:
                self._salud = (self._salud -
                                       (points_of_damage - self._defensa))
                pokemon_was_hit = True
            else:
                print("No damage received.")
                pokemon_was_hit = False
        else:
            print("No damage received.")
            pokemon_was_hit = False

        if self._salud < 1:
            self._salud = 0

        return pokemon_was_hit


def main():
    

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonAir(1, "Pidgey", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_nombre() == "Pidgey":
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

    if pokemon_1.get_defensa() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonAir(7, "Pidgey", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pidgey has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonAir(3, "Pidgey", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
            
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonAir(4, "Pidgey", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_salud() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonAir(5, "Pidgey", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonAir(6, "Pidgey", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 95:
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


```

## Pokemon electrico <a name="id5"></a>
```
import random

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonElectricity(Pokemon):
    


    def __init__(self,id,nombre,arma,salud,ataque,defensa):
        

        super().__init__(id,nombre,arma,salud,ataque,defensa)


    def fight_attack(self, pokemon_to_attack):
        

        points_of_damage = self._ataque

        print("The Pokemon " + self._nombre +
              " hits the Pokemon " + pokemon_to_attack.get_nombre() +
              " with " + str(points_of_damage) + " points of damage!")

        hit_probability = random.randrange(0, 2)

        if hit_probability == 0:  # Normal attack applied.
            points_of_damage = self._ataque
        else:  # Special attack applied.
            points_of_damage = 2 * self._ataque

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit


def main():
    

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonElectricity(1, "Pikachu", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_nombre() == "Pikachu":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "HEADBUTT":
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

    if pokemon_1.get_defensa() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonElectricity(7, "Pikachu", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pikachu has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonElectricity(3, "Pikachu", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonElectricity(4, "Pikachu", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_salud() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_salud() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonElectricity(5, "Pikachu", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonElectricity(6, "Pikachu", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if (pokemon_6.get_salud() == 95) or (pokemon_6.get_salud() == 85):
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
```

## Pokemon tierra <a name="id6"></a>
```
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonEarth(Pokemon):
    


    def __init__(self,id,nombre,arma,salud,ataque,defensa):
        

        super().__init__(id,nombre,arma,salud,ataque,defensa, 10)

        if isinstance(defensa, int):
            if 11 <= defensa <= 20:
                self._defensa = defensa
            else:
                raise ValueError("The parameter defense_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")


    def set_defensa(self, defensa_to_be_set):
        
        if isinstance(defensa_to_be_set, int):
            if 11 <= defensa_to_be_set <= 20:
                self._defensa = defensa_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")


def main():
    

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", WeaponType.HEADBUTT, 100, 8, 15)

    if pokemon_1.get_nombre() == "Diglett":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "HEADBUTT":
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

    if pokemon_1.get_defensa() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", WeaponType.HEADBUTT, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", WeaponType.KICK, 97, 8, 15)

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
    pokemon_4 = PokemonEarth(4, "Diglett", WeaponType.ELBOW, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_salud() == 34:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", WeaponType.PUNCH, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", WeaponType.PUNCH, 99, 9, 18)

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



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```

## Weapon type <a name="id7"></a>
```
from enum import Enum


class WeaponType(Enum):
    
    PUNCH = 2
    KICK = 4
    ELBOW = 6
    HEADBUTT = 10

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(str_arma):
        
        str_arma = str_arma.lower()
        if str_arma == 'punch':
            return WeaponType.PUNCH
        elif str_arma == 'kick':
            return WeaponType.KICK
        elif str_arma == 'elbow':
            return WeaponType.ELBOW
        elif str_arma == 'headbutt':
            return WeaponType.HEADBUTT
        else:
            raise TypeError("The str " + str_arma + " does not correspond with a warrior Type")


def main():
    

    print("=================================================================.")
    print("Test Case 1: Check Class WeaponType - Name.")
    print("=================================================================.")

    if isinstance(WeaponType.PUNCH, WeaponType):
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.KICK, WeaponType):
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.ELBOW, WeaponType):
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.HEADBUTT, WeaponType):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class WeaponType - Value.")
    print("=================================================================.")

    if WeaponType.PUNCH.value == 2:
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.KICK.value == 4:
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.ELBOW.value == 6:
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.HEADBUTT.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


if __name__ == "__main__":
    main()



```
