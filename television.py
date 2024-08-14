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
        self.__status = not self.__status   #  Turns TV on or off

    def mute(self):
        """
        Method to mute or unmute TV.
        """
          # Saves current volume
        if self.__status and not self.__muted:  #  Checks to see if the TV is on
            self.__muted = True  #  Sets TV to mute
            self.__volume = Television.MIN_VOLUME  #  Sets volume to 0
        elif self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume
        elif not self.__status:
            return None
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
        if self.__status and not self.__muted:  # Checks to see if TV is on and if it's not muted
            if self.__volume < Television.MAX_VOLUME:  # Checks volume to make sure it's not maxed
                self.__volume += 1  # increases volume by 1
        elif self.__status and self.__muted:  #  Checks to see if TV is on and if it's on mute
            self.__volume = self.__prev_volume + 1
        self.__prev_volume = self.__volume

    def volume_down(self):
        """
        Method to decrease volume
        """
        if self.__status and not self.__muted:# Checks to see if TV is on and if it's not muted
            if self.__volume > Television.MIN_VOLUME:  # Checks volume to make sure it's not at minimum
                self.__volume -= 1  # decreases volume by 1
        elif self.__status and self.__muted:#  Checks to see if TV is on and if it's on mute
            self.__volume = self.__prev_volume - 1  # decreases volume by 1
        self.__prev_volume = self.__volume

    def __str__(self):
        """
        Prints the output when a print is called
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'