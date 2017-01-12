extern crate challenge_5;
use std::fs::File;
use std::path::Path;
use std::fs::read_dir;
use std::io::Read;
use challenge_5::find_odd_letter;

fn main(){
        let test_dir = Path::new("/Users/rthosfelt/bin/2017Challenges/challenge_5/rust/deg4uss3r/challenge_5/tests/testfiles"); 
        let sub = read_dir(test_dir).unwrap();
    for path in sub {
        let mut file_string = String::new();
        let mut strings: Vec<&str> = Vec::new();
        let mut f = File::open(path.unwrap().path()).unwrap();
        f.read_to_string(&mut file_string);

        strings = file_string.split("\n").collect();
        println!("{:?}", strings);        

        println!("{:?}", find_odd_letter(strings[0], strings[1]));
   }
}
