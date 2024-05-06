public class Arete {

	private float poids;
	private boolean estOriente;
	private Sommet sommet1;
	private Sommet sommet2;
	
	public Arete(float poids, boolean estOriente, Sommet sommet1, Sommet sommet2) {
		this.poids = poids;
		this.estOriente = estOriente;
		this.sommet1 = sommet1;
		this.sommet2 = sommet2;
	}
	
	public float getPoids() {
		return this.poids;
	}
	
	public boolean isOriente() {
		return this.estOriente;
	}
	
	public Sommet getSommet1() {
		return this.sommet1;
	}
	
	public Sommet getSommet2() {
		return this.sommet2;
	}
	
	public void setPoids(float poids) {
		this.poids = poids;
	}
	
	
}
