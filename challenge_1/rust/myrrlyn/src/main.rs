/*! String Reverser

Not actually a string reverser, because text is hard.
!*/

use std::io::{
	self,
};

fn main() {
	//  Programs need user interfaces to be useful, friends
	println!("Hello and welcome to myrrlyn's magical string reverser!");
	println!("Enter a string you'd like to see reversed!");
	println!("This will run forever, until you enter \"quit\".");

	//  Run forever, until the user quits.
	loop {
		//  Rust follows the POSIX conventions for I/O, and requires a separate
		//  buffer into which stdin will be read.
		let mut buf = String::new();
		//  The read_line() call returns the count of bytes read. We don't care.
		let _ = io::stdin().read_line(&mut buf);
		//  Always have an escape route.
		if buf == "quit\n" {
			break;
		}
		//  Herein lies the cheating
		let reverse: String = buf
			//  Get an iterator over all 32-bit chars in the string (note that
			//  the UTF-8 byte sequence gets transformed into a Vec<u32> when
			//  reading into a String).
			.chars()
			//  Reverse the order of the iterator! Mwahahaha!
			.rev()
			//  And fuse the iterator back into a String.
			.collect();
		//  Chop the \n, which is now at the front, so that output doesn't suck.
		println!("{}", reverse.trim_left());
	}
}
