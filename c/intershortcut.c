#include "intershortcut.h"

HRESULT CreateInterShortcut (LPCSTR pszURL, LPCSTR pszURLfilename)
{
 HRESULT hres;
 IUniformResourceLocator *pHook;
 hres = CoCreateInstance (&CLSID_InternetShortcut, NULL, CLSCTX_INPROC_SERVER,&IID_IUniformResourceLocator, (void **)&pHook);
 if (SUCCEEDED (hres))
 {
  IPersistFile *ppf;
  IShellLink *psl;

  hres = pHook->lpVtbl->QueryInterface (pHook,&IID_IPersistFile, (void **)&ppf);
  hres = pHook->lpVtbl->QueryInterface (pHook,&IID_IShellLink, (void **)&psl);
  if (SUCCEEDED (hres))
  { 
   WORD wsz [MAX_PATH]; 
   hres=pHook->lpVtbl->SetURL(pHook,pszURL,0);
   if (SUCCEEDED (hres))
   {
		 // Ensure that the string consists of ANSI characters.
		 MultiByteToWideChar (CP_ACP, 0, pszURLfilename, -1, wsz, MAX_PATH);
		 // Save the shortcut via the IPersistFile::Save member function.
		 hres = ppf->lpVtbl->Save (ppf,wsz, TRUE);
   }
   // Release the pointer to IPersistFile.
   ppf->lpVtbl->Release (ppf);
   psl->lpVtbl->Release (psl);
  }
  // Release the pointer to IShellLink.
  pHook->lpVtbl->Release (pHook);
 }
 return hres;
}


