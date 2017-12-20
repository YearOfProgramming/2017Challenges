

pub fn find_odd_letter(s: &str, t: &str) -> Option<char>{

    for i in t.chars() {
        if s.contains(&i.to_string()){
            continue;
        }
        else {
            return Some(i);
        }
    }

    
    None
}
