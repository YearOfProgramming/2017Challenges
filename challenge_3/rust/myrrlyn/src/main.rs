#![feature(io)]

extern crate myrrlyn;

use myrrlyn::*;

use std::io::{
	Read,
	stdin,
};

fn main() {
	let inbuf: Vec<char> = stdin()
		.chars()
		.map(|x| x.unwrap())
		.filter(|&x| !x.is_whitespace())
		.collect();

	let outbuf = find_majority(inbuf);

	match outbuf {
		Some((k, v, l)) => {
			println!("The majority element, {}, occurred {} times out of {}", k, v, l);
		},
		_ => {
			println!("No majority element could be found.");
		}
	}
}
