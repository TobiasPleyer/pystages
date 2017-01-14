[env]
git_repo: sample_git_repo
branch_name: test_branch

[STAGES]
init
branch

[init]
short: Creates a new git repository named ${env:git_repo}
info: Will run the follwoing command
	mkdir ${env:git_repo} && cd ${env:git_repo} && git init
run: mkdir ${env:git_repo} && cd ${env:git_repo} && git init

[branch]
short: Creates a new branch ${env:branch_name}
info: Will run the follwoing command
	git checkout -b ${env:branch_name}
run: git checkout -b ${env:branch_name}
