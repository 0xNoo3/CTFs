use std::env;
use std::process;
use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};

fn custom_hash(input: &str, prime: u64, base: u64) -> u64 {
    let mut hash_value = 0u64;
    for c in input.chars() {
        hash_value = ((hash_value * base) % prime + c as u64) % prime;
    }
    hash_value
}

fn permute(input: &str, key: u64) -> String {
    let mut chars: Vec<char> = input.chars().collect();
    let len = chars.len();
    
    for i in 0..len {
        let j = ((i as u64 * key) % len as u64) as usize;
        chars.swap(i, j);
    }
    chars.into_iter().collect()
}

fn transform_input(input: &str) -> Vec<u8> {
    let seed = 0x13371337u32;
    let mut result = Vec::new();
    
    for (i, c) in input.chars().enumerate() {
        let transformed = ((c as u32) ^ ((seed >> (i % 32)) & 0xFF)) as u8;
        result.push(transformed);
    }
    
    for i in 0..result.len() {
        if i > 0 {
            result[i] = result[i] ^ (result[i-1] >> 3);
        }
    }
    
    result
}

fn time_based_mutation(input: &[u8]) -> Vec<u8> {
    // Get a stable seed from the day (ignoring hours/minutes/seconds)
    let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs() / 86400;
    let seed = now % 7; // Weekly cycle
    
    input.iter().enumerate().map(|(i, &byte)| {
        byte.wrapping_add(((i as u64 * seed) % 256) as u8)
    }).collect()
}

fn main() {
    println!("=== Chamber of Secrets ===");
    
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} <key>", args[0]);
        process::exit(1);
    }
    
    let user_input = &args[1];

    if user_input.len() < 10 {
        println!("Incorrect flag. The labyrinth remains unsolved.");
        process::exit(1);
    }

    let permuted = permute(user_input, 0x42424242);
    let transformed = transform_input(&permuted);
    let mutated = time_based_mutation(&transformed);

    let expected_checksums: HashMap<usize, u64> = [
        (0, 1910641389),
        (5, 978734675),
        (10, 639015185),
        (15, 434697744),
        (20, 977939275),
    ].iter().cloned().collect();

    let window_size = 5;
    let prime: u64 = 2147483647;
    let base: u64 = 256;
    
    let mut is_valid = true;
    
    for (start_pos, &expected) in &expected_checksums {
        if *start_pos + window_size > mutated.len() {
            is_valid = false;
            break;
        }
        
        let window: String = mutated[*start_pos..*start_pos+window_size]
            .iter()
            .map(|&b| b as char)
            .collect();
        
        let hash = custom_hash(&window, prime, base);

        if hash != expected {
            is_valid = false;
            break;
        }
    }

    let result_code = if is_valid {

        std::thread::sleep(std::time::Duration::from_millis(50));
        0xDEADBEEFu32
    } else {
        0xBADCAFEu32
    };
    
    match result_code {
        0xDEADBEEFu32 => println!("Congratulations! You've mastered the melody and lulled the beast."),
        _ => println!("Incorrect flag. The labyrinth remains unsolved."),
    }
}