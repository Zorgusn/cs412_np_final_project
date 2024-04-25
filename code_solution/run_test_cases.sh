## Exact Solution Test Cases

# run exact solution with the simple test case (this is the provided one)
python exact_solution.py < test_cases/input/9.txt > test_cases/output/9_actual_exact.txt
# diff the simple expected and actual
diff test_cases/output/9_actual_exact.txt test_cases/output/9_expected.txt > test_cases/diffs/9_exact_diff.txt



## Approx. Solution Test Cases

