from l_system_drawer import Drawer
import turtle

def main():

    # ls_rules = {
    #     'X': 'X+YF+',
    #     'Y': '-FX-Y',
    #     'F': 'F',
    #     '+': '+',
    #     '-': '-',
    # }

    ls_rules = {
        '+': '+',
        '-': '-',
        '[': '[',
        ']': ']',
        'X': 'F-[[X]+X]+F[+FX]-X',
        'F': 'FF'
    }
    ls = Drawer.create_L_system('X', 6, ls_rules)

    draw_rules = {
        'F': 'fd(10)',
        '-': 'left(25)',
        '+': 'right(25)',
    }
            
    d = Drawer(draw_rules, start_pos=(-500,-200))
    
    d.draw(ls)
    turtle.mainloop()


if __name__ == "__main__":
    main()
