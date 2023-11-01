"""Task 3 - TV controller
Create a simple prototype of a TV controller in Python.
It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel
numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the
last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel
is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name'
and returns "Yes", if the channel N or 'name' exists in the list,
or "No" - in the other case.

The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    """Simple prototype of a TV controller"""
    def __init__(self, channel_list):
        self.channels = dict(enumerate(channel_list, 1))
        self.current = 1

    def first_channel(self):
        """Turns on the first channel from the list"""
        self.current = 1
        return self.channels[self.current]

    def last_channel(self):
        """Turns on the last channel from the list"""
        self.current = len(self.channels)
        return self.channels[self.current]

    def turn_channel(self, channel_num):
        """Turns on the N channel"""
        if channel_num not in self.channels:
            print(f"Channel number '{channel_num}' does not exist in the channel list")
            return None
        self.current = channel_num
        return self.channels[self.current]

    def next_channel(self):
        """Turns on the next channel.
        If the current channel is the last one, turns on the first channel"""
        self.current = (self.current + 1) if self.current < len(self.channels) else 1
        return self.channels[self.current]

    def previous_channel(self):
        """Turns on the previous channel.
        If the current channel is the first one, turns on the last channel"""
        self.current = (self.current - 1) if self.current > 1 else len(self.channels)
        return self.channels[self.current]

    def current_channel(self):
        """Returns the name of the current channel"""
        return self.channels[self.current]

    def exists(self, search_param):
        """Gets 1 argument - the number N or the string 'name'
        and returns "Yes", if the channel N or 'name' exists in the list,
        or "No" - in the other case"""
        res = any(search_param in pair for pair in self.channels.items())
        return "Yes" if res else "No"


controller = TVController(CHANNELS)
assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.exists(4) == "No"
assert controller.exists("BBC") == "Yes"
