import * as fs from 'node:fs';

function readFileFunction(): Promise<string> {
    return new Promise((resolve, reject) => {
        fs.readFile('input.txt', 'utf-8', (err, data) => {
            if(err) {
                console.error('cannot read local file')
                reject('cannot read local file')
            }
            resolve(data)
        });
    }
)}

async function main() {
    try {
        const fileData = await readFileFunction();
        console.log(fileData);
    } catch(err) {
        console.error('error reading file');
    }
}

main();