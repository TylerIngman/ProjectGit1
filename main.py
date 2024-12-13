from gui import *
from television import Television


def main():
    tv_1 = Television()
    create_window(tv_1)




def create_window(tv_1) -> None:
    """
    Method to create tkinter gui window
    :param tv_1:
    """
    window = Tk()
    window.title('Remote')
    window.geometry('400x500')
    window.resizable(False, False)

    Gui(window, tv_1)
    window.mainloop()




if __name__ == "__main__":
    main()