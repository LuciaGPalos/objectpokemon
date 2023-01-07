from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(30)
        self.spend_attack(30)
        self.spend_defence(40)
        self.add_move(Aumento_de_sueldo())
        self.add_move(Cubiculo_gris())
        self.add_move(Reunion_aburrida())
        self.add_move(Indigestion_en_la_oficina())
        self.set_type(Type.NORMAL)
        self.move = 0
        self.moves = ['Aumento_de_sueldo', "Cubiculo_gris", "Reunion_aburrida", "Indigestion_en_la_oficina"]


    def get_name(self):
        return "Oficinista_frustrado"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Aumento_de_sueldo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Aumento_de_sueldo"

class Cubiculo_gris(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Cubiculo_gris"


class Reunion_aburrida(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Reunion_aburrida"


class Indigestion_en_la_oficina(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Indigestion_en_la_oficina"