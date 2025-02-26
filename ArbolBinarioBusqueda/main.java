package ArbolBinarioBusqueda;

public class main {
    
    public static void main(String[] args) {
        // Crear un árbol binario de búsqueda
        Arbol arbol = new Arbol();

        // Insertar nodos
        arbol.insertar(50);
        arbol.insertar(30);
        arbol.insertar(70);
        arbol.insertar(20);
        arbol.insertar(40);
        arbol.insertar(60);
        arbol.insertar(80);

        // Buscar un nodo
        Nodo nodo = arbol.buscarNodo(40);
        if (nodo != null) {
            System.out.println("Nodo encontrado: " + nodo.valor);
        } else {
            System.out.println("Nodo no encontrado");
        }

        // Verificar si el árbol está vacío
        System.out.println("¿El árbol está vacío? " + arbol.vacio());
    }
}
