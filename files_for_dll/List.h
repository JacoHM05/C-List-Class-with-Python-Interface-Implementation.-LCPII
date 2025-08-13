#include "Node.h"

class List{

   private:

      Node * head;
      Node * tail;
      int elemCount;
   
   public:

      //Constructor
      List();

      //destructor
      ~List();

      //Insert at front
      void append(int val);

      //Deletes first node
      void deleteFirst();

      //Deletes last node
      void deleteLast();

      //print list
      const char * printlist(List * list);



      
};