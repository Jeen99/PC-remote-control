import win32api, win32gui, win32con
import commctrl
def main():
    try:
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
        
        if len(sys.argv) == 1:
            show(key)
        else:
            name, value = sys.argv[1].split('=')
            if name.upper() == 'PATH':
                value = queryValue(key, name) + ';' + value
            if value:
                SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
            else:
                DeleteValue(key, name)
            
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
                            
    except e:
        print (e)

    CloseKey(key)    
    CloseKey(reg) 
main()