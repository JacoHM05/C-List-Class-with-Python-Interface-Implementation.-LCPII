#include "List.h"
#include "Node.h"
#include <iostream>
using namespace std;



   List::List(){
      
      head = nullptr;
      tail = nullptr;
      elemCount = 0;
   }

   List::~List(){
      Node * current = head;
      while(head != nullptr){
         head = head->next;
         delete current;
         current = head;
      }

      head = nullptr;
      tail = nullptr;
   }

   void List::append(int val) {
    Node* newNode = new Node(val);

    if (head == nullptr) {
        head = newNode;
        tail = newNode;
    } else {
        tail->next = newNode;
        tail = newNode;
    }

    elemCount++;
}


   void List::deleteFirst(){

      if(head == nullptr){
         return;
      }

      Node * NodetoDelete = head;
      head = head->next;
      delete NodetoDelete;

      if(head == nullptr){
         tail = nullptr;
      }
      elemCount--;
   }

   void List::deleteLast(){

      if(head == tail){
         
         delete head;

         head = nullptr;
         tail = nullptr;
         return;
      }

      Node * current = head;

      while(current->next != tail){
         current = current->next;
      }

      delete tail;
      tail = current;
      current->next = nullptr;

      elemCount--;
   }

    const char* List::printlist(List* list) {
        static std::string output;
        output.clear();

        Node* current = list->head;
        output += "The list has " + std::to_string(list->elemCount) + " elements: ";

        while (current != nullptr) {
            output += "[ " + std::to_string(current->data) + " ], ";
            current = current->next;
        }

        return output.c_str();  // returns pointer to the internal string buffer
    }



