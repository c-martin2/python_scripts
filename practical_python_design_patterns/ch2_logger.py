class Logger(object):
    class __Logger():
        def __init__(self, p_file_name):
            self.file_name = file_name

        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)

        def _write_log(self, p_level, p_msg):
            """Write message to file_name specified for instance"""
            with open(self.file_name, 'a') as v_log_file:
                v_log_file.write('[' + p_level + '] ' + p_msg + '\n')

        def critical(self, p_msg):
            self._write_log('CRITICAL', p_msg)

        def error(self, p_msg):
            self._write_log('ERROR', p_msg)

        def warn(self, p_msg):
            self._write_log('WARN', p_msg)

        def info(self, p_msg):
            self._write_log('INFO', p_msg)

        def debug(self, p_msg):
            self._write_log('DEBUG', p_msg)

    instance = None

    def __new__(cls, p_file_name):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(p_file_name)

        return Logger.instance

    def __getattr__(self, p_name):
        return getattr(self.instance, p_name)

    def __setattr__(self, p_name):
        return setattr(self.instance, p_name)
