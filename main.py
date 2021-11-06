from contextlib import ContextDecorator
import datetime


class LogFile(ContextDecorator):
    """
    Context manager which logs function execution.

    It writes time of beginning, runtime and error (if exists)
    in format:
    'Start: 2021-03-22 12:38:24.757637 | Run: 0:00:00.000054 | An error occurred: None'
    """
    def __init__(self, logfile):
        super().__init__()
        self.logfile = logfile

    def __enter__(self):
        with open(self.logfile, 'a') as f:
            f.write(f"Start: {datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S')} | ")
            self.start = datetime.datetime.now()
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.logfile, 'a') as f:
            self.end = datetime.datetime.now()
            f.write(f'Run: {str(self.end - self.start)} | ')
            f.write(f"An error occurred: {exc_val}\n")
            return True
