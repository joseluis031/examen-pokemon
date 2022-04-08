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



