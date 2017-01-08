use std::vec::Vec;
use std::collections::HashMap;

pub fn majority_finder(input_vec: Vec<u64>) -> u64 {
    let mut counter = HashMap::new();
    let leng = input_vec.len()/2;

    for i in input_vec{
        let c = counter.entry(i).or_insert(1);
        *c+=1;
    }

    for (k,v) in counter{
        if v >= leng {
            return k;
        }
    }

    panic!("No majority value found!");
}
