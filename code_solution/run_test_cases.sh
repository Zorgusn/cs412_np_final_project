# Exact Solution
echo 'Exact Solution Results:' >> outcome.txt
echo >> outcome.txt

# test 1
python exact_solution.py < test_cases/input/1.txt >> test_cases/output/1_exact.txt
echo 'Test 1 Output:' >> outcome.txt
cat test_cases/output/1_exact.txt >> outcome.txt
echo >> outcome.txt

# test 2
python exact_solution.py < test_cases/input/2.txt >> test_cases/output/2_exact.txt
echo 'Test 2 Output:' >> outcome.txt
cat test_cases/output/2_exact.txt >> outcome.txt
echo >> outcome.txt

# test 3
python exact_solution.py < test_cases/input/3.txt >> test_cases/output/3_exact.txt
echo 'Test 3 Output:' >> outcome.txt
cat test_cases/output/3_exact.txt >> outcome.txt
echo >> outcome.txt

# test 4
python exact_solution.py < test_cases/input/4.txt >> test_cases/output/4_exact.txt
echo 'Test 4 Output:' >> outcome.txt
cat test_cases/output/4_exact.txt >> outcome.txt
echo >> outcome.txt

# test 5 minute
python exact_solution.py < test_cases/input/5min.txt >> test_cases/output/5min_exact.txt
echo 'Test 5 Output:' >> outcome.txt
cat test_cases/output/5min_exact.txt >> outcome.txt
echo >> outcome.txt

# test 20 minute
python exact_solution.py < test_cases/input/20min.txt >> test_cases/output/20min_exact.txt
echo 'Test 5 Output:' >> outcome.txt
cat test_cases/output/20min_exact.txt >> outcome.txt
echo >> outcome.txt



# Approx. Solution
echo >> outcome.txt
echo 'Approximate Solution Results:' >> outcome.txt
echo >> outcome.txt

# test 1
python approx_solution.py < test_cases/input/1.txt >> test_cases/output/1_approx.txt
echo 'Test 1 Output:' >> outcome.txt
cat test_cases/output/1_approx.txt >> outcome.txt
echo >> outcome.txt

# test 2
python approx_solution.py < test_cases/input/2.txt >> test_cases/output/2_approx.txt
echo 'Test 2 Output:' >> outcome.txt
cat test_cases/output/2_approx.txt >> outcome.txt
echo >> outcome.txt

# test 3
python approx_solution.py < test_cases/input/3.txt >> test_cases/output/3_approx.txt
echo 'Test 3 Output:' >> outcome.txt
cat test_cases/output/3_approx.txt >> outcome.txt
echo >> outcome.txt

# test 4
python approx_solution.py < test_cases/input/4.txt >> test_cases/output/4_approx.txt
echo 'Test 4 Output:' >> outcome.txt
cat test_cases/output/4_approx.txt >> outcome.txt
echo >> outcome.txt

# test 5 minute
python approx_solution.py < test_cases/input/5min.txt >> test_cases/output/5min_approx.txt
echo 'Test 5 Output:' >> outcome.txt
cat test_cases/output/5min_approx.txt >> outcome.txt
echo >> outcome.txt

# test 20 minute
python approx_solution.py < test_cases/input/20min.txt >> test_cases/output/20min_approx.txt
echo 'Test 5 Output:' >> outcome.txt
cat test_cases/output/20min_approx.txt >> outcome.txt
echo >> outcome.txt