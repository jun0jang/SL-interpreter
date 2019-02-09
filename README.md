  
### 언어 사양

#### 연산자

단항 연산자  
`+`(양수), `-`(음수), `!`(부정)

이항 연산자  
`+`(덧셈), `-`(뺄셈), `*`(곱셈), `/`(나숫셈), `%`(나머지)  
`<`(왼쪽이 작다), `<=`(왼쪽이 작거나 같다),   
`>`(왼쪽이 크다), `>=`(왼쪽이 크거나 같다),  
`==`(같다), `!=`(같지 않다), `&&`(AND), `||`(OR)

#### 변수

- `var` 키워드를 통해 변수를 선언 가능하지만 선언하지 않아도 사용할 수 있다.  
- `global` 키워드를 사용해 함수 내부에서 전역 변수임을 표현할 수 있다.  
- 1차원 배열을 지원하며 배열의 경우 var 키워드를 통한 선언이 필요하다.  
- 정수, 실수, 문자열 데이터 타입을 지원하고 동적으로 변경 가능하다.  

```
var arr[10]  // arr[0] ~ arr[9]가 유효하다.
arr[0] = 1
arr[1] = 1.1
arr[2] = "String"
  
a = "Hello world"
```

#### 함수

- 함수의 기본 반환값은 정수 1이다.  
- 인수로 배열을 전달할 수 없다.  
- 내장 함수 `print`, `input`, `toint`, `tostring`을 제공한다.

```
func add(a, b) {
  return a + b
}
  
add(1, 2)          // 서브루틴으로 이용 가능
num1 = add(5, 10)  // 함수로 이용 가능
  
name = input()
print(name)
print(name, " ", num1)
  
num1 = toint(1.0)
num1 = tostring(num1)
```

#### 제어문

- `if`, `for`, `while`이 존재한다.  
- `for`의 기본 `step`는 1이다.  
- 반복문의 경우 `break`, `continue` 키워드를 사용할 수 있다.  

```
if a == 1 {
  x = 10
}
elif a == 2 {
  x = 50
}
else {
  x = 90
}
  
n = 1
sum = 0
while n <= 10 {
   sum = sum + n
   n = n + 1
}
  
sum = 0
for n = 1 to 10 {
  sum = sum + n
}
  
sum = 0
for n = 1 to 10 step 2 {
  sum = sum + n
}
  
sum = 0
for n = 10 to 1 step -1 {
  sum = sum + n
}
```
