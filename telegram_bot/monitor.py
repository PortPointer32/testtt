import subprocess

if __name__ == '__main__':
    while True:
        try:
            subprocess.run(["/home/str/testtt/.venv/bin/python", "/home/str/testtt/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
