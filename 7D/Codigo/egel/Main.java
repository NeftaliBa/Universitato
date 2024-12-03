class Animal {
    public String sonido() {
        return "Sonido desconocido"; 
    }
    public String sonido(String tipo) {
        return "Sonido de " + tipo; 
    }
}
class Perro extends Animal {
    @Override
    public String sonido() {
        return "Guau guau";
    }
}
class Gato extends Animal {
    @Override
    public String sonido() {
        return "Miau miau";
    }
}
public class Main {
    public static void main(String[] args) {
        Animal miPerro = new Perro(); 
        Animal miGato = new Gato();   
        System.out.println("Sonido desconocido: " + miPerro.sonido("perro"));
        System.out.println("Sonido desconocido: " + miGato.sonido("gato"));  
    }
}
