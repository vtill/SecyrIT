#include <stdio.h>
#include <winsock2.h>
#include <iphlpapi.h>
#include <stdio.h>
#include <stdlib.h>

#define MALLOC(x) HeapAlloc(GetProcessHeap(), 0, (x))
#define FREE(x) HeapFree(GetProcessHeap(), 0, (x))

/* Note: could also use malloc() and free() */

char** createCharArray(int m, int n);
void destroyCharArray(char** arr);
PIP_ADAPTER_INFO getAdapterInfo();
int getGateway(PIP_ADAPTER_INFO pAdapter,char **gateway);
int printComboIndex(PIP_ADAPTER_INFO pAdapter);
int printAdapterName(PIP_ADAPTER_INFO pAdapter);
int printDescription(PIP_ADAPTER_INFO pAdapter);
int printAdapterAddr(PIP_ADAPTER_INFO pAdapter);
int printIndex(PIP_ADAPTER_INFO pAdapter);
int printType(PIP_ADAPTER_INFO pAdapter);
int printIPAddress(PIP_ADAPTER_INFO pAdapter);
int printIPMask(PIP_ADAPTER_INFO pAdapter);
int printGateway(PIP_ADAPTER_INFO pAdapter);
int printWins(PIP_ADAPTER_INFO pAdapter);
int printDhcp(PIP_ADAPTER_INFO pAdapter);
int printAdapterInfo(PIP_ADAPTER_INFO pAdapter);
int test();
