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
    def log(text, exc=None):
        if (isinstance(text, BaseException)):
            raise(text)
        elif (exc != None):
            raise(exc(text))
        else:
            print(text)


    @staticmethod
    def header(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['HEADER'], text, Logger.endc)
        Logger.log(msg, exc)

    @staticmethod
    def success(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['SUCCESS'], text, Logger.endc)
        Logger.log(msg, exc)

    @staticmethod
    def info(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['INFO'], text, Logger.endc)
        Logger.log(msg, exc)

    @staticmethod
    def warning(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['WARNING'], text, Logger.endc)
        Logger.log(msg, exc)

    @staticmethod
    def error(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['ERROR'], text, Logger.endc)
        Logger.log(msg, exc)

    @staticmethod
    def bold(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['BOLD'], text, Logger.endc)
        Logger.log(msg, exc)

    @staticmethod
    def underline(text, exc=None):
        msg = "%s%s%s" % (Logger.styles['UNDERLINE'], text, Logger.endc)
        Logger.log(msg, exc)