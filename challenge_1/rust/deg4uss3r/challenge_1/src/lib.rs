pub fn string_reverse (mut in_str: std::string::String) -> std::string::String {

    let mut out = "".to_string();
    let in_string = in_str.len();
    let mut i: usize = 0;

    while i < in_string {
        let out_temp = in_str.pop().unwrap().to_string();
        out += &out_temp;
        i+=1;
    }

    out.to_string()
}
