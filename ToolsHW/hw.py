import os, sys, webbrowser

VIDEO_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
QUESTION = "1 times 1 = ?"
CORRECT_ANSWER = "1"

def ask_question(question: str, correct_answer: str):
    while True:
        user_input = input(question)
        if user_input == correct_answer: 
            open_video(VIDEO_LINK)
            break
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")

def open_video(video_link: str):
    os.system("echo 'Rickroll incoming...'")
    webbrowser.open(video_link)

ask_question(QUESTION, CORRECT_ANSWER)
