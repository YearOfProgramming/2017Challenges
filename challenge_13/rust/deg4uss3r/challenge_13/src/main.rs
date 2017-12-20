use std::io;
use std::process;

fn find_pallendrome(number: String) -> bool {

    let mut x = 1;
    let  ten: u64 = 10;

    let number: f64 = match number.trim().parse::<f64>() {
            Ok(x) => x,
            Err(_) => panic!("{} Please check your input number!")
        };

    let digits = number.log10() + 1 as f64;

    while x < digits as usize {
        let last_dig = ((number % ten.pow(x as u32) as f64) / ten.pow(x as u32 - 1) as f64) as u64;
        let first_dig = ((number /(ten.pow(digits as u32  -x as u32)) as f64) % ten as f64) as u64;
        
        if first_dig == last_dig {
            x+=1;
            continue;
        }
        else {
            return false;
        }
    }

    true
}

fn main() {
        let mut in_text = String::new();
    
    match io::stdin().read_line(&mut in_text) {
        Ok(_) => {if find_pallendrome(in_text){println!("true");} else{println!("false");}},
        Err(e) => {println!("Error reading input {}", e); process::exit(1);}
    } 
}
