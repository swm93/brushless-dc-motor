class Logger:
    styles = {
        'HEADER': '\033[95m',
        'SUCCESS': '\033[92m',
        'INFO': '\033[94m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }
    endc = '\033[0m'

    @staticmethod
    def header(text):
        msg = "%s%s%s" % (Logger.styles['HEADER'], text, Logger.endc)
        print(msg)
        return msg

    @staticmethod
    def success(text):
        msg = "%s%s%s" % (Logger.styles['SUCCESS'], text, Logger.endc)
        print(msg)
        return msg

    @staticmethod
    def info(text):
        msg = "%s%s%s" % (Logger.styles['INFO'], text, Logger.endc)
        print(msg)
        return msg

    @staticmethod
    def warning(text):
        msg = "%s%s%s" % (Logger.styles['WARNING'], text, Logger.endc)
        print(msg)
        return msg

    @staticmethod
    def error(text):
        msg = "%s%s%s" % (Logger.styles['ERROR'], text, Logger.endc)
        print(msg)
        return msg

    @staticmethod
    def bold(text):
        msg = "%s%s%s" % (Logger.styles['BOLD'], text, Logger.endc)
        print(msg)
        return msg

    @staticmethod
    def underline(text):
        msg = "%s%s%s" % (Logger.styles['UNDERLINE'], text, Logger.endc)
        print(msg)
        return msg