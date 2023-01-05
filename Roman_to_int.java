
import java.util.HashMap;

public class Roman_to_int {
    public static int romanToInt(String s) {
        HashMap<String, Integer> roman = new HashMap<String, Integer>();
        roman.put("I",1);
        roman.put("II",2);
        roman.put("I",3);
        roman.put("V",5);
        roman.put("X",10);
        roman.put("L",50);
        roman.put("C",100);
        roman.put("D",500);
        roman.put("M",1000);
        roman.put("CM",900);
        roman.put("CD",400);
        roman.put("XL",40);
        roman.put("XC",90);
        roman.put("IX",9);
        roman.put("IV",4);
        int total = 0;
        while(s.length() !=0){
            if (s.contains("CM")){
                total +=roman.get("CM");
                s=s.replace("CM", "");
            }
            if (s.contains("CD")){
                total +=roman.get("CD");
                s=s.replace("CD", "");
            }
            if (s.contains("XL")){
                total +=roman.get("XL");
                s=s.replace("XL", "");
            }
            if (s.contains("XC")){
                total +=roman.get("XC");
                s=s.replace("XC", "");
            }
            if (s.contains("IX")){
                total +=roman.get("IX");
                s=s.replace("IX", "");
            }
            if (s.contains("IV")){
                total +=roman.get("IV");
                s=s.replace("IV", "");
            }
            if (s.contains("III")){
                total +=roman.get("IV");
                s=s.replace("III", "");
            }
            if (s.contains("II")){
                total +=roman.get("IV");
                s=s.replace("II", "");
            }
            if (s.contains("I")){
                total +=roman.get("IV");
                s=s.replace("I", "");
            }
            while(s.length() !=0){
                char x =(s.charAt(0));
                String y =String.valueOf(x);
                total+=roman.get(y);
                s= s.replace(y, "");
            }

        }//end while
        return total;
    }//end method
    public static void main(String[] args) {
            String s = "III";
           // String s2 ="LVIII";
           // String s3 = "MCMXCIV";
            System.out.println(romanToInt(s));
    }
}

