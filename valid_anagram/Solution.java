class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> occurences = new HashMap<>();
        for (Character ch : s.toCharArray()) {
            if (!occurences.containsKey(ch)) {
                occurences.put(ch, 1);
            } else {
                Integer curVal = occurences.get(ch);
                occurences.put(ch, curVal + 1);
            }
        }

        for (Character ch : t.toCharArray()) {
            Integer count = occurences.get(ch);
            if (count == null) {
                return false;
            } else {
                occurences.put(ch, count - 1);
            }
        }
        for (Map.Entry<Character, Integer> ent: occurences.entrySet()) {
            if (ent.getValue() != 0) {
                return false;
            }
        }
        return true;
    }
}