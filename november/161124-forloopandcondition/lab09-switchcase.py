from re import match

browser_name = input("enter the string\n")
match browser_name:
    case "firefox":
        print("star firefox")
    case "chrome":
        print("star chrome")
    case "safari":
        print("start safari")
    case  "default":
        print("browser not found")
    