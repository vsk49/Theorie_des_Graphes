import java.util.ArrayList;

public class Graphe {

	private ArrayList<Sommet> sommets;
	private ArrayList<Arete> aretes;
	
	public Graphe() {
		this.sommets = new ArrayList<>();
		this.aretes = new ArrayList<>();
	}

	public void ajouterSommet(Sommet s) {
		this.sommets.add(s);
	}
	
	public void ajouterArete(Arete a) {
		this.aretes.add(a);
	}
	
	
}	