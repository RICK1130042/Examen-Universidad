from experta import *

def get_valid_input(question):
    """Prompt user until a valid 'yes' or 'no' is received."""
    while True:
        answer = input(question).strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Please answer only with 'yes' or 'no'.")

class CardiologyExpertSystem(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield Fact(action="start_diagnosis")

    # === SYMPTOM QUESTIONS ===
    @Rule(Fact(action="start_diagnosis"), NOT(Fact(chest_pain=W())))
    def symptom_chest_pain(self):
        self.declare(Fact(chest_pain=get_valid_input("Do you experience chest pain? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(shortness_of_breath=W())))
    def symptom_breathing(self):
        self.declare(Fact(shortness_of_breath=get_valid_input("Do you experience shortness of breath? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(fatigue=W())))
    def symptom_fatigue(self):
        self.declare(Fact(fatigue=get_valid_input("Do you feel fatigue? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(swelling=W())))
    def symptom_swelling(self):
        self.declare(Fact(swelling=get_valid_input("Do you have swelling in legs or feet? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(palpitations=W())))
    def symptom_palpitations(self):
        self.declare(Fact(palpitations=get_valid_input("Do you feel heart palpitations? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(dizziness=W())))
    def symptom_dizziness(self):
        self.declare(Fact(dizziness=get_valid_input("Do you feel dizzy or faint? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(fever=W())))
    def symptom_fever(self):
        self.declare(Fact(fever=get_valid_input("Do you have a fever? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(murmur=W())))
    def symptom_murmur(self):
        self.declare(Fact(murmur=get_valid_input("Has a doctor told you that you have a heart murmur? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(high_blood_pressure=W())))
    def symptom_pressure(self):
        self.declare(Fact(high_blood_pressure=get_valid_input("Have you been diagnosed with high blood pressure? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(radiating_pain=W())))
    def symptom_radiating_pain(self):
        self.declare(Fact(radiating_pain=get_valid_input("Do you have pain radiating to the arm, neck, jaw or back? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(anxiety=W())))
    def symptom_anxiety(self):
        self.declare(Fact(anxiety=get_valid_input("Do you experience anxiety along with chest discomfort? (yes/no): ")))

    @Rule(Fact(action="start_diagnosis"), NOT(Fact(sharp_pain=W())))
    def symptom_sharp_pain(self):
        self.declare(Fact(sharp_pain=get_valid_input("Do you have sharp chest pain that worsens when lying down? (yes/no): ")))

    # === DIAGNOSIS RULES ===
    @Rule(Fact(high_blood_pressure=True), Fact(dizziness=True))
    def diagnosis_hypertension(self):
        """
        Diagnosis: Hypertension
        Author: Víctor Ángel Martínez Vidaurri
        Source: https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/symptoms-causes/syc-20373410
        """
        print("\nDiagnosis: Hypertension")
        print("Source: https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/symptoms-causes/syc-20373410")
        self.halt()

    @Rule(Fact(chest_pain=True), Fact(radiating_pain=True), Fact(shortness_of_breath=True))
    def diagnosis_heart_attack(self):
        """
        Diagnosis: Myocardial Infarction (Heart Attack)
        Author: Víctor Ángel Martínez Vidaurri
        Source: https://medlineplus.gov/heartattack.html
        """
        print("\nDiagnosis: Myocardial Infarction (Heart Attack)")
        print("Source: https://medlineplus.gov/heartattack.html")
        self.halt()

    @Rule(Fact(palpitations=True), Fact(dizziness=True))
    def diagnosis_arrhythmia(self):
        """
        Diagnosis: Arrhythmia
        Author: Víctor Ángel Martínez Vidaurri
        Source: https://medlineplus.gov/arrhythmia.html
        """
        print("\nDiagnosis: Arrhythmia")
        print("Source: https://medlineplus.gov/arrhythmia.html")
        self.halt()

    @Rule(Fact(fatigue=True), Fact(swelling=True), Fact(shortness_of_breath=True))
    def diagnosis_heart_failure(self):
        """
        Diagnosis: Heart Failure
        Author: Alan Ulises Luna Hernández
        Source: https://medlineplus.gov/heartfailure.html
        """
        print("\nDiagnosis: Heart Failure")
        print("Source: https://medlineplus.gov/heartfailure.html")
        self.halt()

    @Rule(Fact(chest_pain=True), Fact(fatigue=True))
    def diagnosis_coronary_artery_disease(self):
        """
        Diagnosis: Coronary Artery Disease
        Author: Alan Ulises Luna Hernández
        Source: https://www.mayoclinic.org/diseases-conditions/coronary-artery-disease/symptoms-causes/syc-20350613
        """
        print("\nDiagnosis: Coronary Artery Disease")
        print("Source: https://www.mayoclinic.org/diseases-conditions/coronary-artery-disease/symptoms-causes/syc-20350613")
        self.halt()

    @Rule(Fact(chest_pain=True), Fact(anxiety=True))
    def diagnosis_angina(self):
        """
        Diagnosis: Angina
        Author: Alan Ulises Luna Hernández
        Source: https://www.mayoclinic.org/diseases-conditions/angina/symptoms-causes/syc-20369373
        """
        print("\nDiagnosis: Angina")
        print("Source: https://www.mayoclinic.org/diseases-conditions/angina/symptoms-causes/syc-20369373")
        self.halt()

    @Rule(Fact(sharp_pain=True), Fact(fever=True))
    def diagnosis_pericarditis(self):
        """
        Diagnosis: Pericarditis
        Author: Ricardo Villareal Bazán
        Source: https://medlineplus.gov/ency/article/000166.htm
        """
        print("\nDiagnosis: Pericarditis")
        print("Source: https://medlineplus.gov/ency/article/000166.htm")
        self.halt()

    @Rule(Fact(shortness_of_breath=True), Fact(swelling=True), Fact(palpitations=True))
    def diagnosis_cardiomyopathy(self):
        """
        Diagnosis: Cardiomyopathy
        Author: Ricardo Villareal Bazán
        Source: https://www.mayoclinic.org/diseases-conditions/cardiomyopathy/symptoms-causes/syc-20370709
        """
        print("\nDiagnosis: Cardiomyopathy")
        print("Source: https://www.mayoclinic.org/diseases-conditions/cardiomyopathy/symptoms-causes/syc-20370709")
        self.halt()

    @Rule(Fact(chest_pain=True), Fact(dizziness=True))
    def diagnosis_aortic_stenosis(self):
        """
        Diagnosis: Aortic Stenosis
        Author: Ricardo Villareal Bazán
        Source: https://medlineplus.gov/ency/article/000178.htm
        """
        print("\nDiagnosis: Aortic Stenosis")
        print("Source: https://medlineplus.gov/ency/article/000178.htm")
        self.halt()

    @Rule(Fact(fever=True), Fact(murmur=True))
    def diagnosis_endocarditis(self):
        """
        Diagnosis: Endocarditis
        Author: Uziel Heredia Estrada
        Source: https://medlineplus.gov/endocarditis.html
        """
        print("\nDiagnosis: Endocarditis")
        print("Source: https://medlineplus.gov/endocarditis.html")
        self.halt()

    @Rule(Fact(palpitations=True), Fact(anxiety=True))
    def diagnosis_mitral_valve_prolapse(self):
        """
        Diagnosis: Mitral Valve Prolapse
        Author: Uziel Heredia Estrada
        Source: https://www.mayoclinic.org/diseases-conditions/mitral-valve-prolapse/symptoms-causes/syc-20355446
        """
        print("\nDiagnosis: Mitral Valve Prolapse")
        print("Source: https://www.mayoclinic.org/diseases-conditions/mitral-valve-prolapse/symptoms-causes/syc-20355446")
        self.halt()

    @Rule(Fact(shortness_of_breath=True), Fact(fatigue=True), Fact(murmur=True))
    def diagnosis_congenital_heart_defect(self):
        """
        Diagnosis: Congenital Heart Defect
        Author: Uziel Heredia Estrada
        Source: https://www.mayoclinic.org/diseases-conditions/adult-congenital-heart-disease/symptoms-causes/syc-20355456
        """
        print("\nDiagnosis: Congenital Heart Defect")
        print("Source: https://www.mayoclinic.org/diseases-conditions/adult-congenital-heart-disease/symptoms-causes/syc-20355456")
        self.halt()

# === SYSTEM RUNNER ===
def run_expert_system():
    print("=== Welcome to the Cardiology Expert System ===")
    engine = CardiologyExpertSystem()
    engine.reset()
    engine.run()
    print("\n=== Diagnosis complete. Thank you for using the system. ===")

# === LOOP TO START A NEW DIAGNOSIS ===
if __name__ == "__main__":
    while True:
        run_expert_system()
        again = input("\nWould you like to start a new diagnosis? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye, thank you for using the system")
            break
