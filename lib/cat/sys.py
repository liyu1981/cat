from concurrent.futures import ThreadPoolExecutor

import .conf

s = conf.get('sys')

thread_pool = None

def get_thread_pool():
    if thread_pool == None:
        thread_pool = ThreadPoolExecutor(
            s['thread_pool_threads'] if 'thread_pool_threads' in s else 4)

    return thread_pool