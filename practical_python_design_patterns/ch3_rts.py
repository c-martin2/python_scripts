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
        from os import listdir

        v_files = listdir('ch3_parms')
        self.units = {}
        for v_file in v_files:
            v_file_parts = v_file.split('_')
            v_unit_type = v_file_parts[0].capitalize()
            v_level = int(v_file_parts[1])
            if not v_unit_type in self.units:
                self.units[v_unit_type] = {}
            self.units[v_unit_type][v_level] = Unit(v_unit_type, v_level)

    def build_unit(self, p_unit_type, p_level):
        v_unit_type =  p_unit_type.capitalize()
        if not v_unit_type in self.units:
            raise AssertionError('Invalid unit type: ' + p_unit_type)
        if not p_level in self.units[v_unit_type]:
            raise AssertionError('Invalid level for ' + p_unit_type + ': ' + str(p_level))
        return self.units[v_unit_type][p_level].clone()

if __name__ == '__main__':
    v_barracks = Barracks()
    v_k1 = v_barracks.build_unit('knight',1)
    v_a1 = v_barracks.build_unit('archer',2)
    print('[knight1] ' + str(v_k1))
    print('[archer1] ' + str(v_a1))
    v_f1 = v_barracks.build_unit('footsoldier',1)
    print('[footsoldier1] ' + str(v_f1))
