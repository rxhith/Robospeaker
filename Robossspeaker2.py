import pyttsx3
def main():
    engine = pyttsx3.init()
    print("Welcome to Robo speaker created by Rohith.")
    while True:

        x = input("Enter what you want to pronounce: ")
        if x=="q":
            engine.say("bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

if __name__ == "__main__":
    main()
