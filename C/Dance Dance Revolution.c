#include <stdio.h>
#include <stdlib.h>
#define CASE 4
#define MIN(a, b) (a<b?a:b)

SIZE = 100000;

int get_cost(int p, int n) {
	if (p == n) return 1;
	else if (p == 0) return 2;
	else if ((p + n) % 2 == 0) return 4;
	else return 3;
}

int get_min_strength(int* nums, int*** dp, int index, int left, int right) {
	if (index >= SIZE) return 0;

	// 한 발판에 두 발을 두는 것 허용X -> DP에 초기에 매우 큰 값이 들어가므로 이것을 리턴한다.
	// 이렇게 하면, 이것의 상위 함수에서 min을 통해 걸러낼 수 있다.
	else if (left != 0 && left == right) return dp[left][right][index];

	// DP를 통한 최적화 
	else if(dp[left][right][index] < SIZE * CASE + 1) return dp[left][right][index];

	int cost1 = get_cost(left, nums[index]);
	int cost2 = get_cost(right, nums[index]);

	int res1 = cost1 + get_min_strength(nums, dp, index + 1, nums[index], right);
	int res2 = cost2 + get_min_strength(nums, dp, index + 1, left, nums[index]);

	// 두 개 중 하나를 선택하여 DP값 수정
	dp[left][right][index] = MIN(res1, res2);

	return dp[left][right][index];
}

int solution(int* nums) {
	// 예외 처리
	if (nums[0] == 0) return 0;
	else if (nums[1] == 0) return 2;

	int answer = SIZE * CASE + 1;
	int i, j, k;

	// DP 초기화
	int*** dp = malloc(sizeof(int**) * (CASE + 1));
	for (i = 0; i < CASE + 1; i++) {
		dp[i] = malloc(sizeof(int*) * (CASE + 1));
		for (j = 0; j < CASE + 1; j++) {
			dp[i][j] = malloc(sizeof(int) * SIZE);
			for (k = 0; k < SIZE; k++) {
				dp[i][j][k] = SIZE * CASE + 1;
			}
		}
	}

	// 재귀 호출
	answer = get_min_strength(nums, dp, 0, 0, 0);

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
	int* nums = malloc(sizeof(int) * (SIZE + 1));
	int i;

	for (i = 0; i < SIZE + 1; i++) {
		scanf("%d", &nums[i]);
		if (nums[i] == 0) {
			SIZE = i;
			break;
		}
	}

	printf("%d", solution(nums));

	return 0;
}