import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)

anser_box1 = Rect(0,0,300,150)
anser_box2 = Rect(0,0,300,150)
anser_box3 = Rect(0,0,300,150)
anser_box4 = Rect(0,0,300,150)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)

anser_box1.move_ip(20,270)
anser_box2.move_ip(370,270)
anser_box3.move_ip(20,450)
anser_box4.move_ip(370,450)

score = 0
time_left = 10
question_file_name = "C:/Users/Berdien/Desktop/python game developer/Lesson 10/questions.txt"
marquee_message = ""
is_game_over = 10

anserboxes = [anser_box1,anser_box2,anser_box3,anser_box4]
questions = []
question_count = 0 #total
question_index = 0 #current question

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box,"black")

    screen.draw.filled_rect(question_box,"green")

    screen.draw.filled_rect(timer_box,"purple")

    screen.draw.filled_rect(skip_box,"blue")

    for i in anserboxes:
        screen.draw.filled_rect(i,"pink")

    marquee_message = "Welcome to Quiz Master.."+f"Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box, color = "white")

    screen.draw.textbox("Skip",skip_box, color = "white",angle = -90)

    screen.draw.textbox(str(score),timer_box, color = "white")

    screen.draw.textbox(question[0].strip(),question_box, color = "white")
    index = 1
    for i in anserboxes:
        screen.draw.textbox(question[index].strip(),i,color = "white")
        index = index + 1

def marqueeboxmove():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH



def update():
    marqueeboxmove()




question = ["Question....","ans1","ans2","ans3","ans4","1"]




pgzrun.go()
