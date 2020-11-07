import play
#wallpaper
play.set_backdrop("darkorange")
#images
photo = play.new_image(image = "1.jpg", x = 0, y = 0, size = 20, angle= 0 , transparency= 100)
#text
text = play.new_text(words =  "Happy", x =0, y = 200, font = None, font_size= 100, color = "yellow")
@play.when_program_starts
def start():
    pass

@play.repeat_forever
def do():
    if play.key_is_pressed('e'):
        photo.image = "1.jpg"
        text.words = "Happy"
        text.color = "Yellow"
    if play.key_is_pressed('w'):
        photo.image = "2.jpg"
        text.words = "Sad"
        text.color = "Blue"
    if play.key_is_pressed('a'):
        photo.image = "3.png"
        text.words = "Angry"
        text.color = "REd"
    if play.key_is_pressed('s'):
        photo.image = "4.png"
        text.words = "Neutral"
        text.color = "White"
    if play.key_is_pressed('d'):
        photo.image = "5.png"
        text.words = "Sleepy"
        text.color = "Green"

play.start_program()
