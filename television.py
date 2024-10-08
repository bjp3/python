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
        self.__status = not self.__status

    def mute(self):
        self.__prev_volume = self.__volume
        if self.__status:
            self.__muted = True
            self.__volume = Television.MIN_VOLUME
        else:
            self.__volume = self.__prev_volume
            self.__muted = False

    def channel_up(self):
        if self.__status:
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
        elif self.__status and self.__muted:
            self.__volume = self.__prev_volume + 1

    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
        elif self.__status and self.__muted:
            self.__volume = self.__prev_volume - 1

    def __str__(self):
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'