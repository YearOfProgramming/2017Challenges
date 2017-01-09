pub fn get_sorted_squares(mut v: Vec<i32>) -> Vec<i32> {
    let mut splitting_index = 0;
    let mut has_positives = false;

    // Find the index of 0 to split if it is present
    for x in 0..(v.len() / 2) {
        let opposite_index = v.len() - (x + 1);

        if v[x] > 0 || v[opposite_index] > 0 {
            has_positives = true;
        }

        if v[x] == 0 {
            splitting_index = x;
            break;
        } else if v[opposite_index] == 0 {
            splitting_index = opposite_index;
            break;
        } else if opposite_index == x || opposite_index == x + 1 {
            break;
        }
    }

    match splitting_index {
        0 => { // No need to split at all, but if all negative should reverse
            match has_positives {
                true => v.into_iter().map(|x| x.pow(2)).collect::<Vec<i32>>(),
                false => v.into_iter().map(|x| x.pow(2)).rev().collect::<Vec<i32>>()
            }
        },
        _ => { // Gotta split, and it could be noncontiguous...
            let mut sorted_pows = vec![];

            let grtr_than_zero = v.split_off(splitting_index); // Split on zero

            let mut gtz_pows = grtr_than_zero.into_iter()
                                             .map(|x| x.pow(2))
                                             .collect::<Vec<i32>>();

            let mut ltz_pows = v.into_iter()
                                .map(|x| x.pow(2))
                                .rev()
                                .collect::<Vec<i32>>();
            
            // For all the fans of Merge Sort:
            // You've got two separate, already sorted lists,
            // ...so just take all the items in order!

            loop {
                if gtz_pows.is_empty() && ltz_pows.is_empty() {
                    break;
                } else if gtz_pows.is_empty() {
                    sorted_pows.push(ltz_pows.remove(0));
                } else if ltz_pows.is_empty() {
                    sorted_pows.push(gtz_pows.remove(0));
                } else {
                    if ltz_pows[0] < gtz_pows[0] {
                        sorted_pows.push(ltz_pows.remove(0));
                    } else {
                        sorted_pows.push(gtz_pows.remove(0));
                    }
                }
            };

            sorted_pows
        }
    }
}
