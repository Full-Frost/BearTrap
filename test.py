import wmi

w=wmi.WMI()
# The argument (field filter) is only really needed if browsing a large domain
# as per the warning at https://learn.microsoft.com/en-us/windows/desktop/cimwin32prov/win32-useraccount
# Included it for the sake of completeness
DEFAULT_USERS = ['Administrator', 'Guest', 'WDAGUtilityAccount', 'KRBTGT', 'DefaultAccount']
for u in w.Win32_UserAccount(["Name"]): #Net
    if u.Name in DEFAULT_USERS:
        pass
    else:
        print(u.Name)
del u