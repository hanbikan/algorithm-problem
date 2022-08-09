import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	private static int bisectLeft(ArrayList<Integer> nums, int value) {
		int left = 0;
		int right = nums.size()-1;
		int mid;
		
		while(left<=right) {
			mid = (left + right)/2;
			if(nums.get(mid) >= value) {
				right = mid-1;
			}else {
				left = mid+1;
			}
		}
		
		return left;
	}
	
	private static int solution(int[][] nums, int N) {
		int i, j;
		int index;
		Arrays.sort(nums, (o1, o2) -> o1[0] - o2[0]);
		
		// LIS
		ArrayList<Integer> stack = new ArrayList<Integer>();
		int stackLength = 0;
		for(i=0;i<N;i++) {
			index = bisectLeft(stack, nums[i][1]);
			
			if(index >= stackLength) {
				stack.add(nums[i][1]);
				stackLength += 1;
			}else {
				stack.set(index, nums[i][1]);
			}
		}
		
		return N - stackLength;
	}
	
	public static void main(String[] args) {
		int i;
		Scanner sn = new Scanner(System.in);
		int N = sn.nextInt();
		
		int[][] nums = new int[N][2];
		for(i=0;i<N;i++) {
			nums[i][0] = sn.nextInt();
			nums[i][1] = sn.nextInt();
		}

		System.out.println(solution(nums, N));
	}
}
