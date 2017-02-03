use std::io;
use std::process;

fn find_closes(in_text: String) -> bool {
    let mut stack_collector = Vec::new();
    
    for c in in_text.chars() {
        if c == '(' {
            stack_collector.push(')');
        }
        if c == '{' {
            stack_collector.push('}');
        }
        if c == '[' {
            stack_collector.push(']');
        }
        if c == '<' {
            stack_collector.push('>');
        }

        if c == '>' || c == ']' || c == '}' || c == ')' {
            if stack_collector.len() == 0 {
                return false;
            }

            if c == stack_collector[stack_collector.len()-1] {
                stack_collector.pop();
            }
            else {
                return false;
            }
        }
    }
    if stack_collector.len() == 0   {
        return true;
    }
    else {
        return false;
    }
}

fn main() {

    let mut in_text = String::new();
    
    match io::stdin().read_line(&mut in_text) {
        Ok(_) => {if find_closes(in_text){println!("true");} else{println!("false");}},
        Err(e) => {println!("Error reading input {}", e); process::exit(1);}
    } 
}
