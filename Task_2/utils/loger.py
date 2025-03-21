from colorama import init, Fore

# import datetime

init(autoreset=True)


def log(
    message="------------😢 You need to add some text message ",
    level="info",
):

    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    colors = {
        "info": Fore.BLUE,
        "warning": Fore.YELLOW,
        "error": Fore.RED,
        "success": Fore.GREEN,
    }

    color = colors.get(level.lower(), Fore.WHITE)
    # print(f"{color}[{timestamp}] [{level.upper()}]: {message}")
    print(f"{color}[{level.upper()}]: {message}")


# log("Це інформаційне повідомлення", "info")
# log("Це попередження", "warning")
# log("Це повідомлення про помилку", "error")
# log("Це успішне повідомлення", "success")
