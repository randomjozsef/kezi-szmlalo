gugi = 0

def on_button_pressed_a():
    global gugi
    if True:
        gugi += 1
        basic.show_number(gugi)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global gugi
    if True:
        gugi -=1
        basic.show_number(gugi)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    if True:
        basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)


