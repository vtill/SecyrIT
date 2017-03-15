/*
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
*/
#include "browser.h"
int readDefaultBrowser(char *browser);

int readDefaultBrowser(char *browser){
	LONG lResult;
	//HKEY hKeyRoot=HKEY_LOCAL_MACHINE;
	HKEY hKeyRoot=HKEY_CLASSES_ROOT;
  //LPCTSTR lpSubKey=TEXT("SOFTWARE\\Classes\\http\\shell\\open\\command");
  LPCTSTR lpSubKey=TEXT("http\\shell\\open\\command");
	
  DWORD   ulOptions=0;
  REGSAM  samDesired=KEY_QUERY_VALUE;
	HKEY hKey;

  LPCTSTR lpValueName="";
  LPDWORD lpReserved=NULL;
  DWORD lpType=REG_SZ;
  LPBYTE  lpData=malloc(1000);
  DWORD lpcbData=1000;

	lResult=RegOpenKeyEx (hKeyRoot, lpSubKey, ulOptions, samDesired, &hKey);
	if(lResult != ERROR_SUCCESS){	
		printf("Unable to open registry key");
		return 1;
	}

	if(lpData==NULL){
		printf("fehler beim speicher allokieren");
	}
	RegQueryValueEx(hKey,lpValueName,lpReserved,&lpType,lpData,&lpcbData);

	strcpy(browser,lpData);
	//printf( "the value read from the registry is: %s\n",lpData);
	//
	RegCloseKey(hKey);
	return 0;
}

