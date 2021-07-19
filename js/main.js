// comment

/*
multi
line
comment
*/

// can or cannot put ; at end

// alerts - block execution
// alert('Hello world')

// show on browser console
console.log('Hello World')  // can log multiple values at a time
console.error('Error')
console.warn('warn') // table, assert

// assign variables
// var - global variables - not recommended
// let - can reassign variable values
// const - constant - recommended unless we need changes
let age=30
age=31 // or
let score;
score=10
console.log(score)
const name='smita' // name='neha'  // error // const score  // error

// data types - string, number, boolean, null, undefined, symbol
const myname='Smita'
const myage=28 // or
const rating=4.5
const isCool=true
const x=null
const y=undefined // or
let z
console.log(typeof myage)

// string
const n = 'Smita Patankar'
const a = 28
const hello=`My name is ${n}. I am ${a}.`
console.log('My name is ' + n + '. I am ' + a + '.')  // or
console.log(`My name is ${n}. I am ${a}.`)
console.log(hello)
console.log(n.length)
console.log(n.toUpperCase())
console.log(n.toLowerCase())
console.log(n.substring(0,3))
console.log(n.substring(0,3).toUpperCase())
console.log(n.split(' P'))

// array
const mynumbers = new Array(1,2,3,4,5)  // or
const numbers = [1,2,3,4,'smita'] // const numbers=[1,2,3]  // error
numbers[5] = 6  // or
numbers.push('mango')
numbers.unshift('strawberries')
numbers.pop()
console.log(numbers)
console.log(numbers[0])
console.log(Array.isArray(numbers))
console.log(numbers.indexOf(2))  // -1 for missing ones
console.log(mynumbers.length)

//date
d = new Date("03-02-1992")
console.log(d)
console.log(d.getFullYear())

// object literals - key value pairs
const person = {
    fname: 'smita',
    fage: 28,
    hobbies: ['netflix', 'music'],
    address: {street: 'my street', city: 'my city'}
}
const {fname, fage, address: {city}} = person;
person.email='smita@gmail.com'
console.log(person)
console.log(person.fname, person.fage)
console.log(person.hobbies[1])
console.log(person.address.city)
console.log(city)

// object literals in arrays
const todos = [
    {
        id: 1,
        text: 'sleep',
        completed: true
    },
    {
        id: 2,
        text: 'eat',
        completed: true
    },
    {
        id: 3,
        text: 'workout',
        completed: false
    }
]
console.log(todos)
console.log(todos[2].text)

// json
const myjson = JSON.stringify(todos)
console.log(myjson)

// while loop
let i=0;
while(i <= 10) {
    console.log(`While loop number: ${i}`);
    i++;
}

// for loops
for(let i=0; i<=10;i++) {
    console.log(`For loop number: ${i}`)
}

// for loop on array
for(let t of todos){
    console.log(t.text)
}

// forEach loop
todos.forEach(
    function(todo){
        console.log(todo.text)
    }
)

// map
const todoText = todos.map(
    function(todo){
        return todo.text
    }
)
console.log(todoText)

// filter
const todoCompleted = todos.filter(
    function(todo){
        return todo.completed === true  // three === to match data type also
    }
)
console.log(todoCompleted)

// if else if else conditions
const xx = 5
const yy = 10
if(xx > 5 || yy > 11){
    console.log('xx is 10')
} else if(xx > 10 && yy > 10){
    console.log('xx is not 10')
} else {
    console.log('xx is < 10')
}

// ternary operators
const zz = 10
const color = x > 10 ? 'red': 'blue'
console.log(color)

//switch
switch(color){
    case 'red':
        console.log('color is red')
        break
    case 'blue':
        console.log('color is blue')
        break
    default:
        console.log('color is unknown')
        break
}

//functions
function addNums(num1, num2){
    return num1+num2
}
console.log(addNums(1,3))
console.log(addNums()) // NaN

//arrow functions
const addNumbers = num1 => num1+5
console.log(addNumbers(1))

// constructor function
function Person(f, l, dob){
    this.f = f
    this.l = l
    this.dob = new Date(dob)    
    Person.prototype.getBirthYear = function(){
        return this.dob.getFullYear()
    }
}

//class
class P{
    constructor(f, l, dob) {
        this.f = f
        this.l = l
        this.dob = new Date(dob)        
    }
    getBirthYear = function(){
        return this.dob.getFullYear()
    }
}

// instantiate object
const per1 = new P("smita", "patankar", "03-02-1992")
console.log(per1)
console.log(per1.f)
console.log(per1.getBirthYear())

// window
console.log(window) // window.alert("hey")

// selecting single element from dom
console.log(document.getElementById("my-form"))
console.log(document.querySelector(".container"))
console.log(document.querySelector("h1"))  //  recommended

// select multiple elements from dom
console.log(document.getElementsByClassName("item"))  // HTMLCollection not like array
console.log(document.getElementsByTagName("h1")) 
console.log(document.querySelectorAll(".item"))  // NodeList like an array

// modify DOM
const ul = document.querySelector(".items")
ul.firstElementChild.textContent = "smita" // ul.lastElementChild.remove() // ul.remove()
ul.children[1].innerText = "neha"
ul.lastElementChild.innerHTML = "<h4>hey<h4>"
const btn = document.querySelector(".btn")
btn.style.background = "red"

// events
btn.addEventListener('click', e => {
    e.preventDefault()  // stop form from submitting
    // console.log(e.target.className)
    document.querySelector("#my-form").style.background = "#ccc"
    document.querySelector("body").classList.add("bg-dark")
    document.querySelector(".items").lastElementChild.innerHTML = "<h1>hello</h1>"
    }
)
// mousehover
// mouseout