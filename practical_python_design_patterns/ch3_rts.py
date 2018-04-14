from ch3_unitbase import UnitBase
from copy import deepcopy

class Unit(UnitBase):
    def __init__(self, p_unit_type, p_level):
        self.unit_type = p_unit_type.capitalize()

        try:
            with open('ch3_parms/' + self.unit_type.lower() + '_' + str(p_level)) as v_parm_file:
                v_lines = v_parm_file.read().split('\n')
                self.life = v_lines[0]
                self.speed = v_lines[1]
                self.attack_power = v_lines[2]
                self.attack_range = v_lines[3]
                self.weapon = v_lines[4]
        except Exception as v_error:
            print(v_error.num)
            print(v_error.msg)


    def __str__(self):
        return  'Type: ' + self.unit_type + '\n' \
                'Life: ' + self.life + '\n' \
                'Speed: ' + self.speed + '\n' \
                'Attack Power: ' + self.attack_power + '\n' \
                'Attack Range: ' + self.attack_range + '\n' \
                'Weapon: ' + self.weapon + '\n'

    def clone(self):
        return deepcopy(self)


class Barracks(object):
    def __init__(self):
        self.units = {
            "Knight": {1:Unit('knight', 1), 2:Unit('knight', 2)},
            "Archer": {1:Unit('archer', 1), 2:Unit('archer', 2)}
        }

    def build_unit(self, p_unit_type, p_level):
        return self.units[p_unit_type.capitalize()][p_level].clone()

if __name__ == '__main__':
    v_barracks = Barracks()
    v_k1 = v_barracks.build_unit('knight',1)
    v_a1 = v_barracks.build_unit('archer',2)
    v_f1 = v_barracks.build_unit('footsoldier',1)
    print('[knight1] ' + str(v_k1))
    print('[archer1] ' + str(v_a1))
