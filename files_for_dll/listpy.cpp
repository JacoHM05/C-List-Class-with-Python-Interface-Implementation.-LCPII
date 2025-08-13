#include "List.h"



    extern "C" __declspec(dllexport) List * listcreate(){
      return new List;
   }

   extern "C" __declspec(dllexport) void listdestroy(List * l){
      delete l;
   }

   extern "C" __declspec(dllexport) void listappend(List * l, int val){

      l->append(val);
   }

   extern "C" __declspec(dllexport) void listdeleteFirst(List * l){
      l->deleteFirst();
   }

   extern "C" __declspec(dllexport) void listdeleteLast(List * l){
      l->deleteLast();
   }
   
   extern "C" __declspec(dllexport) const char * listprint(List * l){
      return l->printlist(l);
   }
