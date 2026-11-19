public class CaesarJava {
    static final double[] ENGLISH_FREQ = {
        8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094,
        6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929,
        0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
        1.974, 0.074
    };

    public static String caesar(String text, int shift){
        StringBuilder result = new StringBuilder();
        for (char ch : text.toCharArray()){
            if (Character.isLetter(ch)) {
                char base = Character.isUpperCase(ch) ? 'A' : 'a';
                int shiftedPos = Math.floorMod(ch - base + shift, 26);
                result.append((char) (base+shiftedPos));
            }
            else{
                result.append(ch);
            }
        }
        return result.toString();
    }

    public static void main(String[] args){
        String hasil = caesar("Makima", 3);
        System.out.println(hasil);
    }
}