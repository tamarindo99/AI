import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import random

class RunningGoalRecommender:
    # Constants for input ranges
    MIN_AGE = 18
    MAX_AGE = 70
    MIN_WEIGHT = 40.0
    MAX_WEIGHT = 120.0
    MIN_FITNESS = 1
    MAX_FITNESS = 10
    
    def __init__(self):
        # Create the fuzzy control system
        self.create_fuzzy_system()
        
    def create_fuzzy_system(self):
        # Input variables
        self.genero = ctrl.Antecedent(np.arange(0, 2, 1), 'GENERO')
        self.edad = ctrl.Antecedent(np.arange(18, 71, 1), 'EDAD')
        self.peso = ctrl.Antecedent(np.arange(40, 121, 1), 'PESO')
        self.condicion_fisica = ctrl.Antecedent(np.arange(1, 11, 1), 'CONDICION_FISICA')
        self.historia_lesiones = ctrl.Antecedent(np.arange(0, 11, 1), 'HISTORIA_LESIONES')
        self.nutricion = ctrl.Antecedent(np.arange(1, 11, 1), 'NUTRICION')
        self.horas_sueno = ctrl.Antecedent(np.arange(4, 11, 1), 'HORAS_SUENO')
        self.consumo_agua = ctrl.Antecedent(np.arange(1, 6, 1), 'CONSUMO_AGUA')
        self.uso_suplementos = ctrl.Antecedent(np.arange(0, 2, 1), 'USO_SUPLEMENTOS')
        self.frecuencia_entrenamiento = ctrl.Antecedent(np.arange(1, 8, 1), 'FRECUENCIA_ENTRENAMIENTO')
        self.tiempo_corriendo = ctrl.Antecedent(np.arange(0, 1000, 1), 'TIEMPO_CORRIENDO')
        self.tiempo_sin_correr = ctrl.Antecedent(np.arange(0, 100, 1), 'TIEMPO_SIN_CORRER')
        
        # Output variable
        self.meta_a_correr = ctrl.Consequent(np.arange(0, 6, 0.1), 'META_A_CORRER')
        
        # Membership functions
        self.setup_membership_functions()
        
        # Rules
        self.setup_rules()
        
        # Control system
        self.running_ctrl = ctrl.ControlSystem(self.rules)
        self.running_sim = ctrl.ControlSystemSimulation(self.running_ctrl)
    
    def setup_membership_functions(self):
        # Gender (0 = female, 1 = male)
        self.genero['MUJER'] = fuzz.trimf(self.genero.universe, [0, 0, 1])
        self.genero['HOMBRE'] = fuzz.trimf(self.genero.universe, [0, 1, 1])
        
        # Age
        self.edad['NINO'] = fuzz.trimf(self.edad.universe, [5, 5, 12])
        self.edad['ADOLESCENTE'] = fuzz.trimf(self.edad.universe, [10, 18, 25])
        self.edad['JOVEN_ADULTO'] = fuzz.trimf(self.edad.universe, [20, 30, 40])
        self.edad['ADULTO'] = fuzz.trimf(self.edad.universe, [35, 50, 60])
        self.edad['MAYOR'] = fuzz.trimf(self.edad.universe, [55, 70, 70])
        
        # Weight
        self.peso['MUY_LIVIANO'] = fuzz.trimf(self.peso.universe, [20, 35, 35])
        self.peso['LIVIANO'] = fuzz.trimf(self.peso.universe, [30, 50, 60])
        self.peso['NORMAL'] = fuzz.trimf(self.peso.universe, [50, 70, 85])
        self.peso['SOBREPESO'] = fuzz.trimf(self.peso.universe, [75, 95, 110])
        self.peso['OBESO'] = fuzz.trimf(self.peso.universe, [100, 120, 120])
        
        # Fitness level
        self.condicion_fisica['MUY_MALA'] = fuzz.trimf(self.condicion_fisica.universe, [1, 1, 2])
        self.condicion_fisica['MALA'] = fuzz.trimf(self.condicion_fisica.universe, [1, 3, 5])
        self.condicion_fisica['REGULAR'] = fuzz.trimf(self.condicion_fisica.universe, [4, 6, 7])
        self.condicion_fisica['BUENA'] = fuzz.trimf(self.condicion_fisica.universe, [6, 8, 9])
        self.condicion_fisica['EXCELENTE'] = fuzz.trimf(self.condicion_fisica.universe, [8, 10, 10])
        
        # Injury history
        self.historia_lesiones['NINGUNA'] = fuzz.trimf(self.historia_lesiones.universe, [0, 0, 2])
        self.historia_lesiones['LEVE'] = fuzz.trimf(self.historia_lesiones.universe, [1, 4, 6])
        self.historia_lesiones['MODERADA'] = fuzz.trimf(self.historia_lesiones.universe, [5, 7, 9])
        self.historia_lesiones['GRAVE'] = fuzz.trimf(self.historia_lesiones.universe, [8, 10, 10])
        
        # Nutrition
        self.nutricion['MALA'] = fuzz.trimf(self.nutricion.universe, [1, 1, 3])
        self.nutricion['REGULAR'] = fuzz.trimf(self.nutricion.universe, [2, 5, 7])
        self.nutricion['BUENA'] = fuzz.trimf(self.nutricion.universe, [6, 8, 10])
        
        # Sleep hours
        self.horas_sueno['INSUFICIENTE'] = fuzz.trimf(self.horas_sueno.universe, [4, 4, 5])
        self.horas_sueno['MINIMO'] = fuzz.trimf(self.horas_sueno.universe, [4, 6, 7])
        self.horas_sueno['ADECUADO'] = fuzz.trimf(self.horas_sueno.universe, [6, 8, 9])
        self.horas_sueno['EXCESIVO'] = fuzz.trimf(self.horas_sueno.universe, [8, 10, 10])
        
        # Water intake
        self.consumo_agua['BAJO'] = fuzz.trimf(self.consumo_agua.universe, [1, 1, 2])
        self.consumo_agua['MODERADO'] = fuzz.trimf(self.consumo_agua.universe, [1, 3, 4])
        self.consumo_agua['ALTO'] = fuzz.trimf(self.consumo_agua.universe, [3, 5, 5])
        
        # Supplement use
        self.uso_suplementos['NO'] = fuzz.trimf(self.uso_suplementos.universe, [0, 0, 1])
        self.uso_suplementos['SI'] = fuzz.trimf(self.uso_suplementos.universe, [0, 1, 1])
        
        # Training frequency
        self.frecuencia_entrenamiento['NUNCA'] = fuzz.trimf(self.frecuencia_entrenamiento.universe, [0, 1, 1])
        self.frecuencia_entrenamiento['OCASIONAL'] = fuzz.trimf(self.frecuencia_entrenamiento.universe, [0, 2, 3])
        self.frecuencia_entrenamiento['MODERADO'] = fuzz.trimf(self.frecuencia_entrenamiento.universe, [2, 4, 5])
        self.frecuencia_entrenamiento['FRECUENTE'] = fuzz.trimf(self.frecuencia_entrenamiento.universe, [4, 6, 7])
        self.frecuencia_entrenamiento['DIARIO'] = fuzz.trimf(self.frecuencia_entrenamiento.universe, [6, 7, 7])
        
        # Running experience
        self.tiempo_corriendo['PRINCIPIANTE'] = fuzz.trimf(self.tiempo_corriendo.universe, [0, 0, 90])
        self.tiempo_corriendo['INTERMEDIO'] = fuzz.trimf(self.tiempo_corriendo.universe, [60, 180, 365])
        self.tiempo_corriendo['EXPERTO'] = fuzz.trimf(self.tiempo_corriendo.universe, [300, 365, 999])
        
        # Time without running
        self.tiempo_sin_correr['ACTIVO'] = fuzz.trimf(self.tiempo_sin_correr.universe, [0, 0, 30])
        self.tiempo_sin_correr['INACTIVO_RECIENTE'] = fuzz.trimf(self.tiempo_sin_correr.universe, [20, 90, 180])
        self.tiempo_sin_correr['INACTIVO_PROLONGADO'] = fuzz.trimf(self.tiempo_sin_correr.universe, [150, 365, 99])
        
        # Running goal output
        self.meta_a_correr['CAMINAR'] = fuzz.trimf(self.meta_a_correr.universe, [0, 0, 1])
        self.meta_a_correr['CORRER_1KM'] = fuzz.trimf(self.meta_a_correr.universe, [0.5, 1, 1.5])
        self.meta_a_correr['CORRER_5KM'] = fuzz.trimf(self.meta_a_correr.universe, [1.5, 2, 2.5])
        self.meta_a_correr['CORRER_10KM'] = fuzz.trimf(self.meta_a_correr.universe, [2.5, 3, 3.5])
        self.meta_a_correr['MEDIA_MARATON'] = fuzz.trimf(self.meta_a_correr.universe, [3.5, 4, 4.5])
        self.meta_a_correr['MARATON'] = fuzz.trimf(self.meta_a_correr.universe, [4.5, 5, 5.5])
    
    def setup_rules(self):
        self.rules = [
            # Physical condition rules
            ctrl.Rule(self.condicion_fisica['EXCELENTE'] & self.edad['JOVEN_ADULTO'] & 
                     self.historia_lesiones['NINGUNA'], self.meta_a_correr['MARATON']),
            ctrl.Rule(self.condicion_fisica['BUENA'] & self.edad['ADULTO'] & 
                     self.historia_lesiones['LEVE'], self.meta_a_correr['CORRER_10KM']),
            ctrl.Rule(self.condicion_fisica['REGULAR'] & self.edad['ADOLESCENTE'], 
                     self.meta_a_correr['CORRER_5KM']),
            ctrl.Rule(self.condicion_fisica['MALA'] | self.edad['MAYOR'], 
                     self.meta_a_correr['CAMINAR']),
            ctrl.Rule(self.condicion_fisica['MUY_MALA'], self.meta_a_correr['CAMINAR']),
            ctrl.Rule(self.peso['OBESO'] & self.condicion_fisica['MALA'], 
                     self.meta_a_correr['CAMINAR']),
            ctrl.Rule(self.peso['SOBREPESO'] & self.nutricion['BUENA'], 
                     self.meta_a_correr['CORRER_1KM']),
            ctrl.Rule(self.peso['NORMAL'] & self.nutricion['BUENA'], 
                     self.meta_a_correr['CORRER_5KM']),
            ctrl.Rule(self.peso['LIVIANO'] & self.nutricion['BUENA'], 
                     self.meta_a_correr['CORRER_10KM']),
            
            # Training experience rules
            ctrl.Rule(self.frecuencia_entrenamiento['DIARIO'] & 
                     self.tiempo_corriendo['EXPERTO'], self.meta_a_correr['MARATON']),
            ctrl.Rule(self.frecuencia_entrenamiento['FRECUENTE'] & 
                     self.tiempo_corriendo['INTERMEDIO'], self.meta_a_correr['MEDIA_MARATON']),
            ctrl.Rule(self.frecuencia_entrenamiento['MODERADO'] & 
                     self.tiempo_corriendo['PRINCIPIANTE'], self.meta_a_correr['CORRER_5KM']),
            ctrl.Rule(self.frecuencia_entrenamiento['OCASIONAL'] | 
                     self.tiempo_sin_correr['INACTIVO_PROLONGADO'], self.meta_a_correr['CAMINAR']),
            
            # Lifestyle rules
            ctrl.Rule(self.horas_sueno['ADECUADO'] & self.consumo_agua['ALTO'], 
                     self.meta_a_correr['CORRER_5KM']),
            ctrl.Rule(self.horas_sueno['INSUFICIENTE'] | self.consumo_agua['BAJO'], 
                     self.meta_a_correr['CORRER_1KM']),
            ctrl.Rule(self.uso_suplementos['SI'] & self.nutricion['BUENA'], 
                     self.meta_a_correr['CORRER_10KM']),
            
            # Injury rules
            ctrl.Rule(self.historia_lesiones['GRAVE'], self.meta_a_correr['CAMINAR']),
            ctrl.Rule(self.historia_lesiones['MODERADA'] & self.edad['ADULTO'], 
                     self.meta_a_correr['CORRER_1KM']),
            
            # Gender-specific rules
            ctrl.Rule(self.genero['MUJER'] & self.edad['JOVEN_ADULTO'] & 
                     self.condicion_fisica['BUENA'], self.meta_a_correr['CORRER_10KM']),
            ctrl.Rule(self.genero['HOMBRE'] & self.edad['JOVEN_ADULTO'] & 
                     self.condicion_fisica['BUENA'], self.meta_a_correr['MEDIA_MARATON']),
            
            # New advanced rules
            ctrl.Rule(self.tiempo_corriendo['EXPERTO'] & 
                     self.frecuencia_entrenamiento['FRECUENTE'] & 
                     self.historia_lesiones['NINGUNA'], self.meta_a_correr['MARATON']),
            ctrl.Rule(self.edad['MAYOR'] & self.condicion_fisica['REGULAR'], 
                     self.meta_a_correr['CORRER_1KM']),
            ctrl.Rule(self.nutricion['MALA'] | self.horas_sueno['INSUFICIENTE'], 
                     self.meta_a_correr['CAMINAR']),
            ctrl.Rule(self.peso['NORMAL'] & self.condicion_fisica['BUENA'] & 
                     self.frecuencia_entrenamiento['MODERADO'], self.meta_a_correr['CORRER_10KM'])
        ]
    
    def random_gender(self):
        return random.choice([0, 1])  # 0 = female, 1 = male
    
    def random_age(self):
        return random.randint(self.MIN_AGE, self.MAX_AGE)
    
    def random_weight(self):
        return random.uniform(self.MIN_WEIGHT, self.MAX_WEIGHT)
    
    def random_fitness(self):
        return random.randint(self.MIN_FITNESS, self.MAX_FITNESS)
    
    def random_injury_history(self):
        # Most people will have low injury scores (0-3)
        return min(10, random.randint(0, 3) + random.randint(0, 3))
    
    def random_nutrition(self):
        # Slightly skewed toward better nutrition (4-8)
        return max(1, min(10, 5 + random.randint(-1, 5)))
    
    def random_sleep_hours(self):
        # Normally distributed around 7 hours
        return max(4, min(10, int(random.gauss(7, 1.5))))
    
    def random_water_intake(self):
        return random.uniform(1.0, 5.0)  # 1-5 liters
    
    def random_supplement_use(self):
        return 1 if random.random() < 0.3 else 0  # 30% use supplements
    
    def random_training_freq(self):
        # Most people train 2-5 days/week
        return max(1, min(7, 3 + random.randint(0, 2)))
    
    def random_running_experience(self):
        # Exponential distribution - more beginners than experts
        return min(999, int(random.expovariate(1/50)))
    
    def random_inactivity_period(self):
        # Most runners are either active or recently inactive
        return random.randint(0, 30) if random.random() < 0.7 else 30 + random.randint(0, 70)
    
    def generate_random_profile(self):
        self.running_sim.input['GENERO'] = self.random_gender()
        self.running_sim.input['EDAD'] = self.random_age()
        self.running_sim.input['PESO'] = self.random_weight()
        self.running_sim.input['CONDICION_FISICA'] = self.random_fitness()
        self.running_sim.input['HISTORIA_LESIONES'] = self.random_injury_history()
        self.running_sim.input['NUTRICION'] = self.random_nutrition()
        self.running_sim.input['HORAS_SUENO'] = self.random_sleep_hours()
        self.running_sim.input['CONSUMO_AGUA'] = self.random_water_intake()
        self.running_sim.input['USO_SUPLEMENTOS'] = self.random_supplement_use()
        self.running_sim.input['FRECUENCIA_ENTRENAMIENTO'] = self.random_training_freq()
        self.running_sim.input['TIEMPO_CORRIENDO'] = self.random_running_experience()
        self.running_sim.input['TIEMPO_SIN_CORRER'] = self.random_inactivity_period()
    
    def evaluate(self):
        self.running_sim.compute()
        return self.running_sim.output['META_A_CORRER']
    
    def display_results(self, goal_value):
        print("\n=== RUNNER PROFILE ===")
        print(f"Gender: {'Female' if self.running_sim.input['GENERO'] == 0 else 'Male'}")
        print(f"Age: {self.running_sim.input['EDAD']} years")
        print(f"Weight: {self.running_sim.input['PESO']:.1f} kg")
        print(f"Fitness Level: {self.running_sim.input['CONDICION_FISICA']}/10")
        print(f"Injury History: {self.running_sim.input['HISTORIA_LESIONES']}/10")
        print(f"Nutrition: {self.running_sim.input['NUTRICION']}/10")
        print(f"Sleep: {self.running_sim.input['HORAS_SUENO']} hours/night")
        print(f"Water Intake: {self.running_sim.input['CONSUMO_AGUA']:.1f} liters/day")
        print(f"Supplements: {'Yes' if self.running_sim.input['USO_SUPLEMENTOS'] == 1 else 'No'}")
        print(f"Training Frequency: {self.running_sim.input['FRECUENCIA_ENTRENAMIENTO']} days/week")
        print(f"Running Experience: {self.running_sim.input['TIEMPO_CORRIENDO']} days")
        print(f"Time Since Last Run: {self.running_sim.input['TIEMPO_SIN_CORRER']} days")

        print(f"\nRecommended Running Goal Score: {goal_value:.2f}")
        self.print_detailed_goal_description(goal_value)
    
    def print_detailed_goal_description(self, goal_value):
        print("\n=== RECOMMENDED TRAINING PLAN ===")
        
        if goal_value < 0.5:
            self.print_walking_plan()
        elif goal_value < 1.5:
            self.print_1km_plan()
        elif goal_value < 2.5:
            self.print_5km_plan()
        elif goal_value < 3.5:
            self.print_10km_plan()
        elif goal_value < 4.5:
            self.print_half_marathon_plan()
        else:
            self.print_marathon_plan()
        
        self.print_general_advice()
    
    def print_walking_plan(self):
        print("Level: Walking Program (Beginner)")
        print("Description: Start with 20-30 minutes of walking, 3-5 days per week")
        print("Weekly Schedule:")
        print(" - Day 1: 20 min walk at comfortable pace")
        print(" - Day 3: 20 min walk with 1-2 hills")
        print(" - Day 5: 25 min walk at steady pace")
        print("Focus: Build basic mobility and endurance")
        print("Duration: 4-8 weeks before progressing to walk-run intervals")

    def print_1km_plan(self):
        print("Level: 1km Running Goal")
        print("Description: Walk-run intervals (1 min run/2 min walk)")
        print("Weekly Schedule:")
        print(" - Session 1: 8x (1 min run/2 min walk)")
        print(" - Session 2: 10x (1 min run/2 min walk)")
        print(" - Session 3: 6x (1.5 min run/1.5 min walk)")
        print("Progression: Gradually increase running intervals by 30 sec/week")
        print("Goal: Continuous 1km run within 4-6 weeks")

    def print_5km_plan(self):
        print("Level: 5km Running Goal")
        print("Description: 3-4 runs per week including:")
        print("Weekly Schedule:")
        print(" - Day 1: Easy run (2-3km at conversational pace)")
        print(" - Day 3: Interval training (6x400m with 2 min walk)")
        print(" - Day 5: Long run (gradually building to 5km)")
        print(" - Optional: Day 7: Recovery run/walk (20-30 min)")
        print("Progression: Increase long run by 0.5km/week")
        print("Goal: Comfortable 5km run within 8-10 weeks")

    def print_10km_plan(self):
        print("Level: 10km Running Goal")
        print("Description: 4-5 runs per week including:")
        print("Weekly Schedule:")
        print(" - Day 1: Base run (5km at easy pace)")
        print(" - Day 2: Speed work (8x200m at 5km pace)")
        print(" - Day 4: Tempo run (20-30 mins at comfortable hard pace)")
        print(" - Day 6: Long run (gradually building to 10-12km)")
        print(" - Optional: Day 3: Recovery run (3-4km easy)")
        print("Training period: 10-12 weeks")

    def print_half_marathon_plan(self):
        print("Level: Half Marathon (21km)")
        print("Description: 5-6 runs per week including:")
        print("Weekly Schedule:")
        print(" - Day 1: Easy run (6-8km)")
        print(" - Day 2: Speed work (5x1km at 10km pace)")
        print(" - Day 3: Recovery run (5km easy)")
        print(" - Day 5: Tempo run (40-50 mins at half marathon pace)")
        print(" - Day 7: Long run (gradually building to 18-20km)")
        print(" - Optional: Day 4: Hill repeats or cross-training)")
        print("Training period: 12-16 weeks")

    def print_marathon_plan(self):
        print("Level: Full Marathon (42km)")
        print("Description: Advanced training program including:")
        print("Weekly Schedule:")
        print(" - Monday: Easy run (8-10km)")
        print(" - Tuesday: Interval training (e.g., 6x1km at 10s faster than marathon pace)")
        print(" - Wednesday: Recovery run (5-8km easy) or cross-training")
        print(" - Thursday: Tempo run (10-12km at marathon pace)")
        print(" - Friday: Rest or easy 5km")
        print(" - Saturday: Long run (gradually building to 32-35km)")
        print(" - Sunday: Recovery run (5-8km easy)")
        print("Training period: 16-20 weeks")
        print("Peak Weekly Mileage: 80-100km")

    def print_general_advice(self):
        print("\n=== GENERAL RECOMMENDATIONS ===")
        print("1. Always warm up for 10-15 minutes before running")
        print("2. Include strength training 2-3 times per week")
        print("3. Allow for proper recovery between hard sessions")
        print("4. Stay hydrated and maintain proper nutrition")
        print("5. Listen to your body and adjust as needed")
        print("\nNote: Always consult with a healthcare professional before starting a new exercise program.")

    def run(self):
        try:
            self.generate_random_profile()
            goal_value = self.evaluate()
            self.display_results(goal_value)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    recommender = RunningGoalRecommender()
    recommender.run()