#include "getDesktop.h"
int getDesktop(LPTSTR lpszPath){
HWND   hwndOwner=NULL;
int    csidl=CSIDL_DESKTOPDIRECTORY;
BOOL   fCreate=0;
SHGetSpecialFolderPath(hwndOwner,lpszPath,csidl,fCreate);
	return 0;
}

