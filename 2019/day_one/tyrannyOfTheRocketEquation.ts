import * as fs from 'node:fs';

const file = fs.readFile('input.txt', 'utf-8', (err, data) => {
    if(err) {
        console.error('cannot read local file')
        return
    }
    console.log(`File Content: ${data}`)
});