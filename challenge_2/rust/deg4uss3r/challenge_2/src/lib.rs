use std::vec::Vec;

pub fn find_lonely (mut input_vec: Vec<u64>) -> u64 {

    input_vec.sort();
    println!("{:?}", input_vec);

    for (count, i) in input_vec.iter().enumerate() {
        if count == 0 {
            if *i == input_vec[count+1] {
                continue;
            }
        }

        else if count == input_vec.len()-1 {
            if *i == input_vec[count-1] {
                panic!("No duplicate number found!"); 
            }
            else {
                return input_vec[count];
            }
        }

        if *i == input_vec[count-1] || *i == input_vec[count+1] {
            continue;
        }
  
        else {
                return input_vec[count];
        }
    }   
    
    panic!("should never get here!"); 
}
