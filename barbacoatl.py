from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(1)
        self.spend_attack(0)
        self.spend_defence(99)
        self.add_move(picar_lengua())
        self.add_move(solo_maciza())
        self.add_move(estomago_fuerte())
        self.add_move(en_caldo())
        self.set_type(Type.WATER)
        self.move = 0
        self.moves = ['Te_pica_la_lengua', "Solo_maciza", "Dolor_de_estomago", "Barbacoa_en_caldo"]


    def get_name(self):
        return "Barbacoatl"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Te_pica_la_lengua(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Te pica la lengua!"

class Solo_maciza(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Solo maciza!"


class Dolor_de_estomago(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Dolor de estomago!"


class Barbacoa_en_caldo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Barbacoa en caldo!"
