import * as fs from 'node:fs';



function calculateFuel(fileInput) {

}



const file = fs.readFile('input.txt', 'utf-8', (err, data) => {
    if(err) {
        console.error('cannot read local file')
        return
    }
    return data
});

console.log(file)