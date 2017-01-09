mod string_reverser;

fn main() {
	let input = "hello";
	println!("Entered String : {}", input);
	let result = string_reverser::reverse(input);
	println!("Reversed String : {}", result);
}