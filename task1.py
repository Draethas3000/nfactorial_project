class Logger:
    def __init__(self):
        self.logs = {}
        self.max_size = 100

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logs:
            if timestamp < self.logs[message]:
                return False

        self.logs[message] = timestamp + 10

        if len(self.logs) > self.max_size:
            self.clean(timestamp)

        return True

    def clean(self, timestamp: int) -> bool:
        if any(timestamp >= t for t in self.logs.values()):
            self.logs = {msg: t for msg, t in self.logs.items() if t > timestamp}
            return True
        return False

    def loggerSize(self) -> int:
        return len(self.logs)


logger = Logger()

print(logger.shouldPrintMessage(1, "foo"))  # return True
print(logger.shouldPrintMessage(2, "bar"))  # return True
print(logger.shouldPrintMessage(3, "foo"))  # return False
print(logger.shouldPrintMessage(8, "bar"))  # return False
print(logger.shouldPrintMessage(10, "foo"))  # return False
print(logger.shouldPrintMessage(11, "foo"))  # return True
print(logger.loggerSize())
print(logger.clean(12))
