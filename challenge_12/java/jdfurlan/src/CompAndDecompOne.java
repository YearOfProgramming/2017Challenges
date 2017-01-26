
import java.util.List;
import java.util.Arrays;

public class CompAndDecompOne {
	// the compression threshold used to reduce string size. If too low it can
	// actually increase the size of the string. Compression fails if threshold < 3 
	// since the sequence `aa` would end up larger at `a#2`
	private static final int THRESHOLD = 4;

	/**
	 * decompress walks through a compressed string and checks if it has found a
	 * '#' character, otherwise it just adds the character to the StringBuffer.
	 * If a '#' is found, it was determine the integer value following it, which
	 * could be 1->10 digits. Once the number is determined, that number - 1 of
	 * the last character will be added to the StringBuffer. The hardest part of
	 * this method was just checking for edge cases and indexOutOfBound errors.
	 * 
	 * @param s
	 *            the string to be decompressed
	 * @return decompressed version of s
	 */
	private static String decompress(String s) {
		StringBuffer decompressed = new StringBuffer();
		StringBuffer subString = new StringBuffer();
		char last = 0;
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == '#') {
				i++;
				int num = Character.getNumericValue(s.charAt(i));
				if (i != s.length() - 1 && Character.isDigit(s.charAt(i + 1))) {
					while (Character.isDigit(s.charAt(i)) && i < s.length() - 1) {
						num = num * 10 + Character.getNumericValue(s.charAt(i + 1));
						i++;
					}
				}
				for (int j = 1; j < num; j++) {
					decompressed.append(last);
				}
			} else {
				last = c;
				decompressed.append(last);

			}
		}

		return decompressed.toString();
	}

	/**
	 * compress walks through an uncompressed string and adds every character to
	 * a subString buffer until the character changes. Once we see a new
	 * character, if the size of our buffer is >= THRESHOLD, we must compress,
	 * else just append the buffer to our final compressedBuffer.
	 * 
	 * @param s
	 *            string to compress
	 * @return compressed version of s
	 */
	private static String compress(String s) {
		StringBuffer compressedBuffer = new StringBuffer();
		StringBuffer subString = new StringBuffer();
		char last = s.charAt(0);
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c != last || i == s.length() - 1) {
				if (i == s.length() - 1)
					subString.append(c);
				if (subString.length() >= THRESHOLD) {
					compressedBuffer.append(last + "#" + subString.length());
				} else {
					compressedBuffer.append(subString.toString());
				}
				subString = new StringBuffer();
				subString.append(c);
			} else {
				subString.append(c);
			}
			last = c;
		}
		return compressedBuffer.toString();

	}

	/**
	 * Just an alternate version of the other compression that uses slightly
	 * less space.
	 * 
	 * @param s
	 *            string to compress
	 * @return compressed version of s
	 */
	private static String compressAlternate(String s) {
		StringBuffer sb = new StringBuffer();
		char lastChar = s.charAt(0);
		int count = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) != lastChar || i == s.length() - 1) {
				if (i == s.length() - 1)
					count++;
				if (count >= THRESHOLD) {
					sb.append(lastChar + "#" + count);
					lastChar = s.charAt(i);
					count = 1;
				} else {
					for (int j = 0; j < count; j++) {
						sb.append(lastChar);
					}
					lastChar = s.charAt(i);
					count = 1;
				}
			} else {
				lastChar = s.charAt(i);
				count++;
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		List<String> list = Arrays.asList("aaaabbbcccaaaaccccccc", "abc",
				"bbbfhdjwuwuwuufffffkdkkkkkddddiiiiiqqooodllal", "hhheeelllppp", "jjjjhhhhssssiiiiqqqqllllzzzzppppoooo",
				"iiiiiiiiiiiiiiiiiiiiiiiiiiiii", "ggggtttkkkklllppppooouuuuuuuuuuuu");
		for (String s : list) {
			String comp = compress(s);
			System.out.println("Uncompressed: " + s);
			System.out.println("Compressed: " + comp);
			System.out.println("Decompressed: " + decompress(comp) + "\n");
		}

	}
}
