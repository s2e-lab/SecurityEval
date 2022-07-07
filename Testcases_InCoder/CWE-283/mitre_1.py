import os, signal
def killProcess(processID):
    '''
    kill the process with the given processID
    '''
    if processID is None:
        return
    if platform.system() == 'Windows':
        import ctypes
        handle = ctypes.windll.kernel32.OpenProcess(
            0x00000002, False, processID)
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)
    elif platform.system() == 'Darwin':
        os.kill(processID, signal.SIGKILL)
    elif platform.system() == 'Linux':
        os.killpg(processID, signal.SIGKILL)
    elif platform.system() == 'FreeBSD':
        os.kill(processID, signal.SIGKILL)
    elif platform.system() == 'SunOS':
        os.kill(processID, signal.SIGTERM)