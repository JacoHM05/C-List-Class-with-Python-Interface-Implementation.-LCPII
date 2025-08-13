extern "C"{                       //Funciones que seran exportadas

      __declspec(dllexport) int add(int x, int y){                      //__declrspec(dllexport) obligatorio
            int sum = x + y;
            return sum;
      }

      
}