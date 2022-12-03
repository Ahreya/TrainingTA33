class Student:
  numar_studenti = 0 # atribut, apartine clasei Student =? variabila de clasa
  
  def __init__(self, nume, prenume, medie):
    self.nume = nume # variabila care apartine obiectului => var de instanta/obiect
    self.prenume = prenume # variabila care apartine obiectului => var de instanta/obiect
    self.medie = medie # variabila care apartine obiectului => var de instanta/obiect
    
   # Referirea la variabila de instanță nume se face cu notația self.nume în metodele acelui obiect
    print("Initializare studenti: ",self.nume,self.prenume)
    # Referirea la variabila de clasă numar_studenti se face cu notaţia Student.numar_studenti şi nu cu self.numar_studenti
    Student.numar_studenti += 1

  def test_bursier(self):
    
   if self.medie>=9.50:
    print("Bursa de merit")
   elif 8.50<=self.medie<9.50:
    print("Bursa studiu")

# O variabilă de obiect cu același nume ca o variabilă de clasă, va ascunde variabila de clasă faţă de metodele clasei! 
# Metoda nr_studenti este în fapt o metodă  a clasei şi nu a instanţei. Asta înseamnă că trebuie să o definim cu declaraţia static method. 

  def nr_studenti():
    print("Exista",Student.numar_studenti,"instante.")
  nr_studenti = staticmethod(nr_studenti)
  
student1 = Student('Bucur','Tudor',10)
student1.test_bursier()
Student.nr_studenti()
student2 = Student('Enache','Stefan',9)
student2.test_bursier()
Student.nr_studenti()
