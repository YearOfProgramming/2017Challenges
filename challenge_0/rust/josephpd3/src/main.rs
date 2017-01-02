macro_rules! hello {
    () => ("Hello, World!");
    ($str:expr) => (format!("{}{}{}", "Hello, ", $str, "!"));
}

fn main() {
    println!("{}", hello!());
    println!("{}", hello!("Joe"));
}

#[cfg(test)]
mod tests {
    
    #[test]
    fn generic_hello() {
        assert_eq!("Hello, World!", hello!());
    }

    #[test]
    fn specific_hello() {
        assert_eq!("Hello, Joe!", hello!("Joe"));
    }

}
