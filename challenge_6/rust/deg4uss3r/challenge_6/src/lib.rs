pub fn string_numbers(input_numbers: Vec<u32>) -> Vec<String> {
    let mut output_vec: Vec<String> = Vec::new();
    let mut number_run = String::new();
    let mut current: u32 = 0;
    let mut count = 0;
    let mut first = 0;

    for i in input_numbers.iter() {
        if count == 0 {
            current = *i;
            first = *i;
            number_run += &current.to_string();
            count+=1;
        }
    
        else {
            if *i == current+1 {
                count +=1;
                current = *i;
            }
            
            else {
                output_vec.push(number_run + "->" + &current.to_string());
                number_run = String::new();
                current = *i;
                number_run += &current.to_string();
                first = *i;
                count = 1;
            }
        }
    }
    if first != current {
        output_vec.push(number_run + "->" + &current.to_string());
    }
    output_vec
}
