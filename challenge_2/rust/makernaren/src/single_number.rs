use std::collections::HashMap;

// Finds the unique character in given array
pub fn find_single(input: Vec<i32>) -> i32 {
	// Create hashmap, let the key be the element in input array
	// and value be its count. Then return the key with count of 1.
    let mut occurances: HashMap<i32, i32> = HashMap::new();
    for key in input {
    *occurances.entry(key).or_insert(0) += 1;
    }
   let mut result: i32 = 0;
    for (key, val) in occurances.iter() {
        if *val == 1 {
            result = key.to_owned();
        }
    }
    return result
}


