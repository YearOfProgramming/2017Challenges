

pub fn find_odd_letter(s: &str, t: &str) -> char {

    for i in t.chars() {
        if s.contains(&i.to_string()){
            continue;
        }
        else {
            return i;
        }
    }

    panic!("No odd letter found, ruh roh!");
}
