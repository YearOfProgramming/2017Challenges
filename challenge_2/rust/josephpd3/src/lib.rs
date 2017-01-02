use std::collections::HashMap;

pub fn get_lonely_items(v: &[char]) -> Vec<char> {
    let mut lonely = vec![];
    let mut counts = HashMap::new();

    for ch in v {
        let mut present = true; // Flags are fun!

        match counts.get_mut(ch) {
            // Get mutable reference to entry
            Some(c) => { // If entry exists...
                *c = *c + 1; 
            },
            None => { // If entry doesn't exist...
                present = false;
            }
        }
        
        if !present { // Add base entry if didn't exist
            counts.insert(ch, 1);
        }
    }

    for (key, val) in counts.iter() {
        if *val as u32 == 1u32 { // Gotta deref value
            lonely.push(**key);
        }
    }

    lonely.sort(); // Return in lexicographical order
    lonely
}
