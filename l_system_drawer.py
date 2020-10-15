from turtle import Turtle


from typing import Dict


class Drawer:


    def __init__(self, draw_rules: Dict[str, str], _turtle: Turtle = Turtle(), start_pos = (-100, -100), speed = 10) -> None:
        self.t = _turtle

        self.draw_rules = draw_rules

        self.t.speed(speed)
        self.t.up()
        self.t.setposition(start_pos)
        self.t.down()
        self.t.resizemode('auto')

        
    
    def draw(self, lsystem: str) -> None:
        self.stack = []
        for c in lsystem:
            if c in self.draw_rules:
                try:
                    eval(f'self.t.{self.draw_rules[c]}')
                except:
                    print(f'Cant to do {self.draw_rules[c]}')
            elif c == '[':
                pos = self.t.pos()
                ang = self.t.heading()
                self.stack.append((pos, ang))

            elif c == ']':
                pos, ang = self.stack.pop()
                
                self.t.up()
                self.t.setpos(pos)
                self.t.setheading(ang)
                self.t.down()

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

