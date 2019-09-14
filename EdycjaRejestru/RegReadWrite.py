import winreg

COM_PATH = r"sciezka do rejestru"



def set_reg(name, value,reg_path):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name, reg_path):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
        print(registry_key)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


#Read value
print (get_reg('COM1', COM_PATH))
print (get_reg('COM2', COM_PATH))
#Ustaw Rejestr comów
set_reg('COM1', 2, COM_PATH)
set_reg('COM2', 2, COM_PATH)
