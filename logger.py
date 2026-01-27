from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
  
class Colors:
    def __init__(self):
        self.error = '\033[31m'
        self.success = '\033[32m'
        self.reset = '\033[0m'

class Logger:
    def __init__(self, logFile = './logs/log' ):
        self.logFile = logFile
        self.colors = Colors()
    
    def _log(self, color, message):       
        message == print(f"{color}{message}{self.colors.reset}")
        self._write(message)
    
    def _write(self, message):
        with open(self.logFile, 'a') as f:
            try:
                f.write(f"{now} : {message}\n")
            except Exception as e:
                print(f"Error writing to log file: {e}")
    
    
    
