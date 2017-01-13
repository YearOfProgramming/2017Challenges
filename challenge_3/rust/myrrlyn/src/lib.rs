use std::cmp::Eq;
use std::collections::HashMap;
use std::fmt::Display;
use std::hash::Hash;

/// Find the majority element in a collection, if there is one.
///
/// Generic over any type which can be displayed, equated, and hashed.
pub fn find_majority<T: Display + Eq + Hash>(data: Vec<T>) -> Option<(T, i32, usize)> {
	let mut counter = HashMap::new();

	let len = data.len();

	for elem in data {
		let entry = counter.entry(elem).or_insert(0);
		*entry += 1;
	}

	//  Find the key and value that are the majority element.
	let (mk, mv) = counter
		//  Consume the collection
		.drain()
		//  And collapse it into a single value
		.fold((None, 0), |acc, elem| {
			//  If the current element occurs more often than the accumulator,
			//  keep this instead
			if elem.1 > acc.1 {
				(Some(elem.0), elem.1)
			}
			//  Otherwise hold on to the accumulator
			else {
				acc
			}
		});

	//  If the collapsed max value is more than half, return a success
	if mv as f32 > len as f32 / 2.0 {
		Some((mk.unwrap(), mv, len))
	}
	//  If the collapsed max value fails to reach majority, return a failure
	else {
		None
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn find_most() {
		let maj = find_majority(vec![1, 2, 2, 3, 3, 3, 3,]);
		assert_eq!(Some((3, 4, 7)), maj);
	}

	#[test]
	fn fail_find() {
		let maj = find_majority(vec![1, 2, 3]);
		assert_eq!(None, maj);
	}
}
