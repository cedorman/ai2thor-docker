#
# A class to determine how much time, individually and cumulatively, is
# taken doing something.  Also keeps track of amount of time (individually
# and cumulative) _NOT_ doing something.
# 

import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class CumulativeTimer:
    def __init__(self):
        self._overall_start_time = time.perf_counter()
        self._start_time = None
        self._cumulative_elapsed = 0.0

        self._non_time = time.perf_counter()
        self._cumulative_non = 0.0
        
    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        elapsed_non = time.perf_counter() - self._non_time
        self._cumulative_non += elapsed_non
        print(f"Non internal time: {elapsed_non:0.4f} sec.  Total non: {self._cumulative_non:0.4f} sec")        
        self._start_time = time.perf_counter()

    def stop(self, message=""):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._non_time = time.perf_counter()
        self._cumulative_elapsed += elapsed_time
        self._start_time = None
        print(f"{message} time: {elapsed_time:0.4f} sec.  Total: {self._cumulative_elapsed:0.4f} sec")

    def finish(self):
        print(f"Cumulative elapsed time: {self._cumulative_elapsed:0.4f} seconds")
        print(f"Cumulative non time: {self._cumulative_non:0.4f} seconds")
        total_time = self._cumulative_non + self._cumulative_elapsed
        print(f"Total time: {total_time:0.4f} seconds")
