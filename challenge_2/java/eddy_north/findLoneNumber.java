import java.util.Arrays;
import java.util.HashMap;
import java.util.Random;

public class findLoneNumber {

	public static void main(String[] args) {
		String[] sourceArray = generateRandomisedArray(26,true);
		String answer = findLoneNumber(sourceArray);
		System.out.println(answer);
	}
	
	public static String[] generateRandomisedArray(int elements,boolean useCharacters) {
		boolean charactersIncluded = useCharacters;
		int n = elements;
		if (n % 2 == 0) {
			n = n+1;
		}
		String loneString = "";
		String[] objectArray = new String[n];
		boolean singleValueAdded = false;
		for (int i = 0; i < n; i++) {
			String includeThisValue = "" + (int)Math.floor((Math.random()*n));
			while (includeThisValue.equals(loneString)){
				includeThisValue = "" + (int)Math.floor((Math.random()*n));
			}
			if (charactersIncluded) {
				//if problem using characters, introduce 50% chance to overwrite int with char.
				if (Math.random() < 0.5) {
					Random r = new Random();
					char c = (char)(r.nextInt(26) + 'a');
					includeThisValue =  "" + c;
				}
				while (includeThisValue.equals(loneString)){
					if (Math.random() < 0.5) {
						Random r = new Random();
						char c = (char)(r.nextInt(26) + 'a');
						includeThisValue =  "" + c;
					}
				}
			}
			if (singleValueAdded) {
				objectArray[i] = includeThisValue;
				if (i < n-1) {
					i = i+1;
					objectArray[i] = includeThisValue;
				}
			} else {
				loneString = includeThisValue;
				objectArray[i] = includeThisValue;
				singleValueAdded = true;
			}		
		}
		Arrays.sort(objectArray);
		
		System.out.println("Test Array has been generated with " + n + " elements.");
		StringBuffer tempString = new StringBuffer();
		for (int i = 0; i < n; i++) {
			tempString.append(objectArray[i] + " ");
		}
		System.out.println("Test Array contains: " + tempString);
		return objectArray;
	}
	
	public static String findLoneNumber(String[] sourceArray) {
		String loneNumber = "";
		HashMap<String,Integer> countElements = new HashMap<>(); 
		
		for (int i = 0; i < sourceArray.length; i++) {
			if (!countElements.containsKey(sourceArray[i])) {
				countElements.put(sourceArray[i], 1);
			} else {
				int newValue = countElements.get(sourceArray[i]) + 1;
				countElements.put(sourceArray[i], newValue);
			}
		}
		//Following is O(n^2) solution, O(n) solution not finished yet :(
		for (int i = 0; i < countElements.size(); i++){
			for (String entryKey : countElements.keySet()) {
				if (countElements.get(entryKey).equals(1)){
					loneNumber = entryKey;
				}
			}
		}
		return loneNumber;
	}
	
} //End of solution class
