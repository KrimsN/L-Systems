
from turtle import Turtle
import turtle

from typing import Dict







class Drawer:

    

    def __init__(self, draw_rules: Dict[str, str], _turtle: Turtle = Turtle()) -> None:
        self.t = _turtle

        self.draw_rules = draw_rules

        self.t.speed(10)
        self.t.up()
        self.t.setposition(-200,-200)
        self.t.down()
        self.t.resizemode('auto')

        
    
    def draw(self, lsystem: str) -> None:
        for c in lsystem:
            if c in self.draw_rules:
                try:
                    eval(f'self.t.{self.draw_rules[c]}')
                except:
                    print(f'Cant to do {self.draw_rules[c]}')
            else:
                pass

    @staticmethod
    def create_L_system(ls: str, n: int, ls_rules: Dict[str, str]) -> str:
        
        for i in range(n):
            rez = ''
            for c in ls:
                rez += ls_rules[c]
            ls = rez
        return rez




def main():

    ls_rules = {
        'X': 'X+YF+',
        'Y': '-FX-Y',
        'F': 'F',
        '+': '+',
        '-': '-',
    }

    ls = Drawer.create_L_system('FX', 10, ls_rules)

    draw_rules = {
        'F': 'forward(10)',
        '+': 'left(90)',
        '-': 'right(90)',

    }
            
    d = Drawer(draw_rules)
    
    d.draw(ls)
    turtle.mainloop()


if __name__ == "__main__":
    main()
