from datetime import time


class StopWatch:
    def __init__(self):

        self.start_time = None
        self.stop_time = None
        self.start() #activeer (mag je nu als doen bij init want bij toekennen van iets aan dit classe zal de methode al in place zijn

    def start(self):
        self.start_time= time.time()    #nog geen return, da is voor "get...."

    def stop(self):
        self.stop_time= time.time()

    def get_start_time(self):
        return self.start_time
    def get_end_time(self):
        return self.stop_time
    def get_elapsed_time(self):
        return int(self.stop_time-self.start_time)    #omzetten tot milisec


