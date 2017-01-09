Ranges
---
Scans through the array, looking for continuous ranges. When it encounters a range, it reduces it into a 'start->end' string. It then creates a copy of the array without the range that has been made. It then recursively calls ranges on that array, making a list of range strings.
