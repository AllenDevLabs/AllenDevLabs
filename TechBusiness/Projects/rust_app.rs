fn main() {
    let mut counter = 0;
    for _ in 0..5 {
        counter += 1;
    }
    println!("[RUST] Service log counter: {}", counter);
}
