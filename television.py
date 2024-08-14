class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False  # boolean for mute on or off
        self.__status = False # boolean for TV on or off
        self.__volume = Television.MIN_VOLUME  # sets initial volume level to 0
        self.__channel = Television.MIN_CHANNEL # sets initial channel to 0

    def power(self) -> None:
        """
        Method to turn TV on or off.
        """
        self.__status = not self.__status  # Turns TV on or off

    def mute(self) -> None:
        """
        Method to mute or unmute TV.
        """
        if self.__status:  # checks to see if the TV is on
            self.__muted = not self.__muted  # mutes or un-mutes TV based on previous boolean value

    def channel_up(self) -> None:
        """
        Method to increase channel
        """
        if self.__status:  # Checks to see if the TV is on
            if self.__channel < self.MAX_CHANNEL:  # Checks to see if the channel is greater than 3
                self.__channel += 1  # increases channel by 1
            else:
                self.__channel = Television.MIN_CHANNEL  # sets channel to 0

    def channel_down(self) -> None:
        """
        Method to decrease channel
        """
        if self.__status:  # Checks to see if the TV is on
            if self.__channel > Television.MIN_CHANNEL:  # sets channel to 0
                self.__channel -= 1  # Decreases channel by 1
            else:
                self.__channel = Television.MAX_CHANNEL  # sets channel to 3

    def volume_up(self) -> None:
        """
        Method to increase volume.
        """
        if self.__status:  # checks to see if the TV is on
            self.__muted = False  # changes mute to off when volume up button is hit
            if self.__volume < Television.MAX_VOLUME:  # checks volume level to see if it's below the max
                self.__volume += 1  # increases the volume by 1

    def volume_down(self) -> None:
        """
        Method to decrease volume
        """
        if self.__status:  # checks to see if the TV is on
            self.__muted = False  # changes mute to off when volume down button is hit
            if self.__volume > Television.MIN_VOLUME: # checks volume level to see if it's above the minimum
                self.__volume -= 1 # decreases the volume by 1

    def __str__(self) -> str:
        """
        Prints the output when a print is called
        """
        if self.__muted:  # checks to see if TV is muted
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'  # prints the power, channel, and volume
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'  # prints the power, channel, and volume
