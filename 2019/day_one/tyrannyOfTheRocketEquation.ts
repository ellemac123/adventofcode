/*
The Typescript solution for: https://adventofcode.com/2019/day/1
The answer to part one is: 3311492
*/ 
import * as fs from 'node:fs';

function readFileFunction(): Promise<string> {
    // read and return the input file text
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


function calculateEquation(listVelocities: Array<string>): number{
    /*
    Given a list of numbers, calculate the fuel required by 
    dividing its value by three, rounding down, and 
    then subtracting 2
    */
    let totalFuelRequired = 0;

    for(let velocity of listVelocities){
        let tempVelocity: number = (velocity as unknown) as number;

        totalFuelRequired += Math.floor(tempVelocity / 3) - 2
    }

    return totalFuelRequired;
}

async function main(): Promise<string> {
    /*
        Read the input file, and call associated functions to perfrom calculation for 
        the fuel required.
    */
    let fileData: string;

    try {
        fileData = await readFileFunction();
    } catch(err) {
        console.error('error reading file');
        return('error while trying to read file');
    }

    let velocities: Array<string> = fileData.split('\n');
    const totalFuelNeeded: number = calculateEquation(velocities);

    return `The answer to part one is: ${totalFuelNeeded}`; 
}

// run code and print the result to screen
let result: string = await main();
console.log(result);