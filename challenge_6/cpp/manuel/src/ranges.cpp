#include <vector>
#include <string>

namespace ranges {

    std::string represent_range (int start, int end) {

        return std::to_string(start) + "->" + std::to_string(end);
    }

    std::vector<std::string> get_ranges (std::vector<int> numbers) {
        // [1, 2, 4, 5] to ["1->2", "4->5"]

        std::vector<std::string> ranges;

        int length = numbers.size();
        int start = numbers[0];
        int end = numbers[0];

        for( int i = 1; i < length; i++ ) {

            // If there's a gap of >=2 and the current range is > 0
            if( end + 1 < numbers[i] && start != end) {

                ranges.push_back(represent_range(start, end));
                start = numbers[i];
            } else if (end + 1 < numbers[i] && start == end) {
                // if the gap is >=2, but the range is 0
                // skip

                start = numbers[i];
            }

            end = numbers[i];
        }

        // Final range
        if (start != end) {
            ranges.push_back(represent_range(start, end));
        }

        return ranges;
    }

}
