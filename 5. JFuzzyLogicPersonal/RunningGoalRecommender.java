import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;

public class RunningGoalRecommender {

    // Constants for input ranges
    private static final int MIN_AGE = 18;
    private static final int MAX_AGE = 70;
    private static final double MIN_WEIGHT = 40.0;
    private static final double MAX_WEIGHT = 120.0;
    private static final int MIN_FITNESS = 1;
    private static final int MAX_FITNESS = 10;
    
    public static void main(String[] args) {
        try {
            // Load FIS from embedded FCL string
            FIS fis = FIS.createFromString(createFclString(), true);
            
            if (fis == null) {
                System.err.println("Error loading FCL rules");
                return;
            }

            FunctionBlock fb = fis.getFunctionBlock("Corredores");
            
            // Generate realistic random values within defined ranges
            fb.setVariable("GENERO", randomGender());                          // 0 = female, 1 = male
            fb.setVariable("EDAD", randomAge());                              // 18-70 years
            fb.setVariable("PESO", randomWeight());                          // 40-120 kg
            fb.setVariable("CONDICION_FISICA", randomFitness());              // 1-10
            fb.setVariable("HISTORIA_LESIONES", randomInjuryHistory());       // 0-10
            fb.setVariable("NUTRICION", randomNutrition());                   // 1-10
            fb.setVariable("HORAS_SUENO", randomSleepHours());                // 4-10 hours
            fb.setVariable("CONSUMO_AGUA", randomWaterIntake());              // 1.0-5.0 liters/day
            fb.setVariable("USO_SUPLEMENTOS", randomSupplementUse());         // 0=no, 1=yes
            fb.setVariable("FRECUENCIA_ENTRENAMIENTO", randomTrainingFreq()); // 1-7 days/week
            fb.setVariable("TIEMPO_CORRIENDO", randomRunningExperience());    // 0-999 days
            fb.setVariable("TIEMPO_SIN_CORRER", randomInactivityPeriod());   // 0-99 days

            // Evaluate the fuzzy rules
            fb.evaluate();

            // Get and display results
            Variable meta = fb.getVariable("META_A_CORRER");
            displayResults(fb, meta);
            
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    // Helper methods for generating realistic random inputs
    private static int randomGender() {
        return Math.random() < 0.5 ? 0 : 1;  // 50/50 distribution
    }
    
    private static double randomAge() {
        return MIN_AGE + Math.floor(Math.random() * (MAX_AGE - MIN_AGE + 1));
    }
    
    private static double randomWeight() {
        return MIN_WEIGHT + Math.floor(Math.random() * (MAX_WEIGHT - MIN_WEIGHT + 1));
    }
    
    private static double randomFitness() {
        return MIN_FITNESS + Math.floor(Math.random() * (MAX_FITNESS - MIN_FITNESS + 1));
    }
    
    private static double randomInjuryHistory() {
        // Most people will have low injury scores (0-3)
        return Math.min(10, Math.floor(Math.random() * 4 + Math.random() * 4));
    }
    
    private static double randomNutrition() {
        // Slightly skewed toward better nutrition (4-8)
        return Math.max(1, Math.min(10, 5 + (Math.random() * 6 - 1)));
    }
    
    private static double randomSleepHours() {
        // Normally distributed around 7 hours
        return Math.max(4, Math.min(10, 7 + (Math.random() * 4 - 2)));
    }
    
    private static double randomWaterIntake() {
        return 1 + Math.floor(Math.random() * 5);  // 1-5 liters
    }
    
    private static double randomSupplementUse() {
        return Math.random() < 0.3 ? 1 : 0;  // 30% use supplements
    }
    
    private static double randomTrainingFreq() {
        // Most people train 2-5 days/week
        return Math.max(1, Math.min(7, 3 + Math.floor(Math.random() * 3)));
    }
    
    private static double randomRunningExperience() {
        // Exponential distribution - more beginners than experts
        return Math.min(999, Math.floor(Math.pow(Math.random() * 20, 2)));
    }
    
    private static double randomInactivityPeriod() {
        // Most runners are either active or recently inactive
        return Math.random() < 0.7 ? Math.floor(Math.random() * 30) : 
                                    30 + Math.floor(Math.random() * 70);
    }

    private static void displayResults(FunctionBlock fb, Variable goal) {
        // Display all input values
        System.out.println("\n=== RUNNER PROFILE ===");
        System.out.printf("Gender: %s%n", fb.getVariable("GENERO").getValue() == 0 ? "Female" : "Male");
        System.out.printf("Age: %.0f years%n", fb.getVariable("EDAD").getValue());
        System.out.printf("Weight: %.0f kg%n", fb.getVariable("PESO").getValue());
        System.out.printf("Fitness Level: %.0f/10%n", fb.getVariable("CONDICION_FISICA").getValue());
        System.out.printf("Injury History: %.0f/10%n", fb.getVariable("HISTORIA_LESIONES").getValue());
        System.out.printf("Nutrition: %.0f/10%n", fb.getVariable("NUTRICION").getValue());
        System.out.printf("Sleep: %.0f hours/night%n", fb.getVariable("HORAS_SUENO").getValue());
        System.out.printf("Water Intake: %.1f liters/day%n", fb.getVariable("CONSUMO_AGUA").getValue());
        System.out.printf("Supplements: %s%n", fb.getVariable("USO_SUPLEMENTOS").getValue() == 1 ? "Yes" : "No");
        System.out.printf("Training Frequency: %.0f days/week%n", fb.getVariable("FRECUENCIA_ENTRENAMIENTO").getValue());
        System.out.printf("Running Experience: %.0f days%n", fb.getVariable("TIEMPO_CORRIENDO").getValue());
        System.out.printf("Time Since Last Run: %.0f days%n", fb.getVariable("TIEMPO_SIN_CORRER").getValue());

        // Display fuzzy output chart
        JFuzzyChart.get().chart(goal, goal.getDefuzzifier(), true);
        
        // Display recommendation
        System.out.printf("\nRecommended Running Goal Score: %.2f%n", goal.getValue());
        printDetailedGoalDescription(goal.getValue());
    }

    private static void printDetailedGoalDescription(double goalValue) {
        System.out.println("\n=== RECOMMENDED TRAINING PLAN ===");
        
        if (goalValue < 0.5) {
            printWalkingPlan();
        } else if (goalValue < 1.5) {
            print1KmPlan();
        } else if (goalValue < 2.5) {
            print5KmPlan();
        } else if (goalValue < 3.5) {
            print10KmPlan();
        } else if (goalValue < 4.5) {
            printHalfMarathonPlan();
        } else {
            printMarathonPlan();
        }
        
        printGeneralAdvice();
    }

    private static void printWalkingPlan() {
        System.out.println("Level: Walking Program (Beginner)");
        System.out.println("Description: Start with 20-30 minutes of walking, 3-5 days per week");
        System.out.println("Weekly Schedule:");
        System.out.println(" - Day 1: 20 min walk at comfortable pace");
        System.out.println(" - Day 3: 20 min walk with 1-2 hills");
        System.out.println(" - Day 5: 25 min walk at steady pace");
        System.out.println("Focus: Build basic mobility and endurance");
        System.out.println("Duration: 4-8 weeks before progressing to walk-run intervals");
    }

    private static void print1KmPlan() {
        System.out.println("Level: 1km Running Goal");
        System.out.println("Description: Walk-run intervals (1 min run/2 min walk)");
        System.out.println("Weekly Schedule:");
        System.out.println(" - Session 1: 8x (1 min run/2 min walk)");
        System.out.println(" - Session 2: 10x (1 min run/2 min walk)");
        System.out.println(" - Session 3: 6x (1.5 min run/1.5 min walk)");
        System.out.println("Progression: Gradually increase running intervals by 30 sec/week");
        System.out.println("Goal: Continuous 1km run within 4-6 weeks");
    }

    private static void print5KmPlan() {
        System.out.println("Level: 5km Running Goal");
        System.out.println("Description: 3-4 runs per week including:");
        System.out.println("Weekly Schedule:");
        System.out.println(" - Day 1: Easy run (2-3km at conversational pace)");
        System.out.println(" - Day 3: Interval training (6x400m with 2 min walk)");
        System.out.println(" - Day 5: Long run (gradually building to 5km)");
        System.out.println(" - Optional: Day 7: Recovery run/walk (20-30 min)");
        System.out.println("Progression: Increase long run by 0.5km/week");
        System.out.println("Goal: Comfortable 5km run within 8-10 weeks");
    }

    private static void print10KmPlan() {
        System.out.println("Level: 10km Running Goal");
        System.out.println("Description: 4-5 runs per week including:");
        System.out.println("Weekly Schedule:");
        System.out.println(" - Day 1: Base run (5km at easy pace)");
        System.out.println(" - Day 2: Speed work (8x200m at 5km pace)");
        System.out.println(" - Day 4: Tempo run (20-30 mins at comfortable hard pace)");
        System.out.println(" - Day 6: Long run (gradually building to 10-12km)");
        System.out.println(" - Optional: Day 3: Recovery run (3-4km easy)");
        System.out.println("Training period: 10-12 weeks");
    }

    private static void printHalfMarathonPlan() {
        System.out.println("Level: Half Marathon (21km)");
        System.out.println("Description: 5-6 runs per week including:");
        System.out.println("Weekly Schedule:");
        System.out.println(" - Day 1: Easy run (6-8km)");
        System.out.println(" - Day 2: Speed work (5x1km at 10km pace)");
        System.out.println(" - Day 3: Recovery run (5km easy)");
        System.out.println(" - Day 5: Tempo run (40-50 mins at half marathon pace)");
        System.out.println(" - Day 7: Long run (gradually building to 18-20km)");
        System.out.println(" - Optional: Day 4: Hill repeats or cross-training");
        System.out.println("Training period: 12-16 weeks");
    }

    private static void printMarathonPlan() {
        System.out.println("Level: Full Marathon (42km)");
        System.out.println("Description: Advanced training program including:");
        System.out.println("Weekly Schedule:");
        System.out.println(" - Monday: Easy run (8-10km)");
        System.out.println(" - Tuesday: Interval training (e.g., 6x1km at 10s faster than marathon pace)");
        System.out.println(" - Wednesday: Recovery run (5-8km easy) or cross-training");
        System.out.println(" - Thursday: Tempo run (10-12km at marathon pace)");
        System.out.println(" - Friday: Rest or easy 5km");
        System.out.println(" - Saturday: Long run (gradually building to 32-35km)");
        System.out.println(" - Sunday: Recovery run (5-8km easy)");
        System.out.println("Training period: 16-20 weeks");
        System.out.println("Peak Weekly Mileage: 80-100km");
    }

    private static void printGeneralAdvice() {
        System.out.println("\n=== GENERAL RECOMMENDATIONS ===");
        System.out.println("1. Always warm up for 10-15 minutes before running");
        System.out.println("2. Include strength training 2-3 times per week");
        System.out.println("3. Allow for proper recovery between hard sessions");
        System.out.println("4. Stay hydrated and maintain proper nutrition");
        System.out.println("5. Listen to your body and adjust as needed");
        System.out.println("\nNote: Always consult with a healthcare professional before starting a new exercise program.");
    }

    private static String createFclString() {
        return "FUNCTION_BLOCK Corredores\n\n" +
        
               "VAR_INPUT\n" +
               "    GENERO : REAL;\n" +
               "    EDAD : REAL;\n" +
               "    PESO : REAL;\n" +
               "    CONDICION_FISICA : REAL;\n" +
               "    HISTORIA_LESIONES : REAL;\n" +
               "    NUTRICION : REAL;\n" +
               "    HORAS_SUENO : REAL;\n" +
               "    CONSUMO_AGUA : REAL;\n" +
               "    USO_SUPLEMENTOS : REAL;\n" +
               "    FRECUENCIA_ENTRENAMIENTO : REAL;\n" +
               "    TIEMPO_CORRIENDO : REAL;\n" +
               "    TIEMPO_SIN_CORRER : REAL;\n" +
               "END_VAR\n\n" +
        
               "VAR_OUTPUT\n" +
               "    META_A_CORRER : REAL;\n" +
               "END_VAR\n\n" +
        
               "FUZZIFY GENERO\n" +
               "    TERM MUJER := 0;\n" +
               "    TERM HOMBRE := 1;\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY EDAD\n" +
               "    TERM NINO := (5,1) (12,0);\n" +
               "    TERM ADOLESCENTE := (10,0) (18,1) (25,0);\n" +
               "    TERM JOVEN_ADULTO := (20,0) (30,1) (40,0);\n" +
               "    TERM ADULTO := (35,0) (50,1) (60,0);\n" +
               "    TERM MAYOR := (55,0) (70,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY PESO\n" +
               "    TERM MUY_LIVIANO := (20,1) (35,0);\n" +
               "    TERM LIVIANO := (30,0) (50,1) (60,0);\n" +
               "    TERM NORMAL := (50,0) (70,1) (85,0);\n" +
               "    TERM SOBREPESO := (75,0) (95,1) (110,0);\n" +
               "    TERM OBESO := (100,0) (120,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY CONDICION_FISICA\n" +
               "    TERM MUY_MALA := (1,1) (2,0);\n" +
               "    TERM MALA := (1,0) (3,1) (5,0);\n" +
               "    TERM REGULAR := (4,0) (6,1) (7,0);\n" +
               "    TERM BUENA := (6,0) (8,1) (9,0);\n" +
               "    TERM EXCELENTE := (8,0) (10,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY HISTORIA_LESIONES\n" +
               "    TERM NINGUNA := (0,1) (2,0);\n" +
               "    TERM LEVE := (1,0) (4,1) (6,0);\n" +
               "    TERM MODERADA := (5,0) (7,1) (9,0);\n" +
               "    TERM GRAVE := (8,0) (10,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY NUTRICION\n" +
               "    TERM MALA := (1,1) (3,0);\n" +
               "    TERM REGULAR := (2,0) (5,1) (7,0);\n" +
               "    TERM BUENA := (6,0) (8,1) (10,0);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY HORAS_SUENO\n" +
               "    TERM INSUFICIENTE := (0,1) (5,0);\n" +
               "    TERM MINIMO := (4,0) (6,1) (7,0);\n" +
               "    TERM ADECUADO := (6,0) (8,1) (9,0);\n" +
               "    TERM EXCESIVO := (8,0) (10,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY CONSUMO_AGUA\n" +
               "    TERM BAJO := (1,1) (2,0);\n" +
               "    TERM MODERADO := (1,0) (3,1) (4,0);\n" + 
               "    TERM ALTO := (3,0) (5,1);\n" +           
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY USO_SUPLEMENTOS\n" +
               "    TERM NO := 0;\n" +
               "    TERM SI := 1;\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY FRECUENCIA_ENTRENAMIENTO\n" +
               "    TERM NUNCA := (0,1) (1,0);\n" +
               "    TERM OCASIONAL := (0,0) (2,1) (3,0);\n" +
               "    TERM MODERADO := (2,0) (4,1) (5,0);\n" +
               "    TERM FRECUENTE := (4,0) (6,1) (7,0);\n" +
               "    TERM DIARIO := (6,0) (7,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY TIEMPO_CORRIENDO\n" +
               "    TERM PRINCIPIANTE := (0,1) (90,0);\n" +
               "    TERM INTERMEDIO := (60,0) (180,1) (365,0);\n" +
               "    TERM EXPERTO := (300,0) (365,1);\n" +
               "END_FUZZIFY\n\n" +
    
               "FUZZIFY TIEMPO_SIN_CORRER\n" +
               "    TERM ACTIVO := (0,1) (30,0);\n" +
               "    TERM INACTIVO_RECIENTE := (20,0) (90,1) (180,0);\n" +
               "    TERM INACTIVO_PROLONGADO := (150,0) (365,1);\n" +
               "END_FUZZIFY\n\n" +
        
               "DEFUZZIFY META_A_CORRER\n" +
               "    TERM CAMINAR := TRIAN 0 0 1;\n" +
               "    TERM CORRER_1KM := TRIAN 0.5 1 1.5;\n" +
               "    TERM CORRER_5KM := TRIAN 1.5 2 2.5;\n" +
               "    TERM CORRER_10KM := TRIAN 2.5 3 3.5;\n" +
               "    TERM MEDIA_MARATON := TRIAN 3.5 4 4.5;\n" +
               "    TERM MARATON := TRIAN 4.5 5 5.5;\n" +
               "    METHOD : COG;\n" +
               "    DEFAULT := 0;\n" +
               "END_DEFUZZIFY\n\n" +
        
               "RULEBLOCK RunningGoals\n" +
               "    AND : MIN;\n" +
               "    OR : MAX;\n" +
               "    ACT : MIN;\n" +
               "    ACCU : MAX;\n\n" +

               "    // Physical condition rules\n" +
               "    RULE 1: IF CONDICION_FISICA IS EXCELENTE AND EDAD IS JOVEN_ADULTO AND HISTORIA_LESIONES IS NINGUNA THEN META_A_CORRER IS MARATON;\n" +
               "    RULE 2: IF CONDICION_FISICA IS BUENA AND EDAD IS ADULTO AND HISTORIA_LESIONES IS LEVE THEN META_A_CORRER IS CORRER_10KM;\n" +
               "    RULE 3: IF CONDICION_FISICA IS REGULAR AND EDAD IS ADOLESCENTE THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 4: IF CONDICION_FISICA IS MALA OR EDAD IS MAYOR THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 5: IF CONDICION_FISICA IS MUY_MALA THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 6: IF PESO IS OBESO AND CONDICION_FISICA IS MALA THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 7: IF PESO IS SOBREPESO AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_1KM;\n" +
               "    RULE 8: IF PESO IS NORMAL AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 9: IF PESO IS LIVIANO AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_10KM;\n" +
        
               "    // Training experience rules\n" +
               "    RULE 10: IF FRECUENCIA_ENTRENAMIENTO IS DIARIO AND TIEMPO_CORRIENDO IS EXPERTO THEN META_A_CORRER IS MARATON;\n" +
               "    RULE 11: IF FRECUENCIA_ENTRENAMIENTO IS FRECUENTE AND TIEMPO_CORRIENDO IS INTERMEDIO THEN META_A_CORRER IS MEDIA_MARATON;\n" +
               "    RULE 12: IF FRECUENCIA_ENTRENAMIENTO IS MODERADO AND TIEMPO_CORRIENDO IS PRINCIPIANTE THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 13: IF FRECUENCIA_ENTRENAMIENTO IS OCASIONAL OR TIEMPO_SIN_CORRER IS INACTIVO_PROLONGADO THEN META_A_CORRER IS CAMINAR;\n" +
        
               "    // Lifestyle rules\n" +
               "    RULE 14: IF HORAS_SUENO IS ADECUADO AND CONSUMO_AGUA IS ALTO THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 15: IF HORAS_SUENO IS INSUFICIENTE OR CONSUMO_AGUA IS BAJO THEN META_A_CORRER IS CORRER_1KM;\n" +
               "    RULE 16: IF USO_SUPLEMENTOS IS SI AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_10KM;\n" +
        
               "    // Injury rules\n" +
               "    RULE 17: IF HISTORIA_LESIONES IS GRAVE THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 18: IF HISTORIA_LESIONES IS MODERADA AND EDAD IS ADULTO THEN META_A_CORRER IS CORRER_1KM;\n" +
        
               "    // Gender-specific rules\n" +
               "    RULE 19: IF GENERO IS MUJER AND EDAD IS JOVEN_ADULTO AND CONDICION_FISICA IS BUENA THEN META_A_CORRER IS CORRER_10KM;\n" +
               "    RULE 20: IF GENERO IS HOMBRE AND EDAD IS JOVEN_ADULTO AND CONDICION_FISICA IS BUENA THEN META_A_CORRER IS MEDIA_MARATON;\n" +
        
               "    // New advanced rules\n" +
               "    RULE 21: IF TIEMPO_CORRIENDO IS EXPERTO AND FRECUENCIA_ENTRENAMIENTO IS FRECUENTE AND HISTORIA_LESIONES IS NINGUNA THEN META_A_CORRER IS MARATON;\n" +
               "    RULE 22: IF EDAD IS MAYOR AND CONDICION_FISICA IS REGULAR THEN META_A_CORRER IS CORRER_1KM;\n" +
               "    RULE 23: IF NUTRICION IS MALA OR HORAS_SUENO IS INSUFICIENTE THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 24: IF PESO IS NORMAL AND CONDICION_FISICA IS BUENA AND FRECUENCIA_ENTRENAMIENTO IS MODERADO THEN META_A_CORRER IS CORRER_10KM;\n" +
               "END_RULEBLOCK\n\n" +
               "END_FUNCTION_BLOCK";
    }
}