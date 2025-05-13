import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;

public class RunningGoalRecommender {

    public static void main(String[] args) {
    try {
        // Load the FCL file (we'll create it programmatically)
        FIS fis = FIS.createFromString(createFclString(), true);
        
        // Rest of your existing code...
        if (fis == null) {
            System.err.println("Error loading FCL file");
            return;
        }

        // Get the function block
        FunctionBlock fb = fis.getFunctionBlock("Corredores");

        // Set inputs (example values)
        fb.setVariable("GENERO", 0);          // 0 = female, 1 = male
        fb.setVariable("EDAD", 28);           // years
        fb.setVariable("PESO", 68);          // kg
        fb.setVariable("CONDICION_FISICA", 7); // 1-10
        fb.setVariable("HISTORIA_LESIONES", 2); // 0-10
        fb.setVariable("NUTRICION", 8);       // 1-10
        fb.setVariable("HORAS_SUENO", 7);     // hours
        fb.setVariable("CONSUMO_AGUA", 3);  // liters/day
        fb.setVariable("USO_SUPLEMENTOS", 1); // 0=no, 1=yes
        fb.setVariable("FRECUENCIA_ENTRENAMIENTO", 5); // days/week
        fb.setVariable("TIEMPO_CORRIENDO", 200); // days
        fb.setVariable("TIEMPO_SIN_CORRER", 10); // days

        // Evaluate the system
        fb.evaluate();

        // Show output variable's chart
        Variable meta = fb.getVariable("META_A_CORRER");
        JFuzzyChart.get().chart(meta, meta.getDefuzzifier(), true);

        // Print output value
        System.out.println("Recommended running goal: " + meta.getValue());
        printGoalDescription(meta.getValue());
        
        
    } catch (Exception e) {
        System.err.println("Error: " + e.getMessage());
        e.printStackTrace();
    }
}
private static void printGoalDescription(double goalValue) {
        System.out.print("Goal description: ");
        if (goalValue < 0.5) {
            System.out.println("Walking program");
        } else if (goalValue < 1.5) {
            System.out.println("1km running goal");
        } else if (goalValue < 2.5) {
            System.out.println("5km running goal");
        } else if (goalValue < 3.5) {
            System.out.println("10km running goal");
        } else if (goalValue < 4.5) {
            System.out.println("Half marathon (21km) goal");
        } else {
            System.out.println("Full marathon (42km) goal");
        }
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
               "    TERM MODERADO := (1,0) (3,1) (4,0);\n" +  // Cambiado de 1.5 a 1
               "    TERM ALTO := (3,0) (5,1);\n" +            // Cambiado de 3.5 a 3
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
    
               "    RULE 1: IF CONDICION_FISICA IS EXCELENTE AND EDAD IS JOVEN_ADULTO AND HISTORIA_LESIONES IS NINGUNA THEN META_A_CORRER IS MARATON;\n" +
               "    RULE 2: IF CONDICION_FISICA IS BUENA AND EDAD IS ADULTO AND HISTORIA_LESIONES IS LEVE THEN META_A_CORRER IS CORRER_10KM;\n" +
               "    RULE 3: IF CONDICION_FISICA IS REGULAR AND EDAD IS ADOLESCENTE THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 4: IF CONDICION_FISICA IS MALA OR EDAD IS MAYOR THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 5: IF CONDICION_FISICA IS MUY_MALA THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 6: IF PESO IS OBESO AND CONDICION_FISICA IS MALA THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 7: IF PESO IS SOBREPESO AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_1KM;\n" +
               "    RULE 8: IF PESO IS NORMAL AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 9: IF PESO IS LIVIANO AND NUTRICION IS EXCELENTE THEN META_A_CORRER IS CORRER_10KM;\n" +
               "    RULE 10: IF FRECUENCIA_ENTRENAMIENTO IS DIARIO AND TIEMPO_CORRIENDO IS EXPERTO THEN META_A_CORRER IS MARATON;\n" +
               "    RULE 11: IF FRECUENCIA_ENTRENAMIENTO IS FRECUENTE AND TIEMPO_CORRIENDO IS INTERMEDIO THEN META_A_CORRER IS MEDIA_MARATON;\n" +
               "    RULE 12: IF FRECUENCIA_ENTRENAMIENTO IS MODERADO AND TIEMPO_CORRIENDO IS PRINCIPIANTE THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 13: IF FRECUENCIA_ENTRENAMIENTO IS OCASIONAL OR TIEMPO_SIN_CORRER IS INACTIVO_PROLONGADO THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 14: IF HORAS_SUENO IS ADECUADO AND CONSUMO_AGUA IS ALTO THEN META_A_CORRER IS CORRER_5KM;\n" +
               "    RULE 15: IF HORAS_SUENO IS INSUFICIENTE OR CONSUMO_AGUA IS BAJO THEN META_A_CORRER IS CORRER_1KM;\n" +
               "    RULE 16: IF USO_SUPLEMENTOS IS SI AND NUTRICION IS BUENA THEN META_A_CORRER IS CORRER_10KM;\n" +
               "    RULE 17: IF HISTORIA_LESIONES IS GRAVE THEN META_A_CORRER IS CAMINAR;\n" +
               "    RULE 18: IF HISTORIA_LESIONES IS MODERADA AND EDAD IS ADULTO THEN META_A_CORRER IS CORRER_1KM;\n" +
               "    RULE 19: IF GENERO IS MUJER AND EDAD IS JOVEN_ADULTO AND CONDICION_FISICA IS BUENA THEN META_A_CORRER IS CORRER_10KM;\n" +
               "    RULE 20: IF GENERO IS HOMBRE AND EDAD IS JOVEN_ADULTO AND CONDICION_FISICA IS BUENA THEN META_A_CORRER IS MEDIA_MARATON;\n" +
               "END_RULEBLOCK\n\n" +
               "END_FUNCTION_BLOCK";
    }
}