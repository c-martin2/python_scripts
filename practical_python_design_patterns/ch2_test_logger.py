from ch2_logger import Logger

v_log = Logger('test.log')

print('Log1: ' + v_log.file_name)

v_log.info('test info')

v_log.debug('test debug')

v_log2 = Logger('test2.log')

print('Log1: ' + v_log.file_name)
print('Log2: ' + v_log2.file_name)

v_log2.info('test info2')
