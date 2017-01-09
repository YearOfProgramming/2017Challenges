pub fn get_missing_num(v: Vec<u32>) -> u32 {
    let supposed_sum = (0..(v.len() + 1)).fold(0, |sum, x| sum + x);
    let actual_sum = v.into_iter().fold(0, |sum, x| sum + x);
    supposed_sum as u32 - actual_sum as u32
}
