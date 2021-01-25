# timer.py

import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class CumulativeTimer:
    def __init__(self):
        self._start_time = None
        self._cumulative_elapsed = 0.0

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self, message=""):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._cumulative_elapsed += elapsed_time
        self._start_time = None
        print(f"{message} time: {elapsed_time:0.4f} sec.  Total: {self._cumulative_elapsed:0.4f} sec")

    def finish(self):
        print(f"Cumulative elapsed time: {self._cumulative_elapsed:0.4f} seconds")        
