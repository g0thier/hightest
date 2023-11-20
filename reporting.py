import time

def format_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def execution_time(time_start):
    time_end = time.time()
    
    return {'start_time': format_time(time_start),
            'end_time': format_time(time_end),
            'duration': round(time_end - time_start, 2)}

def success_message(time_start):
    return {'status': 'success',
            'execution_time': execution_time(time_start)}

def error_message(time_start, error_message):
    return {'status': 'error',
            'error_message': error_message,
            'execution_time': execution_time(time_start)}