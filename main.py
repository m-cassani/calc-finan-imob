from gui.layout import create_main_window
from gui.controller import run_event_loop

def main():
    window = create_main_window()
    run_event_loop(window)

if __name__ == "__main__":
    main()
