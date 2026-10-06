//#include <stdio.h>
//#include "fibonacci.h"

//int main(void) {
//    int term = 10;
//    printf("The %dth Fibonacci number is %d\n", term, fibonacci(term));
//    printf("The theoretical Golden Ratio is %f\n", golden_ratio_approx(term));
//    return 0?;
//}

#include "utest.h"
#include "fibonacci.h"

UTEST(fibonacci, terms_1_to_10) {
    int expected[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    for (int term = 1; term <= 10; term++) {
        EXPECT_EQ(expected[term - 1], fibonacci(term));
    }
}

UTEST_MAIN()
