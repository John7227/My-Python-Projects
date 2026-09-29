class Video:
    def __init__(self, title:str, duration: int):
        self.title = title
        self.duration = duration
        self.current_playback_position = 0

    def play(self):
        return self.title + " is now playing"

    def advance(self, minutes):
        if(minutes > 1 and minutes <= self.duration):

            if(self.current_playback_position + minutes) > self.duration:
                self.current_playback_position = self.duration
            else:
                self.current_playback_position += minutes

        else:
            raise ValueError("Invalid duration")

        return self.current_playback_position

    def is_finished(self):
        return self.current_playback_position == self.duration

    def restart(self):
        return self.current_playback_position == 0

    def time_remaining(self):
        remaining =  self.duration - self.current_playback_position

        return remaining