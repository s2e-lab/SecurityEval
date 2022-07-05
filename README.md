# SecurityEval
## Bandit

source bandit-env/bin/activate
bandit -r Testcases_Bad_Solution -f json -o Result/testcases_bad.json
bandit -r Testcases_Copilot -f json -o Result/testcases_copilot.json 
bandit -r Testcases_InCoder -f json -o Result/testcases_incoder.json

## CodeQL
codeql database create --language=python  '/Users/lsiddiqsunny/Documents/Notre Dame/Research/SecurityEval/Databases/Testcases_Bad_DB'
codeql database create --language=python  '/Users/lsiddiqsunny/Documents/Notre Dame/Research/SecurityEval/Databases/Testcases_Copilot_DB'
codeql database create --language=python  '/Users/lsiddiqsunny/Documents/Notre Dame/Research/SecurityEval/Databases/Testcases_Incoder_DB'