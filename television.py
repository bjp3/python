class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to turn TV on or off.
        """
        self.__status = not self.__status  #  Turns TV on or off

    def mute(self):
        """
        Method to mute or unmute TV.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Method to increase channel
        """
        if self.__status:  #  Checks to see if the TV is on
            if self.__channel < self.MAX_CHANNEL:  # Checks to see if the channel is greater than 3
                self.__channel += 1  # increases channel by 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease channel
        """
        if self.__status:  #  Checks to see if the TV is on
            if self.__channel > Television.MIN_CHANNEL:  # sets channel to 0
                self.__channel -= 1  # Decreases channel by 1
            else:
                self.__channel = Television.MAX_CHANNEL  # sets channel to 3

    def volume_up(self):
        """
        Method to increase volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Method to decrease volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Prints the output when a print is called
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
