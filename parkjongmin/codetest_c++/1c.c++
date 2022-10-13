//정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    answer = num1 - num2;
    return answer;
}
//x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다.
//좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록
//solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> dot) {
    return dot[0] > 0 ? (dot[1] > 0 ? 1 : 4) : (dot[1] < 0 ? 3 : 2);
}
//정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    answer = num1*num2;
    return answer;
}

//중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
//예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때,
//중앙값을 return 하도록 solution 함수를 완성해보세요.
//파이썬
//def solution(array):
    // array = sorted(array)
    // length = len(array)//2
    // return array[length]

//hello world 출력
#include <iostream>
int main(int argc, char* argv[]) {
    std::cout << "Hello World" << std::endl;
    return 0;
}