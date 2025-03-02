/*
The Typescript solution for: https://adventofcode.com/2020/day/1

The solution for part one is: 319531
*/ 
import * as fs from 'node:fs'; 

function calculateRepair(inputData: string[]): any {
    // Find two values that sum to 2020 in the list and return the product
    for(let value of inputData){
        let numVal = Number(value);
        let numDiff = 2020 - numVal;

        if(inputData.includes(numDiff.toString())){
            return numDiff * numVal; 
        }
    }

    return -1;
}

function readFileFunction(): Promise<string> {
    // read and return the input file text
    return new Promise((resolve, reject) => {
        fs.readFile('input.txt', 'utf-8', (err, data) => {
            if(err) {
                console.error('cannot read local file');
                reject('cannot read local file');
            }
            resolve(data);
        });
    }
)}

async function main(): Promise<number | string> {
    let fileData: string; 

    try{
        fileData = await readFileFunction();
    } catch(err){
        return('Error while reading file '); 
    }

    let repairData: Array<string> = fileData.split('\n');
    let partOneSolution: number = calculateRepair(repairData); 

    return partOneSolution;
}

let answer = await main(); 
console.log(`The solution for part one is: ${answer}`);