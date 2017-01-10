#![cfg_attr(test, feature(try_from))]

use std::collections::{
	HashMap,
};

/// Takes a list of characters and finds the characters that occur once.
/// This should execute in O(n) time, as access into a HashMap is roughly O(1).
/// TODO: Make this consume an iterator, instead of a collection.
pub fn find_unique_simple(data: Vec<char>) -> Vec<char> {
	//  Fun fact: in this particular use case, we could build the collection as
	//  HashMap::with_hasher(s) where s is a no-op.
	//
	//  I don't know how to do that, but it would cut down on access time.
	let mut counter = HashMap::new();

	//  Loop through the incoming data, counting characters as they arrive.
	for elem in data.into_iter() {
		//  Get the bucket for the current element. If it's not in there, insert
		//  0 as a starting value.
		let entry = counter.entry(elem).or_insert(0);
		//  Bump the count.
		*entry += 1;
	}

	let mut ret = counter
		//  Iterate through the counter, moving data out of it
		.drain()
		//  Throwing away elements whose counts are not 1.
		//  Elements coming out of drain() are (key, val) tuples.
		.filter(|&elem| elem.1 == 1)
		//  Also, strip whitespace.
		.filter(|&elem| !elem.0.is_whitespace())
		//  Strip the value half of the tuple
		.map(|e| e.0)
		//  And assemble the keys into a Vec
		.collect::<Vec<_>>();

	ret.sort();
	ret
}

#[cfg(test)]
mod tests {
	use super::*;
	use std::convert::TryFrom;

	//  Get a collection of sample data. Should reduce to '5'.
	fn sample() -> Vec<char> {
		[2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 9, 8, 7, 8, 7, ]
			.into_iter()
			//  Translate the numerals into their ASCII equivalents.
			.map(|x| char::try_from(*x + 48).unwrap())
			.collect()
	}

	#[test]
	fn test_simple() {
		assert_eq!(find_unique_simple(sample()), ['5']);
	}
}
