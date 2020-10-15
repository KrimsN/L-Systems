from l_system_drawer import LSDrawer
from turtle import Turtle, Screen
from time import sleep
def main():

    cursor = Turtle()

    # ls_rules = {
    #     '+': '+',
    #     '-': '-',
    #     '[': '[',
    #     ']': ']',
    #     'X': 'F-[[X]+X]+F[+FX]-X',
    #     'F': 'FF'
    # }
    ls_rules = {
        'F': '',
        'L': 'FL-FR--FR+FL++FLFL+FR-',
        'R': '+FL-FRFR--FR-FL++FL+FR',
    }
    ls = LSDrawer.create_L_system('FL', 4, ls_rules)

    draw_rules = {
        'F': 'fd(2)',
        '-': 'left(60)',
        '+': 'right(60)',
    }
            
    d = LSDrawer(draw_rules, start_pos=(0, -200), _turtle=cursor)
    
    d.draw(ls)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
