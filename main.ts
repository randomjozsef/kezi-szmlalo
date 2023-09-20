let gugi = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (true) {
        gugi += 1
        basic.showNumber(gugi)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (true) {
        gugi -= 1
        basic.showNumber(gugi)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    if (true) {
        basic.clearScreen()
    }
    
})
