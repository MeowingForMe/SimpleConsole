def newConsole():
    print("Loading...")
    time.sleep(1)
    clear()
    print(f'''{Fore.RED}
               ███▄    █  ██▓ ██░ ██  ██▓     ██▓  ██████  ███▄ ▄███▓
               ██ ▀█   █ ▓██▒▓██░ ██▒▓██▒    ▓██▒▒██    ▒ ▓██▒▀█▀ ██▒
               ▓██  ▀█ ██▒▒██▒▒██▀▀██░▒██░    ▒██▒░ ▓██▄   ▓██    ▓██░
               ▓██▒  ▐▌██▒░██░░▓█ ░██ ▒██░    ░██░  ▒   ██▒▒██    ▒██ 
               ▒██░   ▓██░░██░░▓█▒░██▓░██████▒░██░▒██████▒▒▒██▒   ░██▒
               ░ ▒░   ▒ ▒ ░▓   ▒ ░░▒░▒░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░
               ░ ░░   ░ ▒░ ▒ ░ ▒ ░▒░ ░░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░░  ░      ░
                  ░   ░ ░  ▒ ░ ░  ░░ ░  ░ ░    ▒ ░░  ░  ░  ░      ░   
                        ░  ░   ░  ░  ░    ░  ░ ░        ░         ░ {Fore.RESET}

                                  ADMIN   |   {bot.user}
                                  PREFIX  |   {bot.command_prefix}

''')


newConsole()


@bot.listen()
async def on_command_completion(nighty):
    if nighty.command.name == 'cls':
        clear()
        print(f'''{Fore.RED}
               ███▄    █  ██▓ ██░ ██  ██▓     ██▓  ██████  ███▄ ▄███▓
                ██ ▀█   █ ▓██▒▓██░ ██▒▓██▒    ▓██▒▒██    ▒ ▓██▒▀█▀ ██▒
               ▓██  ▀█ ██▒▒██▒▒██▀▀██░▒██░    ▒██▒░ ▓██▄   ▓██    ▓██░
               ▓██▒  ▐▌██▒░██░░▓█ ░██ ▒██░    ░██░  ▒   ██▒▒██    ▒██ 
               ▒██░   ▓██░░██░░▓█▒░██▓░██████▒░██░▒██████▒▒▒██▒   ░██▒
               ░ ▒░   ▒ ▒ ░▓   ▒ ░░▒░▒░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░
               ░ ░░   ░ ▒░ ▒ ░ ▒ ░▒░ ░░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░░  ░      ░
                  ░   ░ ░  ▒ ░ ░  ░░ ░  ░ ░    ▒ ░░  ░  ░  ░      ░   
                        ░  ░   ░  ░  ░    ░  ░ ░        ░         ░ {Fore.RESET}

                                      ADMIN  |   {bot.user}
                                      PREFIX |   {bot.command_prefix}
        ''')
