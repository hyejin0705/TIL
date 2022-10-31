// console.log('hello, javascript')


// console.log(add(2, 7))    // 9

// function add(num1, num2) {
// 	return num1 + num2
// }



// console.log(sub(7, 2))   // 5

// const sub = function (num1, num2) {
// 	return num1 - num2
// }


// const mySub = function nameSub (num1, num2) {
// 	return num1 - num2
// }

// console.log(mySub(1, 2))   // -1
// console.log(nameSub(1, 2)) // ReferenceError: nameSub is not defined


// const greeting = function (name = 'Anonymous') {
// 	return `Hi ${name}`
// }

// console.log(greeting())   // Hi Anonymous


// const threeArgs = function(arg1, arg2, arg3) {
// 	return [arg1, arg2, arg3]
// }

// console.log(threeArgs())
// console.log(threeArgs(1))
// console.log(threeArgs(1, 2))


// let parts = ['shoulders', 'knees']
// let lyrics = ['head', ...parts, 'and', 'toes']

// console.log(lyrics)


// const restOpr = function(arg1, arg2, ...restArgs) {
// 	return [arg1, arg2, restArgs]
// }

// console.log(restOpr(1, 2, 3, 4, 5))
// console.log(restOpr(1, 2))


// const greeting = function (name) {
// 	return `Hi ${name}`
// }


// // 1단계
// const greeting = (name) => {
// 	return `Hi ${name}`
// }


// // 2단계
// const greeting = name => {
// 	return `Hi ${name}`
// }


// // 3단계
// const greeting = name => `Hi ${name}`

// console.log(greeting('김싸피'))


// function (num) { return num ** 3 }

// // 1단계
// (num) => {return num ** 3}


// // 3단계
// (num) => num ** 3


// // IIFE
// console.log(((num) => num ** 3)(2))


// const numbers = [1, 2, 3, 4, 5]

// console.log(numbers[0])      // 1
// console.log(numbers[-1])     // undefined  => 음의 정수 인덱스를 불가능
// console.log(numbers.length)  // 5
// console.log(numbers[numbers.length - 1])   // 5


// const numbers = [1, 2, 3, 4, 5]

// numbers.reverse()
// console.log(numbers)  // [5, 4, 3, 2, 1]

// numbers.push(100)
// console.log(numbers)  // [1, 2, 3, 4, 5, 100]

// numbers.pop()
// console.log(numbers)  // [1, 2, 3, 4, 5]

// console.log(numbers.includes(1))   // true

// console.log(numbers.includes(100)) // false


// let result

// result = numbers.indexOf(3)  // 2
// console.log(result)

// result = numbers.indexOf(100)  // -1
// console.log(result)


// const numbers = [1, 2, 3, 4, 5]

// let result

// result = numbers.join()      // 1,2,3,4,5
// console.log(result)

// result = numbers.join('')    // 12345
// console.log(result)

// result = numbers.join(' ')   // 1 2 3 4 5
// console.log(result)

// result = numbers.join('-')   // 1-2-3-4-5
// console.log(result)


const chars = ['A', 'B', 'C', 'D']

// for loop
for (let idx = 0; idx < chars.length; idx++) {
	console.log(idx, chars[idx])
}


// for ... of
for (const char of chars) {
	console.log(char)
}


// for ... in
chars.forEach((char, idx) => {
	console.log(idx, char)
})


chars.forEach(char => {
	console.log(char)
})