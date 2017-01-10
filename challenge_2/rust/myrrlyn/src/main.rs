#![feature(io)]

extern crate myrrlyn;

use myrrlyn::*;

use std::io::{
	Read,
	stdin,
};

fn main() {
	//  Collect data from stdin
	let inbuf: Vec<char> = stdin().chars().map(|x| x.unwrap()).collect();

	//  Process the data
	let outbuf = find_unique_simple(inbuf);

	//  Print the results
	for elem in outbuf.into_iter() {
		println!("Unique element: {}", elem);
	}
}
