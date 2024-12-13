from operator import truediv
from tkinter import *


class Gui:
    def __init__(self, window, tv_1) -> None:
        """
        Method to create gui
        :param window:
        :param tv_1:
        """
        self.window = window
        self.tv_1 = tv_1

        # Screen
        self.screen = Canvas(self.window, width=395, height=200, bg='white')
        self.screen.create_rectangle(0, 0, 395, 200, fill="black", outline="black", width=3)
        self.screen.pack()

        #Channel frame
        self.frame_channel_buttons = Frame(self.window)
        self.channel_up_button = Button(self.frame_channel_buttons, text='Channel +', width = 10, height = 4, bg = 'grey', command = self.channel_up)
        self.channel_down_button = Button(self.frame_channel_buttons, text = 'Channel -', width = 10, height = 4, bg = 'grey', command = self.channel_down)
        self.channel_up_button.pack(padx = 30, pady = 50)
        self.channel_down_button.pack()
        self.frame_channel_buttons.pack(side = "left", padx = 0, pady = 0, anchor = 'n')


        #Volume frame
        self.frame_volume_buttons = Frame(self.window)
        self.volume_up_button = Button(self.frame_volume_buttons, text='Volume +', width=10, height=4, bg='grey', command=self.volume_up)
        self.volume_down_button = Button(self.frame_volume_buttons, text='Volume -', width=10, height=4, bg='grey', command=self.volume_down)
        self.volume_up_button.pack(padx = 30, pady = 50)
        self.volume_down_button.pack()
        self.frame_volume_buttons.pack(side="right", padx=0, pady=0, anchor='n')

        #Mute frame
        self.frame_mute_button = Frame(self.window)
        self.mute_button = Button(self.frame_mute_button, text='Mute', width=10, height=4, bg='grey', command=self.mute)
        self.mute_button.pack()
        self.frame_mute_button.pack(side = "bottom", pady= 30)

        #Power frame
        self.frame_power_button = Frame(self.window)
        self.power_button = Button(self.frame_power_button, text='Power', width=10, height=4, bg='grey', command=self.power)
        self.power_button.pack()
        self.frame_power_button.pack(side="bottom", pady=30)



    def channel_up(self) ->None:
        """
        Tv channel up, update screen
        """
        self.tv_1.channel_up()
        self.screen_update()

    def channel_down(self) -> None:
        """
        Tv channel down, update screen
        """
        self.tv_1.channel_down()
        self.screen_update()

    def volume_up(self) -> None:
        """
        Tv volume up, update screen
        """
        self.tv_1.volume_up()
        self.screen_update()

    def volume_down(self) -> None:
        """
        Tv volume down, update screen
        """
        self.tv_1.volume_down()
        self.screen_update()


    def mute(self) -> None:
        """
        Mute tv, update screen
        """
        self.tv_1.mute()
        self.screen_update()

    def power(self) -> None:
        """
        Power on/off tv, update screen
        """
        self.tv_1.power()
        self.screen_update()




    def screen_update(self) -> None:
        """
        Method to update screen using TV values
        """
        power, channel, volume = self.tv_1.get_status()
        self.screen.delete('all')
        if power:
            if channel == 0:
                self.screen.create_rectangle(147.5, 50, 247.5, 150, fill="green", outline="black", width=3)
            elif channel == 1:
                self.screen.create_rectangle(147.5, 50, 247.5, 150, fill="red", outline="black", width=3)
            elif channel == 2:
                self.screen.create_rectangle(147.5, 50, 247.5, 150, fill="purple", outline="black", width=3)
            elif channel == 3:
                self.screen.create_rectangle(147.5, 50, 247.5, 150, fill="blue", outline="black", width=3)
            self.screen.create_text(3, 3, text="Volume = " + str(volume), anchor='nw')
        else:
            self.screen.create_rectangle(0, 0, 395, 200, fill="black", outline="black", width=3)





