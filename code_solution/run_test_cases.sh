## Exact Solution Test Cases

# run exact solution with the simple test case (this is the provided one)
python exact_solution.py < test_cases/input/simple.txt > test_cases/output/simple_actual.txt
# diff the simple expected and actual
diff test_cases/output/simple_actual.txt test_cases/output/simple_expected.txt > test_cases/diffs/simple_diff.txt



## Approx. Solution Test Cases

