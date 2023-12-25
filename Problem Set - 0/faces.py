def main():
    text = input()
    convertEmoji(text)

def convertEmoji (inputString):
    inputString=inputString.replace(":)", "🙂")
    inputString=inputString.replace(":(", "🙁")
    print(inputString)

main()
