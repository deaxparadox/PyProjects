const displayVal = async (a) => {
    document.querySelector("#displayVal").innerHTML = a
}
const displayArray = async (a) => {
    document.querySelector("#displayArray").innerHTML = a
}

const UpdateHistory = async (total, string) => {
    data = JSON.stringify({
        total: total,
        string: string.join("")
    })
    fetch("http://localhost:8000/history/", {
        method: 'post',
        body: data,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json()
    }).then((res) => {
        if (res.status === 201) {
            console.log("Post successfully created!")
        }
    }).catch((error) => {
        console.log(error)
    })
}

const add = async (a, b) => {
    return a + b
}
const sub = async (a, b) => {
    return a - b
}
const mul = async (a, b) => {
    return a * b
}
const div = async (a, b) => {
    return a / b
}

const calculator = async (a, b, opt) => {
    if (opt === "+") {
        return add(a, b)
    } else if (opt === "-") {
        return sub(a, b)
    } else if (opt === "*") {
        return mul(a, b)
    } else if (opt === "/") {
        return div(a, b)
    }
}


class Fun {
    constructor() {
        this.a = ""
        this.b = ""
        this.opt = null
        this.display = ""
        this.arr = []
    }

    async work(val) {
        const num = Number(val)

        if (isNaN(num)) {
            // if num is not number
            if (!this.opt) {
                // if opt is not defined
                // define it 

                this.opt = val
                console.log
                this.arr.push(this.opt)

                this.display = this.a + " " + this.opt
                displayVal(this.display)

            } else {
                console.log(this.a, this.b, this.opt)

                // if opt is define 
                // check current val 
                //  and perform operation

                if (this.b.length > 0 && val === "=") {
                    // is opt is =

                    this.a = parseFloat(this.a)
                    this.b = parseFloat(this.b)
                    this.a = await calculator(this.a, this.b, this.opt)
                    console.log(this.a)

                    await UpdateHistory(this.a, this.arr)

                    // set the displayVal
                    displayVal(this.a)

                    this.b = ""
                    this.opt = null
                    this.arr = []

                } else {
                    // if opt is operator

                    if (this.b.length > 0) {
                        this.a = parseFloat(this.a)
                        this.b = parseFloat(this.b)
                        this.a = await calculator(this.a, this.b, this.opt)
                        console.log(this.a)

                        // set the displayVal
                        this.display = this.a + " " + this.opt
                        displayVal(this.display)

                        this.b = ""
                        this.opt = val
                        this.arr.push(this.opt)
                    } else {
                        console.log("Invalid operation")
                    }

                }
            }
        } else {
            // if num is number
            if (!this.opt) {
                // if opt is not defined
                // save val in a 

                this.a += val;
                console.log(this.a)

                // to display
                this.display = this.a
                displayVal(this.a)
                this.arr.push(this.a)
            } else {
                // if opt is define 
                // save val is b

                this.b += val;
                console.log(this.b)
                this.display = this.a + " " + this.opt + " " + this.b
                displayVal(this.display)
                this.arr.push(this.b)
            }
        }
    }


}


let f = new Fun()
async function forever() {

    let keys = document.querySelectorAll(".key");

    for (let key of keys) {
        key.addEventListener("click", () => {
            keyValue = key.innerHTML
            console.log(keyValue);
            if (keyValue === "C") {
                f.a = ""
                f.b = ""
                f.opt = null
                displayVal(0)
            } else {
                f.work(keyValue);
            }

        })
    }
}



forever();