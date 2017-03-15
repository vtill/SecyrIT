#include "gateway.h"
#include "intershortcut.h"
#include "getDesktop.h"

int main(){
	PIP_ADAPTER_INFO pAdapterInfo;
	char **gateway;
	char *desktop;
	char *url;
	char *filepath;
	int count;

	HRESULT hr;
	hr = CoInitialize(NULL);
	if (FAILED(hr)){
		return 1;
	}

	gateway=createCharArray(10,50);
	desktop=malloc(100+sizeof(char));
	url=malloc(100+sizeof(char));
	filepath=malloc(100+sizeof(char));

	pAdapterInfo=getAdapterInfo();
	count=getGateway(pAdapterInfo,gateway);
	printf("%s\n",gateway[0]);

	getDesktop(desktop);
	printf("%s\n",desktop);

	sprintf(url,"http://%s",gateway[0]);
	printf("%s\n",url);
	sprintf(filepath,"%s\\secyrIT.url",desktop);
	printf("%s\n",filepath);

	CreateInterShortcut (url, filepath);
	//CreateInterShortcut ("http://192.168.1.1", "d:\\shit.url");
	//CreateInterShortcut ("http://192.168.1.1","C:\\Users\\IsI\\Desktop\\secyrIT.url");
	CoUninitialize();
	return 0;
	return 0;
}
