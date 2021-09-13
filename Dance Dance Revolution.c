#include <stdio.h>
#include <stdlib.h>
SIZE = 100000;
CASE = 4;

int get_cost(int p, int n) {
	if (p == n) return 1;
	else if (p == 0) return 2;
	else if ((p + n)%2 == 0) return 4;
	else return 3;
}

int dfs(int* nums, int ***dp, int index, int left, int right) {
	if (index >= SIZE) return 0;
	if ((left != 0 && left == right) || dp[left][right][index] < SIZE * CASE + 1) return dp[left][right][index];

	int cost1 = get_cost(left, nums[index]);
	int cost2 = get_cost(right, nums[index]);

	int res1 = cost1 + dfs(nums, dp, index + 1, nums[index], right);
	int res2 = cost2 + dfs(nums, dp, index + 1, left, nums[index]);
	
	if (res1 > res2)
		dp[left][right][index] = res2;
	else
		dp[left][right][index] = res1;

	return dp[left][right][index];
}

int solution(int* nums) {
	// 예외 처리
	if (nums[0] == 0) return 0;
	else if (nums[1] == 0) return 2;

	int answer = SIZE * CASE + 1;
	int i, j, k;

	// DP 초기화
	int*** dp = malloc(sizeof(int **) * (CASE+1));
	for (i = 0; i < CASE+1; i++) {
		dp[i] = malloc(sizeof(int *) * (CASE + 1));
		for (j = 0; j < CASE+1; j++) {
			dp[i][j] = malloc(sizeof(int) * SIZE);
			for (k = 0; k < SIZE; k++) {
				dp[i][j][k] = SIZE * CASE + 1;
			 }
		}
	}

	// 탐색
	answer = dfs(nums, dp, 0, 0, 0);

	// 메모리 해제
	for (i = 0; i < CASE + 1; i++) {
		for (j = 0; j < CASE + 1; j++) {
			free(dp[i][j]);
		}
		free(dp[i]);
	}
	free(dp);

	return answer;
}

int main() {
	int* nums = malloc(sizeof(int) * (SIZE+1));
	int i;

	for (i = 0; i < SIZE+1; i++) {
		scanf("%d", &nums[i]);
		if (nums[i] == 0) {
			SIZE = i;
			break;
		}
	}

	printf("%d", solution(nums));

	return 0;
}